# Generated by Django 2.1.3 on 2018-11-25 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_book_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Your name')),
                ('book_suggestion', models.CharField(max_length=255, verbose_name='Name of Book')),
                ('link_to_book', models.CharField(max_length=255)),
            ],
        ),
    ]
