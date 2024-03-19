from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from realm.models import Category, Book, Purchase, UserProfile, Rental
from realm.forms import UserForm
from django.forms import HiddenInput,Field
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from .models import Book, Rental, Wishlist
from django.contrib import messages
from django.utils import timezone
import datetime

from os.path import join

# Create your views here.
def home(request):
 
 # Construct a dictionary to pass to the template
 context_dict = {'boldmessage': 'test that context_dict works'}
 # Return a rendered response to send to the client.
 return render(request, 'realm/home.html', context=context_dict)

def about(request):
 context_dict = {'boldmessage': 'this is the about page, test that context_dict works'}
 return render(request, 'realm/about.html', context=context_dict)

def categories(request):
    context_dict = {
        'boldmessage': 'this is the categories page, test that context_dict works',
        'categories': Category.objects.all()
    }
    return render(request, 'realm/categories.html', context=context_dict)

def popularbooks(request):
    
    context_dict = {}
  
    books_list = Book.objects.order_by('-views')[:5]
    context_dict ['boldmessage'] ='this is the popular books page, test that context_dict works'
    context_dict['books'] = books_list

    return render(request, 'realm/popularbooks.html', context=context_dict)


def get_profile_picture_url(request):
    profile_picture_url = None
    if request.user.is_authenticated:
        profile = getattr(request.user, 'userprofile', None)
        if profile and profile.profilepicture:
            profile_picture_url = profile.profilepicture.url
    return profile_picture_url

def basepfp(request):
    profile_picture_url = get_profile_picture_url(request)
    return render(request, 'realm/base.html', {'profile_picture_url': profile_picture_url})

# Other view functions remain unchanged



def myreviews(request):
 
    context_dict = {'boldmessage': 'this is the my reviews page, test that context_dict works'}
    return render(request, 'realm/account/myreviews.html', context=context_dict)

def mybooks(request):
    if request.user.is_authenticated:
        purchased_books = Purchase.objects.filter(user=request.user).select_related('book')
        rented_books = Rental.objects.filter(user=request.user, rental_end_date__gte=timezone.now()).select_related('book')
        context_dict = {
            'purchased_books': purchased_books,
            'rented_books': rented_books,
        }
    return render(request, 'realm/account/mybooks.html', context=context_dict)

def mywishlist(request):
    if request.user.is_authenticated:
        context_dict = {}
        
        wishlist_items = Wishlist.objects.filter(user=request.user)
        context_dict['wishlist'] = wishlist_items
        
    return render(request, 'realm/account/mywishlist.html', context=context_dict)


