# Generated by Django 2.2.28 on 2024-03-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realm', '0020_remove_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilepicture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
