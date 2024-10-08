# Generated by Django 4.2.6 on 2024-07-21 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ada_balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bnb_balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='doge_balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='sol_balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='usdc_balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='xlm_balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='xrp_balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
