# Generated by Django 4.1.7 on 2023-02-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booknow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Id_Proof',
            field=models.ImageField(upload_to='car_image'),
        ),
    ]
