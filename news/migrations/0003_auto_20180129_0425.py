# Generated by Django 2.0.1 on 2018-01-29 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='tags',
            new_name='tag',
        ),
    ]
