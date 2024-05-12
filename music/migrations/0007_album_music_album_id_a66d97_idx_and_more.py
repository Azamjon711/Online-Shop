# Generated by Django 5.0.4 on 2024-05-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_album_options_alter_artist_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='album',
            index=models.Index(fields=['id'], name='music_album_id_a66d97_idx'),
        ),
        migrations.AddIndex(
            model_name='artist',
            index=models.Index(fields=['id'], name='music_artis_id_a6462a_idx'),
        ),
        migrations.AddIndex(
            model_name='song',
            index=models.Index(fields=['id'], name='music_song_id_82e124_idx'),
        ),
    ]
