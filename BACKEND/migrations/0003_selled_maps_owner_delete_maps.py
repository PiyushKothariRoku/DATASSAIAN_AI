# Generated by Django 5.0.6 on 2024-11-27 06:41

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BACKEND', '0002_maps_registered_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='selled_maps_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('Registered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('maps_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('maps_length', models.IntegerField()),
                ('maps_width', models.IntegerField()),
                ('land_address', models.CharField(max_length=200)),
                ('owner_address', models.CharField(max_length=200)),
                ('owner_pan', models.CharField(max_length=10)),
                ('owner_Addhar', models.CharField(max_length=10)),
                ('Token_money', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Maps',
        ),
    ]
