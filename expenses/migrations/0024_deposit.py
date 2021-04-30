# Generated by Django 3.1.6 on 2021-03-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0023_auto_20210306_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Deposit Date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]