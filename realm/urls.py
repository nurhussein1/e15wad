
from django.urls import path
from realm import views

app_name = 'realm'
urlpatterns = [
 
 path('', views.home, name='Home'),
 path('about/', views.about, name = 'About'),
 path('register/',views.register,name = 'Register'),

]