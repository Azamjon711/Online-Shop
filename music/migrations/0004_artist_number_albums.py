# Generated by Django 5.0.4 on 2024-05-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_count_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='number_albums',
            field=models.PositiveIntegerField(default=0),
        ),
    ]