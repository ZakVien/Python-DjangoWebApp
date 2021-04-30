# Generated by Django 3.1.6 on 2021-03-06 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0021_auto_20210306_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='expenses.parentcategory'),
            preserve_default=False,
        ),
    ]