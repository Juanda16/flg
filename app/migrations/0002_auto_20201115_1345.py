# Generated by Django 3.1.3 on 2020-11-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='documentType',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]