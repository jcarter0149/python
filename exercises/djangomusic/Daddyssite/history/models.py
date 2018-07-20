from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    discover_name = models.DateTimeField('date published')


class Songs(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    song_length_secs = models.IntegerField(default=0)