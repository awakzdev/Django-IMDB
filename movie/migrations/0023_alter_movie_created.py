# Generated by Django 4.0.4 on 2022-05-28 16:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0022_alter_movie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 16, 39, 13, 317752, tzinfo=utc)),
        ),
    ]
