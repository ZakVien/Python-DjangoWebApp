# Generated by Django 3.1.6 on 2021-03-06 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0013_auto_20210305_1910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExpenseList',
            new_name='Expense',
        ),
    ]
