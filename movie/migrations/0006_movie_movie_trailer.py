# Generated by Django 4.0.4 on 2022-05-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
