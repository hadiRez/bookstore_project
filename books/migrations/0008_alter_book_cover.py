# Generated by Django 3.2.13 on 2022-07-08 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='covers/'),
        ),
    ]