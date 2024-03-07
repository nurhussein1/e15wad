
from django.urls import path
from realm import views

app_name = 'realm'
app_name = 'realm'
urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('register/', views.register, name='Register'),
    path('login/', views.login, name='Login'),
    path('categories/', views.categories, name='Categories'),
    path('popularbooks/', views.popularbooks, name='PopularBooks'),
    path('account/', views.account, name='Account'),
    path('account/profilepicture/', views.profilepicture, name='ProfilePictures'),
    path('account/myreviews/', views.myreviews, name='MyReviews'),
    path('account/mybooks/', views.mybooks, name='MyBooks'),
    path('categories/historical/', views.historical, name='Historical'),
    path('categories/scifi/', views.scifi, name='SciFi'),
    path('categories/classics/', views.classics, name='Classics'),
    path('categories/thriller/', views.thriller, name='Thriller'),
    path('categories/fantasy/', views.fantasy, name='Fantasy'),
]