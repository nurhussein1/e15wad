# Generated by Django 2.2.28 on 2024-03-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realm', '0006_auto_20240308_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', unique=True),
        ),
    ]