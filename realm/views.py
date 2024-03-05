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