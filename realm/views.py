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

""" def register(request):
 
    context_dict = {'boldmessage': 'this is the register page, test that context_dict works'}
    return render(request, 'realm/register.html', context=context_dict)

def login(request):
 
    context_dict = {'boldmessage': 'this is the login page, test that context_dict works'}
    return render(request, 'realm/login.html', context=context_dict) """

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
    # Retrieve the profile picture URL
    profile_picture_url = None
    if request.user.is_authenticated:


        ##display profile
        if hasattr(request.user, 'userprofile'):
            profile_picture = request.user.userprofile.profilepicture
            if profile_picture:
                profile_picture_url = profile_picture.url

    return render(request, 'realm/account.html', {'profile_picture_url': profile_picture_url})

def profilepicture(request):
 
    if request.method == 'POST':
        # Assuming the user profile is related to the User model
        
        profile = request.user.userprofile
        profile.profilepicture = request.FILES['profile_pic']
        profile.save()
        # Redirect to the user's profile page

    return render(request, 'realm/account/profilepicture.html')

def purchase(request):
    context_dict = {'boldmessage': 'this is the Purchase page, '}
    return render(request, 'realm/purchaseOrRent/purchase.html', context=context_dict)

def rent(request):
    context_dict = {'boldmessage': 'this is the Rent page, '}
    return render(request, 'realm/purchaseOrRent/rent.html', context=context_dict)
    

""" def userauth(request:HttpRequest,user_control_form_slug):
    form=UserForm()
    if(user_control_form_slug!="register"):
        for i in ("email",):
            email:Field =form.fields.get(i)
            email.is_hidden=True
            email.widget=HiddenInput()
            email.required=False
        
    if(request.method.lower()=="post"):
        if(user_control_form_slug=="register"):
            userProfile,created= UserProfile.objects.get_or_create(defaults=request.POST,name=request.POST.get("username"))
            if(not created):
                return render(request,template_name=join("realm",f"login.html"),context={'form':form,'ctx':user_control_form_slug},status=200)
        elif(user_control_form_slug=="login"):
            try:
                userProfile = UserProfile.objects.get(name=request.POST.get("username"))
            except UserProfile.DoesNotExist:
                form.add_error("username",f"No User {request.POST.get('username')} found")
                return render(request,template_name=join("realm",f"login.html"),context={'form':form,'ctx':user_control_form_slug},status=200)


    form.hidden_fields
    return render(request,template_name=join("realm",f"login.html"),context={'form':form,'ctx':user_control_form_slug},status=200)
  """
