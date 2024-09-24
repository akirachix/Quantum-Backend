from django.db import models


# Create your models here.
class Sensorreadings(models.Model):
    sensor_id = models.IntegerField()
    moisture_readings = models.IntegerField()
    npk_readings = models.IntegerField()
    ph_reading = models.IntegerField()
    farmer_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.sensor_id} {self.farmer_id} Active: {self.is_active}"
    
      