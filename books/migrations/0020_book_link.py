# Generated by Django 2.1.3 on 2018-11-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_delete_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='link',
            field=models.TextField(default=32),
            preserve_default=False,
        ),
    ]
