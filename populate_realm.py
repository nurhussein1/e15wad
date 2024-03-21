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
            'author': 'https://en.wikipedia.org/wiki/Jane_Austen',
            'image':'static/bookCovers/classics_books/PrideAndPrejudice.jpg',
            'views':12},

        {'title': 'To Kill a Mockingbird',
         'description' : "To Kill a Mockingbird takes place in the fictional town of Maycomb, Alabama, during the Great Depression. The protagonist is Jean Louise (“Scout”) Finch, an intelligent though unconventional girl who ages from six to nine years old during the course of the novel. She is raised with her brother, Jeremy Atticus" ,
            'url': 'https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird',
         'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 20 minutes',
         'author': 'https://en.wikipedia.org/wiki/Harper_Lee',
         'image':'static/bookCovers/classics_books/ToKillAMockingbird.jpg',
         'views':122}
    ]

    fantasy_books = [
        {'title': 'Harry Potter and the Philosophers Stone',
         'description' : "Harry Potter and the Philosopher's Stone is the first installment of the Harry Potter book series by J.K. Rowling12. The story follows the events of Harry Potters first year at Hogwarts, and works as an introduction to the world of magic" ,
            'url': 'https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone',
         'estimatedreadingtime': 'Estimated Reading Time: 3 hours and 43 minutes',
         'author': 'https://en.wikipedia.org/wiki/J._K._Rowling',
         'image':'static/bookCovers/fantasy_books/HarryPotter.jpg' ,
         'views':112},

         {'title': 'The Hobbit',
         'description' : "In a HOLE in the ground there lived a hobbit.”. Bilbo Baggins lives a quiet, peaceful life in his comfortable hole at Bag End. One day his comfort is shattered by the arrival of Gandalf the Wizard, who persuades Bilbo to set out on an adventure with a group of thirteen" ,
         'url': 'https://en.wikipedia.org/wiki/The_Hobbit',
            'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 20 minutes',
            'author': 'https://en.wikipedia.org/wiki/J._R._R._Tolkien',
            'image':'static/bookCovers/fantasy_books/TheHobbit.jpg',
            'views':1321}
    ]

    historical_books = [
        {'title': 'All the Light We Cannot See',
         'description' : "Marie-Laure lives in Paris near the Museum of Natural History, where her father works. When she is twelve, the Nazis occupy Paris and father and daughter flee to the walled citadel of Saint-Malo, where Marie-Laure’s reclusive great uncle lives in a tall house by the sea. With them they carry what might be the museum’s most valuable and dangerous jewel." ,
            'url': 'https://en.wikipedia.org/wiki/All_the_Light_We_Cannot_See',
         'estimatedreadingtime': 'Estimated Reading Time: 8 hours and 51 minutes',
         'author': 'https://en.wikipedia.org/wiki/Anthony_Doerr',
         'image':'static/bookCovers/historical_books/AllTheLightWeCannotSee.jpg',
         'views': 131},

        {'title': 'The Book Thief',
         'description' : "So begins Liesel's love affair with books and words, and soon she is stealing from Nazi book-burnings, the mayor's wife's library . . . wherever there are books to be found." ,
         'url': 'https://en.wikipedia.org/wiki/The_Book_Thief',
            'estimatedreadingtime': 'Estimated Reading Time: 10 hours and 8 minutes',
            'author': 'https://en.wikipedia.org/wiki/Markus_Zusak',
        'image':'static/bookCovers/historical_books/TheBookThief.jpg',
        'views':13}
    ]

    scifi_books = [
        {'title': 'Dune',
         'description' : "Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world where the only thing of value is the “spice” melange, a drug capable of extending life and enhancing consciousness. Coveted across the known universe, melange is a prize worth killing for..." ,
            'url': 'https://en.wikipedia.org/wiki/Dune_(novel)',
         'estimatedreadingtime': 'Estimated Reading Time: 12 hours and 32 minutes',
         'author': 'https://en.wikipedia.org/wiki/Frank_Herbert',
         'image':'static/bookCovers/scifi_books/Dune.jpg',
         'views':156},
        
        {'title': 'Ender’s Game',
         'description' : "Andrew 'Ender' Wiggin thinks he is playing computer simulated war games; he is, in fact, engaged in something far more desperate. The result of genetic experimentation, Ender may be the military genius Earth desperately needs in a war against an alien enemy seeking to destroy all human life. The only way to find out is to throw Ender into ever harsher training, to chip away and find the diamond inside, or destroy him utterly. Ender Wiggin is six years old when it begins." ,
         'url': 'https://en.wikipedia.org/wiki/Ender%27s_Game',
            'estimatedreadingtime': 'Estimated Reading Time: 5 hours and 57 minutes',
            'author': 'https://en.wikipedia.org/wiki/Orson_Scott_Card',
            'image':'static/bookCovers/scifi_books/EndersGame.jpg',
            'views':312
        }
    ]

    thriller_books = [
        {'title': 'Gone Girl',
            'description' : "These are the questions Nick Dunne finds himself asking on the morning of his fifth wedding anniversary when his wife Amy suddenly disappears. The police suspect Nick. Amy's friends reveal that she was afraid of him, that she kept secrets from him. He swears it isn't true. A police examination of his computer shows strange searches. " ,
            'url': 'https://en.wikipedia.org/wiki/Gone_Girl_(novel)',
         'estimatedreadingtime': 'Estimated Reading Time: 9 hours and 20 minutes',
         'author': 'https://en.wikipedia.org/wiki/Gillian_Flynn',
         'image':'static/bookCovers/thriller_books/GoneGirl.jpg',
         'views':32
        },

        {'title': 'The Girl with the Dragon Tattoo',
         'description' : "Disgraced crusading journalist Mikael Blomkvist has no idea of the levels of conspiracy he will uncover when is enlisted to investigate the unsolved disappearance nearly forty years ago of a Swedish industrialist’s niece. And when the pierced and tattooed computer savant Lisbeth Salander joins him, together they unearth layers and layers of secrets and scandals that permeate the highest levels of society, from politics to finance to the legal system itself--at the bottom of which lies unimaginable cruelty perpetrated on the weak." ,
            'url': 'https://en.wikipedia.org/wiki/The_Girl_with_the_Dragon_Tattoo',
         'estimatedreadingtime': 'Estimated Reading Time:11 hours and 12 minutes',
         'author': 'https://en.wikipedia.org/wiki/Stieg_Larsson',
         'image':'static/bookCovers/thriller_books/TheGirlWithTheDragonTattoo.jpg',
         'views':2}
    ]

    cats = {
        'Classics': {'description': 'Classics books represent a timeless treasure trove of literature, capturing the essence of different eras and cultures while transcending the limitations of time and space. These works are revered for their profound insights into the human condition, intricate character development, and enduring themes that resonate across generations. From the eloquent prose of Jane Austens "Pride and Prejudice," which explores the complexities of societal norms and romantic relationships in Regency-era England, to Harper Lees "To Kill a Mockingbird," a poignant portrayal of racial injustice and moral growth in the American South during the 1930s, classics books transport readers to worlds both familiar and fantastical, inviting introspection and fostering empathy. Whether delving into the depths of existential dilemmas, grappling with ethical quandaries, or celebrating the triumph of the human spirit, classics books continue to inspire, enlighten, and enrich readers of all ages, leaving an indelible mark on literary history.','books': classics_books},
        'Fantasy': {'description': 'Fantasy books transport readers to enchanting realms where magic and adventure intertwine, captivating imaginations with tales of epic quests, mythical creatures, and heroic protagonists. Within the pages of fantasy literature, readers embark on extraordinary journeys through mystical lands, encountering wizards, dragons, elves, and other fantastical beings. These narratives often explore themes of good versus evil, the power of friendship and bravery, and the triumph of the human spirit against insurmountable odds. From the iconic wizardry of J.K. Rowlings "Harry Potter" series to the timeless allure of J.R.R. Tolkiens Middle-earth in "The Hobbit" and "The Lord of the Rings," fantasy books offer an escape into richly imagined worlds brimming with wonder, danger, and the promise of adventure at every turn. Whether delving into classic tales or discovering new realms crafted by contemporary authors, fantasy literature continues to captivate readers of all ages with its boundless creativity and enduring magic.','books': fantasy_books},
        'Historical': {'description': 'Historical books offer readers a captivating journey through the annals of time, immersing them in rich narratives that unfold against the backdrop of real-world events and settings from the past. These books serve as windows into bygone eras, shedding light on the triumphs, trials, and tribulations of humanity throughout history. Whether delving into the intricacies of ancient civilizations, exploring pivotal moments in world wars, or unraveling the complexities of cultural movements, historical books provide not only entertainment but also invaluable insights into the shaping of our modern world. Through meticulous research and vivid storytelling, authors of historical literature breathe life into characters and events from yesteryears, offering readers the opportunity to learn, reflect, and connect with the enduring legacies of the past.','books': historical_books},
        'SciFi': {'description': 'Science fiction, often abbreviated as scifi, encompasses a vast and imaginative realm of literature that explores speculative concepts rooted in scientific principles, futuristic technologies, and otherworldly settings. Within the scifi genre, readers embark on thrilling journeys across distant galaxies, encounter advanced civilizations, and grapple with the ethical dilemmas posed by artificial intelligence and space exploration. From epic space operas to mind-bending dystopian futures, scifi books captivate audiences with their visionary storytelling and thought-provoking narratives. These books challenge our perceptions of reality, pushing the boundaries of human imagination while offering compelling insights into the possibilities and pitfalls of our ever-evolving relationship with technology and the cosmos.','books': scifi_books},
        'Thriller': {'description': 'Thriller books captivate readers with their gripping narratives, intense suspense, and unexpected plot twists, keeping them on the edge of their seats from start to finish. In the realm of thrillers, readers delve into intricate webs of deception, unraveling dark secrets, and navigating through the minds of complex characters. These books often explore themes of mystery, crime, and psychological tension, drawing readers into heart-pounding scenarios where danger lurks around every corner. Whether its a psychological thriller that delves into the depths of the human psyche or a fast-paced action thriller filled with adrenaline-pumping sequences, thriller books offer an exhilarating reading experience that leaves readers eagerly turning pages to uncover the truth behind each thrilling mystery.','books': thriller_books}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['description'])
        for p in cat_data['books']:
            add_book(c, **p)


    for c in Category.objects.all():
        for p in Book.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_book(cat, title,description, url, author="", estimatedreadingtime=0,views=0,  *args, **kwargs,):
    p = Book.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.estimatedreadingtime = f"{estimatedreadingtime}"
    p.description = f"{description}"
    p.author = author
    p.views =views
    p.save()
    return p


def add_cat(name, description):
    c, created = Category.objects.get_or_create(name=name, defaults={'description': description})
    if not created:
        c.description = description
        c.save()
    return c



if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
