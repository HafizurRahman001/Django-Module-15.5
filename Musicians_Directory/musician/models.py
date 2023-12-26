from django.db import models

# Create your models here.
class AddMusician(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    INSTRUMENTS = [
        ('guitar','Guitar'),
        ('Flute','Flute'),
        ('Tobla','Tobla'),
        ('Dhol','Dhol'),
    ]
    instrument_type = models.CharField(max_length=20, choices=INSTRUMENTS)



    def __str__(self):
        return f"{self.first_name}"
