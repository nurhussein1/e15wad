# Generated by Django 2.2.28 on 2024-03-08 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realm', '0013_auto_20240308_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='views',
        ),
    ]
