# Generated by Django 3.1.3 on 2020-12-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_donation_fund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='legalState',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]