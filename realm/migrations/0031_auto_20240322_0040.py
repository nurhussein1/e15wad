# Generated by Django 2.2.28 on 2024-03-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realm', '0030_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='book',
            name='rent_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
