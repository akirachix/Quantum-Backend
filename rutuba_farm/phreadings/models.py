from django.db import models

# Create your models here.
class Phreadings(models.Model):
    farmer_id = models.IntegerField()
    sensor_id = models.IntegerField(default=0.0)
    ph_reading = models.IntegerField()
    reccomendation_id = models.IntegerField(default=0)
    ph_id = models.CharField(max_length=250)
    def __str__(self):
        return f"{self.sensor_id} {self.farmer_id}"