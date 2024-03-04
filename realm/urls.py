
from django.urls import path
from realm import views

app_name = 'realm'
urlpatterns = [
 
 path('', views.index, name='index'),

]