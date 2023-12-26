from django.db import models
from musician.models import AddMusician

# Create your models here.
class AddAlbum(models.Model):
    album_name = models.CharField(max_length = 100)
    album_reels_date = models.DateField()
    musician_name = models.ForeignKey(AddMusician, on_delete=models.CASCADE, default=None)
    RATINGS=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    ratings = models.CharField(max_length=1,choices=RATINGS)


    def __str__(self):
        return f"{self.album_name}"
