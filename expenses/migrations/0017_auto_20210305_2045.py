# Generated by Django 3.1.6 on 2021-03-06 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0016_auto_20210305_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='expenses.category'),
            preserve_default=False,
        ),
    ]