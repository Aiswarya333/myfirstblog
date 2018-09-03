from django.db import models

class Albums(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title +'-'+self.artist

class Songs(models.Model):
    album=models.ForeignKey(Albums,on_delete=models.CASCADE)
    songs_title=models.CharField(max_length=250)
    file_type=models.CharField(max_length=10)
