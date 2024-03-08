#!/usr/bin/env python3

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'reading_realm_with_django_project.settings')

import django



django.setup()
from realm.models import Category, Book


def populate():
    classics_books = [
        {'title': 'Pride and Prejudice',
            'url': 'https://en.wikipedia.org/wiki/Pride_and_Prejudice',
            'estimatedreadingtime': 'Estimated Reading Time: 7 hours',
            'author': 'https://en.wikipedia.org/wiki/J._R._R._Tolkien'},
        {'title': 'To Kill a Mockingbird',
            'url': 'https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird',
         'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 20 minutes',
         'author': 'https://en.wikipedia.org/wiki/Harper_Lee'}
    ]

    fantasy_books = [
        {'title': 'The Hobbit',
         'url': 'https://en.wikipedia.org/wiki/The_Hobbit',
            'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 20 minutes'},
        {'title': 'Harry Potter and the Philosophers Stone',
            'url': 'https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone',
         'estimatedreadingtime': 'Estimated Reading Time: 3 hours and 43 minutes'}
    ]

    historical_books = [
        {'title': 'The Book Thief',
         'url': 'https://en.wikipedia.org/wiki/The_Book_Thief',
            'estimatedreadingtime': 'Estimated Reading Time: 10 hours and 8 minutes'},
        {'title': 'All the Light We Cannot See',
            'url': 'https://en.wikipedia.org/wiki/All_the_Light_We_Cannot_See',
         'estimatedreadingtime': 'Estimated Reading Time: 8 hours and 51 minutes'}
    ]

    scifi_books = [
        {'title': 'Dune',
            'url': 'https://en.wikipedia.org/wiki/Dune_(novel)',
         'estimatedreadingtime': 'Estimated Reading Time: 12 hours and 32 minutes'},
        {'title': 'Ender’s Game',
         'url': 'https://en.wikipedia.org/wiki/Ender%27s_Game',
            'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 57 minutes'}
    ]

    thriller_books = [
        {'title': 'The Girl with the Dragon Tattoo',
            'url': 'https://en.wikipedia.org/wiki/The_Girl_with_the_Dragon_Tattoo',
         'estimatedreadingtime': 'Estimated Reading Time:11 hours and 12 minutes'},
        {'title': 'Gone Girl',
            'url': 'https://en.wikipedia.org/wiki/Gone_Girl_(novel)',
         'estimatedreadingtime': 'Estimated Reading Time: 9 hours and 20 minutes', }
    ]

    cats = {
        'Classics': {'books': classics_books},
        'Fantasy': {'books': fantasy_books},
        'Historical': {'books': historical_books},
        'SciFi': {'books': scifi_books},
        'Thriller': {'books': thriller_books}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['books']:
            add_book(c, **p)

    for c in Category.objects.all():
        for p in Book.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_book(cat, title, url, author="", estimatedreadingtime=0,  *args, **kwargs,):
    p = Book.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.estimatedreadingtime = f"{estimatedreadingtime}"
    p.author = author
    p.save()
    return p


def add_cat(name):
    c, created = Category.objects.get_or_create(name=name)
    if created:
        c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
