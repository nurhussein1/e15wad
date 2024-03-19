from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime

# Create your models here.

def default_rental_end_date():
    return timezone.now() + datetime.timedelta(weeks=1)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()
    description = models.TextField(default="No Desctiption Availible")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    description=models.TextField(null=True)
    slug=models.SlugField(unique=True)
    # bookcover = models.ImageField()
    estimatedreadingtime=models.TextField(null=True,default="0hrs 30mins")
    author = models.URLField()

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Book,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user=models.OneToOneField(User,models.CASCADE,null=True)
    favourite_categories = models.ManyToManyField(Category)
    selected_favourites = models.BooleanField(default=False)
    profilepicture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    rental_end_date = models.DateTimeField(default=default_rental_end_date)

    def is_active(self):
        return self.rental_date + datetime.timedelta(weeks=1) > timezone.now()

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f'Review {self.id} by {self.user.username} on {self.book.title}'
