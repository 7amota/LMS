# Generated by Django 4.1.2 on 2022-11-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_book_rental_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rental_total',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
    ]
