# Generated by Django 4.0.5 on 2022-06-05 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_alter_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
