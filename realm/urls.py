
from django.urls import path,reverse
from realm import views

app_name = 'realm'

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    #path('register/', views.userauth, name='register',kwargs={'user_control_form_slug':'register'}),
    # path('login/', views.login, name='Login'),
    path('categories/', views.categories, name='Categories'),
    path('popularbooks/', views.popularbooks, name='PopularBooks'),
    path('account/', views.account, name='Account'),
    path('account/profilepicture/', views.profilepicture, name='ProfilePictures'),
    path('account/myreviews/', views.myreviews, name='MyReviews'),
    path('account/mybooks/', views.mybooks, name='MyBooks'),
    path('FavouriteCategories', views.favourite_category, name='FavouriteCategories'),
    path('Recommendations', views.recommendations, name='Recommendations'),
    # path('categories/historical/', views.historical, name='Historical'),
    # path('categories/scifi/', views.scifi, name='SciFi'),
    path('categories/<slug:category_name_slug>/', views.category, name='category',),
    path('book/<slug:book_name_slug>/', views.book, name='book',),
    path('purchase/',views.purchase, name='Purchase'),
    path('rent/',views.rent, name='Rent'),
    path('orderConfirmation/',views.orderConfirmation, name='OrderConfirmation')
    #path('login/', views.userauth, name='login',kwargs={'user_control_form_slug':'login'}),
    # path('categories/thriller/', views.thriller, name='Thriller'),
    # path('categories/fantasy/', views.fantasy, name='Fantasy'),
]