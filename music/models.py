from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    number_albums = models.PositiveIntegerField(default=0)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    count_songs = models.PositiveIntegerField(default=0)
    image = models.URLField()
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    listened = models.PositiveBigIntegerField(default=0)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.title





