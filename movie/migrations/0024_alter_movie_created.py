# Generated by Django 4.0.4 on 2022-05-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0023_alter_movie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=2000),
        ),
    ]
