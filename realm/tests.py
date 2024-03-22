from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Book, Rental, Review, Wishlist, Category
from .views import home, about, categories, popularbooks, myreviews, mybooks, mywishlist, category, book, purchase, add_to_wishlist, rent, orderConfirmation, read_book, delete_review
from django.urls import reverse

class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='secret')

        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.book = Book.objects.create(title='Test Book', slug='test-book', category=self.category)

        self.review = Review.objects.create(book=self.book, user=self.user, rating=5, content='Great book!')
        self.wishlist = Wishlist.objects.create(user=self.user, book=self.book)
        self.rental = Rental.objects.create(user=self.user, book=self.book)

    def test_home_view(self):
        request = self.factory.get(reverse('realm:home'))
        request.user = self.user
        response = home(request)
        self.assertEqual(response.status_code, 200)


    from django.http import HttpResponseRedirect

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    # Check if the user owns the review
    if review.user != request.user:
        messages.error(request, "You cannot delete someone else's review.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    review.delete()
    messages.success(request, "Review deleted successfully.")

    # Redirect to the appropriate page based on the referrer
    referrer = request.META.get('HTTP_REFERER', '/')
    if 'book' in referrer:
        request.session['review_deletion_referrer'] = 'book'
        return HttpResponseRedirect(reverse('realm:book', kwargs={'book_name_slug': review.book.slug}))
    elif 'myreviews' in referrer:
        request.session['review_deletion_referrer'] = 'myreviews'
        return HttpResponseRedirect(reverse('realm:myreviews'))
    else:
        request.session['review_deletion_referrer'] = 'unknown'
        return HttpResponseRedirect(referrer)

    def test_delete_review_non_owner(self):
        user2 = User.objects.create_user(username='testuser2', email='test2@example.com', password='secret')
        request = self.factory.post(reverse('realm:delete_review', kwargs={'review_id': self.review.id}))
        request.user = user2
        response = delete_review(request, self.review.id)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Review.objects.filter(pk=self.review.id).exists())
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from realm.models import Book, Category, Review, Wishlist, Rental

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='secret')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.book = Book.objects.create(title='Test Book', slug='test-book', category=self.category)
        self.review = Review.objects.create(book=self.book, user=self.user, rating=5, content='Great book!')
        self.wishlist = Wishlist.objects.create(user=self.user, book=self.book)
        self.rental = Rental.objects.create(user=self.user, book=self.book)

    def test_home_view(self):
        response = self.client.get(reverse('realm:Home'))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(reverse('realm:About'))
        self.assertEqual(response.status_code, 200)

    def test_categories_view(self):
        response = self.client.get(reverse('realm:Categories'))
        self.assertEqual(response.status_code, 200)

    def test_popularbooks_view(self):
        response = self.client.get(reverse('realm:PopularBooks'))
        self.assertEqual(response.status_code, 200)

    def test_account_view(self):
        response = self.client.get(reverse('realm:Account'))
        self.assertEqual(response.status_code, 200)

    def test_profilepicture_view(self):
        response = self.client.get(reverse('realm:ProfilePictures'))
        self.assertEqual(response.status_code, 200)

    def test_myreviews_view(self):
        response = self.client.get(reverse('realm:MyReviews'))
        self.assertEqual(response.status_code, 200)

    def test_mybooks_view(self):
        response = self.client.get(reverse('realm:MyBooks'))
        self.assertEqual(response.status_code, 200)

    def test_mywishlist_view(self):
        response = self.client.get(reverse('realm:MyWishList'))
        self.assertEqual(response.status_code, 200)

    def test_favourite_category_view(self):
        response = self.client.get(reverse('realm:FavouriteCategories'))
        self.assertEqual(response.status_code, 200)

    def test_recommendations_view(self):
        response = self.client.get(reverse('realm:Recommendations'))
        self.assertEqual(response.status_code, 200)

    def test_category_view(self):
        response = self.client.get(reverse('realm:category', kwargs={'category_name_slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)

    def test_book_view(self):
        response = self.client.get(reverse('realm:book', kwargs={'book_name_slug': self.book.slug}))
        self.assertEqual(response.status_code, 200)

    def test_purchase_view(self):
        response = self.client.get(reverse('realm:purchase_book', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200)

    def test_rent_view(self):
        response = self.client.get(reverse('realm:rent_book', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200)

    def test_order_confirmation_view(self):
        response = self.client.get(reverse('realm:orderConfirmation', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200)

    def test_read_book_view(self):
        response = self.client.get(reverse('realm:read_book', kwargs={'book_slug': self.book.slug}))
        self.assertEqual(response.status_code, 200)

    def test_confirm_purchase_view(self):
        response = self.client.get(reverse('realm:confirm_purchase', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200)

    def test_confirm_rental_view(self):
        response = self.client.get(reverse('realm:confirm_rental', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200)

    def test_add_to_wishlist_view(self):
        response = self.client.get(reverse('realm:add_to_wishlist', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200)

    def test_delete_review_view(self):
        response = self.client.get(reverse('realm:delete_review', kwargs={'review_id': self.review.id}))
        self.assertEqual(response.status_code, 302)  
