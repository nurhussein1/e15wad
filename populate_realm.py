import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reading_realm_with_django_project.settings')

import django
django.setup()
from realm.models import Category, Page

def populate():
    classics_books = [
        {'title': 'Pride and Prejudice', 'url': 'https://en.wikipedia.org/wiki/Pride_and_Prejudice'},
        {'title': 'To Kill a Mockingbird', 'url': 'https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird'}
    ]
    
    fantasy_books = [
        {'title': 'The Hobbit', 'url': 'https://en.wikipedia.org/wiki/The_Hobbit'},
        {'title': 'Harry Potter and the Philosophers Stone', 'url': 'https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone'}
    ]
    
    historical_books = [
        {'title': 'The Book Thief', 'url': 'https://en.wikipedia.org/wiki/The_Book_Thief'},
        {'title': 'All the Light We Cannot See', 'url': 'https://en.wikipedia.org/wiki/All_the_Light_We_Cannot_See'}
    ]
    
    scifi_books = [
        {'title': 'Dune', 'url': 'https://en.wikipedia.org/wiki/Dune_(novel)'},
        {'title': 'Ender’s Game', 'url': 'https://en.wikipedia.org/wiki/Ender%27s_Game'}
    ]
    
    thriller_books = [
        {'title': 'The Girl with the Dragon Tattoo', 'url': 'https://en.wikipedia.org/wiki/The_Girl_with_the_Dragon_Tattoo'},
        {'title': 'Gone Girl', 'url': 'https://en.wikipedia.org/wiki/Gone_Girl_(novel)'}
    ]
    
    cats = {
        'Classics': {'pages': classics_books, 'views': 128, 'likes': 64}, #example likes and views will be updated later
        'Fantasy': {'pages': fantasy_books, 'views': 256, 'likes': 128},
        'Historical': {'pages': historical_books, 'views': 64, 'likes': 32},
        'SciFi': {'pages': scifi_books, 'views': 512, 'likes': 256},
        'Thriller': {'pages': thriller_books, 'views': 1024, 'likes': 512}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    # Updated add_cat function to handle views and likes
    c, created = Category.objects.get_or_create(name=name)
    if created:
        c.views = views
        c.likes = likes
        c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
