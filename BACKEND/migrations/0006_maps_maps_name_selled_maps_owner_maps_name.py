# Generated by Django 5.0.6 on 2024-11-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BACKEND', '0005_owner_seller_remove_selled_maps_owner_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maps',
            name='maps_name',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='selled_maps_owner',
            name='maps_name',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
