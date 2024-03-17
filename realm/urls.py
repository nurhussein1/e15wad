
from django.urls import path,reverse
from realm import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'realm'

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('categories/', views.categories, name='Categories'),
    path('popularbooks/', views.popularbooks, name='PopularBooks'),
    path('account/', views.account, name='Account'),
    path('account/profilepicture/', views.profilepicture, name='ProfilePictures'),
    path('account/myreviews/', views.myreviews, name='MyReviews'),
    path('account/mybooks/', views.mybooks, name='MyBooks'),
    path('FavouriteCategories', views.favourite_category, name='FavouriteCategories'),
    path('Recommendations', views.recommendations, name='Recommendations'),
    path('categories/<slug:category_name_slug>/', views.category, name='category',),
    path('book/<slug:book_name_slug>/', views.book, name='book',),
    path('purchase/<int:book_id>/', views.purchase, name='Purchase'),
    path('rent/',views.rent, name='Rent'),
    path('orderConfirmation/<int:book_id>/', views.orderConfirmation, name='orderConfirmation'),
    path('confirm_purchase/<int:book_id>/', views.confirm_purchase, name='confirm_purchase'),
    path('read/<slug:book_slug>/', views.read_book, name='read_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)