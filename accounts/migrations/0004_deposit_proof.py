# Generated by Django 4.2.6 on 2024-07-21 01:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_ada_balance_profile_bnb_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='proof',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]