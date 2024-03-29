# Generated by Django 2.2.28 on 2024-03-08 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realm', '0005_auto_20240307_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='No Desctiption Availible'),
        ),
    ]
