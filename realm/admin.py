from django.contrib import admin
from realm.models import Category, Book
from realm.models import UserProfile

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url') 
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
    
admin.site.register(Category, CategoryAdmin)


admin.site.register(Book, BookAdmin)

admin.site.register(UserProfile)