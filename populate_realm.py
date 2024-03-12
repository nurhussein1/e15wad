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
         'description' : "Pride and Prejudice is the second novel by English author Jane Austen, published in 1813. A novel of manners, it follows the character development of Elizabeth Bennet, the protagonist of the book" ,
            'url': 'https://en.wikipedia.org/wiki/Pride_and_Prejudice',
            'estimatedreadingtime': 'Estimated Reading Time: 7 hours',
            'author': 'https://en.wikipedia.org/wiki/J._R._R._Tolkien'},
        {'title': 'To Kill a Mockingbird',
         'description' : "To Kill a Mockingbird takes place in the fictional town of Maycomb, Alabama, during the Great Depression. The protagonist is Jean Louise (“Scout”) Finch, an intelligent though unconventional girl who ages from six to nine years old during the course of the novel. She is raised with her brother, Jeremy Atticus" ,
            'url': 'https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird',
         'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 20 minutes',
         'author': 'https://en.wikipedia.org/wiki/Harper_Lee'}
    ]

    fantasy_books = [
        {'title': 'The Hobbit',
         'description' : "In a HOLE in the ground there lived a hobbit.”. Bilbo Baggins lives a quiet, peaceful life in his comfortable hole at Bag End. One day his comfort is shattered by the arrival of Gandalf the Wizard, who persuades Bilbo to set out on an adventure with a group of thirteen" ,
         'url': 'https://en.wikipedia.org/wiki/The_Hobbit',
            'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 20 minutes'},
        {'title': 'Harry Potter and the Philosophers Stone',
         'description' : "Harry Potter and the Philosopher's Stone is the first installment of the Harry Potter book series by J.K. Rowling12. The story follows the events of Harry Potters first year at Hogwarts, and works as an introduction to the world of magic" ,
            'url': 'https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone',
         'estimatedreadingtime': 'Estimated Reading Time: 3 hours and 43 minutes'}
    ]

    historical_books = [
        {'title': 'The Book Thief',
         'description' : "So begins Liesel's love affair with books and words, and soon she is stealing from Nazi book-burnings, the mayor's wife's library . . . wherever there are books to be found." ,
         'url': 'https://en.wikipedia.org/wiki/The_Book_Thief',
            'estimatedreadingtime': 'Estimated Reading Time: 10 hours and 8 minutes'},
        {'title': 'All the Light We Cannot See',
         'description' : "Marie-Laure lives in Paris near the Museum of Natural History, where her father works. When she is twelve, the Nazis occupy Paris and father and daughter flee to the walled citadel of Saint-Malo, where Marie-Laure’s reclusive great uncle lives in a tall house by the sea. With them they carry what might be the museum’s most valuable and dangerous jewel." ,
            'url': 'https://en.wikipedia.org/wiki/All_the_Light_We_Cannot_See',
         'estimatedreadingtime': 'Estimated Reading Time: 8 hours and 51 minutes'}
    ]

    scifi_books = [
        {'title': 'Dune',
         'description' : "Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world where the only thing of value is the “spice” melange, a drug capable of extending life and enhancing consciousness. Coveted across the known universe, melange is a prize worth killing for..." ,
            'url': 'https://en.wikipedia.org/wiki/Dune_(novel)',
         'estimatedreadingtime': 'Estimated Reading Time: 12 hours and 32 minutes'},
        {'title': 'Ender’s Game',
         'description' : "Andrew 'Ender' Wiggin thinks he is playing computer simulated war games; he is, in fact, engaged in something far more desperate. The result of genetic experimentation, Ender may be the military genius Earth desperately needs in a war against an alien enemy seeking to destroy all human life. The only way to find out is to throw Ender into ever harsher training, to chip away and find the diamond inside, or destroy him utterly. Ender Wiggin is six years old when it begins." ,
         'url': 'https://en.wikipedia.org/wiki/Ender%27s_Game',
            'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 57 minutes'
        }
    ]

    thriller_books = [
        {'title': 'The Girl with the Dragon Tattoo',
         'description' : "Disgraced crusading journalist Mikael Blomkvist has no idea of the levels of conspiracy he will uncover when is enlisted to investigate the unsolved disappearance nearly forty years ago of a Swedish industrialist’s niece. And when the pierced and tattooed computer savant Lisbeth Salander joins him, together they unearth layers and layers of secrets and scandals that permeate the highest levels of society, from politics to finance to the legal system itself--at the bottom of which lies unimaginable cruelty perpetrated on the weak." ,
            'url': 'https://en.wikipedia.org/wiki/The_Girl_with_the_Dragon_Tattoo',
         'estimatedreadingtime': 'Estimated Reading Time:11 hours and 12 minutes'},
        {'title': 'Gone Girl',
            'description' : "These are the questions Nick Dunne finds himself asking on the morning of his fifth wedding anniversary when his wife Amy suddenly disappears. The police suspect Nick. Amy's friends reveal that she was afraid of him, that she kept secrets from him. He swears it isn't true. A police examination of his computer shows strange searches. " ,
            'url': 'https://en.wikipedia.org/wiki/Gone_Girl_(novel)',
         'estimatedreadingtime': 'Estimated Reading Time: 9 hours and 20 minutes',
        }
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


def add_book(cat, title,description, url, author="", estimatedreadingtime=0,  *args, **kwargs,):
    p = Book.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.estimatedreadingtime = f"{estimatedreadingtime}"
    p.description = f"{description}"
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
