from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from realm.models import Book,Category, Review,UserProfile
from registration.forms import RegistrationForm
from django.utils.translation import gettext, gettext_lazy as _


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Category
        fields = ('name',)

class UserForm(RegistrationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    profilepicture = forms.ImageField(required = False)

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the book.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the book.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Book
        exclude = ('category',)

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(x, f"{x} Stars") for x in range(1, 6)], widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = ['comment', 'rating'] 

