
from django.urls import path
from e15wad import views

app_name = 'e15wad'
urlpatterns = [
 
 path('', views.index, name='index'),

]