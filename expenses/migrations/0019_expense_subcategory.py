# Generated by Django 3.1.6 on 2021-03-06 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0018_auto_20210306_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='expenses.subcategory'),
            preserve_default=False,
        ),
    ]
