from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from realm.models import Category, Book, UserProfile
from realm.forms import UserForm
from django.forms import HiddenInput,Field

from os.path import join

# Create your views here.
def home(request):
 
 # Construct a dictionary to pass to the template
 context_dict = {'boldmessage': 'test that context_dict works'}
 # Return a rendered response to send to the client.
 return render(request, 'realm/home.html', context=context_dict)

def about(request):

 # Construct a dictionary to pass to the template
 context_dict = {'boldmessage': 'this is the about page, test that context_dict works'}
 # Return a rendered response to send to the client.
 return render(request, 'realm/about.html', context=context_dict)

def categories(request):
    context_dict = {
        'boldmessage': 'this is the categories page, test that context_dict works',
        'categories': Category.objects.all()
    }
    return render(request, 'realm/categories.html', context=context_dict)

def popularbooks(request):
 
    context_dict = {'boldmessage': 'this is the popular books page, test that context_dict works'}
    return render(request, 'realm/popularbooks.html', context=context_dict)




def myreviews(request):
 
    context_dict = {'boldmessage': 'this is the my reviews page, test that context_dict works'}
    return render(request, 'realm/account/myreviews.html', context=context_dict)

def mybooks(request):
 
    context_dict = {'boldmessage': 'this is the my books page, test that context_dict works'}
    return render(request, 'realm/account/mybooks.html', context=context_dict)

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

def book(request,book_name_slug):
    context_dict = {}
    
    try:
        book = Book.objects.get(slug=book_name_slug)
        context_dict['book'] = book
    except Book.DoesNotExist:
        context_dict['book'] = None
    
    return render(request, 'realm/book/book.html', context=context_dict)

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

def purchase(request):
    context_dict = {'boldmessage': 'this is the Purchase page, '}
    return render(request, 'realm/purchaseOrRent/purchase.html', context=context_dict)

def rent(request):
    context_dict = {'boldmessage': 'this is the Rent page, '}
    return render(request, 'realm/purchaseOrRent/rent.html', context=context_dict)

def orderConfirmation(request):
    context_dict = {'boldmessage': 'this is the Confirmation page, '}
    return render(request, 'realm/purchaseOrRent/orderConfirmation.html', context=context_dict)

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