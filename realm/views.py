from django.shortcuts import render
from django.http import HttpResponse

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

def register(request):
 
    context_dict = {'boldmessage': 'this is the register page, test that context_dict works'}
    return render(request, 'realm/register.html', context=context_dict)

def login(request):
 
    context_dict = {'boldmessage': 'this is the login page, test that context_dict works'}
    return render(request, 'realm/login.html', context=context_dict)

def categories(request):
 
    context_dict = {'boldmessage': 'this is the categories page, test that context_dict works'}
    return render(request, 'realm/categories.html', context=context_dict)

def popularbooks(request):
 
    context_dict = {'boldmessage': 'this is the popular books page, test that context_dict works'}
    return render(request, 'realm/popularbooks.html', context=context_dict)

def account(request):
 
    context_dict = {'boldmessage': 'this is the account page, test that context_dict works'}
    return render(request, 'realm/account.html', context=context_dict)

def profilepicture(request):
 
    context_dict = {'boldmessage': 'this is the profile picture page, test that context_dict works'}
    return render(request, 'realm/account/profilepicture.html', context=context_dict)

def myreviews(request):
 
    context_dict = {'boldmessage': 'this is the my reviews page, test that context_dict works'}
    return render(request, 'realm/account/myreviews.html', context=context_dict)

def mybooks(request):
 
    context_dict = {'boldmessage': 'this is the my books page, test that context_dict works'}
    return render(request, 'realm/account/mybooks.html', context=context_dict)

def historical(request):
 
    context_dict = {'boldmessage': 'this is the historicals page, test that context_dict works'}
    return render(request, 'realm/categories/historical.html', context=context_dict)

def scifi(request):
 
    context_dict = {'boldmessage': 'this is the science fiction page, test that context_dict works'}
    return render(request, 'realm/categories/scifi.html', context=context_dict)

def classics(request):
 
    context_dict = {'boldmessage': 'this is the classics page, test that context_dict works'}
    return render(request, 'realm/categories/classics.html', context=context_dict)

def thriller(request):
 
    context_dict = {'boldmessage': 'this is the thrillers page, test that context_dict works'}
    return render(request, 'realm/categories/thriller.html', context=context_dict)

def fantasy(request):
 
    context_dict = {'boldmessage': 'this is the fantasy page, test that context_dict works'}
    return render(request, 'realm/categories/fantasy.html', context=context_dict)