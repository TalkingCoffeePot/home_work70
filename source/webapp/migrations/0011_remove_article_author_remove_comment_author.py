# Generated by Django 4.2.7 on 2023-12-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alter_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]