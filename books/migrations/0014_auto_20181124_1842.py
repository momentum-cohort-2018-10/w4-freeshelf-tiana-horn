# Generated by Django 2.1.3 on 2018-11-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20181124_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(),
        ),
    ]