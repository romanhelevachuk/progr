from django.db import models



class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    duration = models.DurationField()
    genre = models.CharField(max_length=255) # Додано поле genre
    file = models.FileField(upload_to='songs/') # Додано поле file

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
