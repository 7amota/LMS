# Generated by Django 4.1.2 on 2022-11-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_alter_book_image_alter_book_image_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rental_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
