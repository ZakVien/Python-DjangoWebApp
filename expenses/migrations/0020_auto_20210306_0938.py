# Generated by Django 3.1.6 on 2021-03-06 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0019_expense_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.subcategory', verbose_name='subcategories'),
        ),
    ]
