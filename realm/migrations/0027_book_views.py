# Generated by Django 2.2.28 on 2024-03-18 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realm', '0026_rental_rental_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
