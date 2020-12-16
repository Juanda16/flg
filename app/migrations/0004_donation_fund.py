# Generated by Django 3.1.3 on 2020-12-10 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201121_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valueDonation', models.BigIntegerField(editable=False)),
                ('dateDonation', models.DateTimeField(auto_now_add=True)),
                ('statusTransactionState', models.BooleanField()),
                ('legalState', models.BooleanField()),
                ('donorId', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerFund', models.TextField(auto_created=True, max_length=10, unique=True)),
                ('valueFund', models.BigIntegerField(editable=False, null=True)),
            ],
        ),
    ]