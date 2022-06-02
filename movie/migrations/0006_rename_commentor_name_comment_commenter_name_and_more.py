# Generated by Django 4.0.4 on 2022-06-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentor_name',
            new_name='commenter_name',
        ),
        migrations.AlterField(
            model_name='movie',
            name='banner',
            field=models.ImageField(blank=True, upload_to='movies_banner'),
        ),
    ]