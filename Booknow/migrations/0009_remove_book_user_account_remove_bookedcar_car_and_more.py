# Generated by Django 4.1.7 on 2023-03-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booknow', '0008_rename_purchaseditems_bookedcar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user_Account',
        ),
        migrations.RemoveField(
            model_name='bookedcar',
            name='car',
        ),
        migrations.AddField(
            model_name='bookedcar',
            name='TotalRent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