def category(request,category_name_slug):
    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Book.objects.filter(category=category)
        context_dict['books'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['books'] = None
    
    return render(request, 'realm/categories/category.html', context=context_dict)

def book(request, book_name_slug):
    context_dict = {}
    try:
        book = Book.objects.get(slug=book_name_slug)
        user_has_purchased = False
        user_has_active_rental = False  # Initialize the flag for active rental

        if request.user.is_authenticated:
            user_has_purchased = Purchase.objects.filter(user=request.user, book=book).exists()
            # Check for active rental
            user_has_active_rental = Rental.objects.filter(
                user=request.user, 
                book=book, 
                rental_end_date__gte=timezone.now()
            ).exists()

        context_dict['book'] = book
        context_dict['user_has_purchased'] = user_has_purchased
        context_dict['user_has_active_rental'] = user_has_active_rental
        
        # if the user tried to access the read_book page without purchasing or renting, show a message
        if 'just_tried_to_read' in request.session and request.session['just_tried_to_read']:
            messages.info(request, 'You must purchase or rent the book to read it.')
            del request.session['just_tried_to_read']  # remove the flag after showing the message
    except Book.DoesNotExist:
        context_dict['book'] = None

    return render(request, 'realm/book/book.html', context_dict)

def webimg(request):

    return HttpResponse(b"",status=404,reason="Not Found")

def account(request):
    profile_picture_url = None
    if request.user.is_authenticated:
        profile = getattr(request.user, 'userprofile', None)
        if profile and profile.profilepicture:
            profile_picture_url = profile.profilepicture.url
    return render(request, 'realm/account.html', {'profile_picture_url': profile_picture_url})

def profilepicture(request):
 
    if request.method == 'POST':
        if 'profile_pic' in request.FILES:
            profile = request.user.userprofile
            profile.profilepicture = request.FILES['profile_pic']
            profile.save()
    return render(request, 'realm/account/profilepicture.html')

def purchase(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user.is_authenticated:
        already_purchased = Purchase.objects.filter(user=request.user, book=book).exists()
        if already_purchased:
            messages.info(request, 'You have already purchased this book.')
            return redirect('realm:book', book_name_slug=book.slug)
            
    context_dict = {'boldmessage': 'this is the Purchase page, ', 'book': book}
    return render(request, 'realm/purchaseOrRent/purchase.html', context_dict)

def add_to_wishlist(request, book_id):
    # Get the book object and the current user's profile
    book = get_object_or_404(Book, id=book_id)
    if request.user.is_authenticated:
        # Check if the book is already in the user's wishlist
        if Wishlist.objects.filter(user=request.user, book=book).exists():
          # Book is already in the wishlist, you may want to handle this differently
            messages.info(request, 'This book is currently on your Wishlist.')
            return redirect('realm:book', book_name_slug=book.slug)
    
        # Create a new wishlist item
        wishlist_item = Wishlist(user=request.user, book=book)
        wishlist_item.save()
    return redirect('realm:book', book_name_slug=book.slug)



def rent(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        if request.user.is_authenticated:
            Rental.objects.create(user=request.user, book=book, rental_end_date=timezone.now() + datetime.timedelta(weeks=1))
            messages.success(request, "You have successfully rented this book for a week.")
            return redirect('realm:orderConfirmation', book_id=book.id)
        else:
            messages.warning(request, "You must be logged in to rent a book.")
            return redirect('realm:login')
    else:
        if request.user.is_authenticated:
            active_rental = Rental.objects.filter(user=request.user, book=book, rental_end_date__gte=timezone.now()).exists()
            if active_rental:
                messages.info(request, "You're currently renting this book.")
                return redirect('realm:book', book_name_slug=book.slug)
        context = {'book': book}
        return render(request, 'realm/purchaseOrRent/rent.html', context)

def orderConfirmation(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'realm/purchaseOrRent/orderConfirmation.html', context)

def favourite_category(request):
    category_list = Category.objects.all()
    context_dict={}
    context_dict['categories'] = category_list
    context_dict['user'] = request.user
    context_dict['userprofile'] = request.user.userprofile
    selected_categories = []
    for category in category_list:
        if request.POST.get(category.name):
            selected_categories.append(category)
    if hasattr(request.user, 'userprofile'):
        for category in selected_categories:
            request.user.userprofile.favourite_categories.add(category)
            if request.user.userprofile.selected_favourites == False:
                request.user.userprofile.selected_favourites = True
            request.user.userprofile.save()
    return render(request, 'realm/favouriteCategories.html', context=context_dict)

def recommendations(request):
    context_dict = {}
    recommended = []
    if hasattr(request.user, 'userprofile'):
        context_dict['userprofile'] = request.user.userprofile
        if request.user.userprofile.selected_favourites == True:
            favourites = request.user.userprofile.favourite_categories.all()
            for i in favourites:
                book = Book.objects.filter(category=i)[0]
                recommended.append(book)
    context_dict['recommended_books'] = recommended
    return render(request, 'realm/Recommendations.html', context=context_dict)

def confirm_purchase(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    Purchase.objects.create(user=request.user, book=book)
    return redirect('realm:orderConfirmation', book_id=book.id)

def confirm_rental(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        if request.user.is_authenticated:
            rental = Rental.objects.create(user=request.user, book=book, rental_end_date=timezone.now() + datetime.timedelta(weeks=1))
            messages.success(request, "You have successfully rented this book for a week.")
            return redirect('realm:orderConfirmation', rental.id)
        else:
            messages.error(request, "You need to be logged in to rent a book.")
            return redirect('login')
    else:
        return redirect('realm:book', book_name_slug=book.slug)

def read_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    user_has_purchased = False
    user_has_active_rental = False

    if request.user.is_authenticated:
        user_has_purchased = Purchase.objects.filter(user=request.user, book=book).exists()
        user_has_active_rental = Rental.objects.filter(user=request.user, book=book, rental_date__gt=timezone.now()-datetime.timedelta(weeks=1)).exists()

    if not (user_has_purchased or user_has_active_rental):
        messages.info(request, "You must purchase or rent the book to read it.")
        return redirect('realm:book', book_name_slug=book.slug)

    context = {'book': book}
    return render(request, 'realm/read_book.html', context)
