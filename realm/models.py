from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

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
    #email=models.EmailField(null=True)
    #prefrences = models.TextChoices()
    profilepicture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username
