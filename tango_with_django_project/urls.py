# tango_with_django_project URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path
from django.urls import include
from e15wad import views

urlpatterns = [
    path('', views.index, name='index'),
    path('e15wad/', include('e15wad.urls')),
    # The above maps any URLs starting with e15wad/ to be handled by e15wad.
    path('admin/', admin.site.urls),
 ]
