# Generated by Django 2.2.28 on 2024-03-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realm', '0015_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='nouser', max_length=128),
        ),
    ]
