# Generated by Django 4.1.7 on 2023-03-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booknow', '0005_alter_book_user_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
