# Generated by Django 4.1.7 on 2023-02-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_cardetail_car_image'),
        ('Booknow', '0003_remove_book_status_alter_book_id_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.cardetail'),
        ),
    ]
