# Generated by Django 3.1.6 on 2021-02-17 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20210216_1837'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
    ]
