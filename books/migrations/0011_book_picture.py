# Generated by Django 2.1.3 on 2018-11-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20181124_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(null=True, upload_to='books/'),
        ),
    ]
