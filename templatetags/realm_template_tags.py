from django import template
from realm.models import Category

register = template.Library()

@register.inclusion_tag('realm/categories/category.html')
def get_category_list():
    return {'categories': Category.objects.all()}