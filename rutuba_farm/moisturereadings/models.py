from django.db import models
class Moisturereadings(models.Model):
    sensor_id = models.IntegerField()
    farmer_id = models.IntegerField()
    moisture_readings = models.IntegerField()
    moisture_id = models.IntegerField()
    recommendation_id=models.IntegerField()
    def __str__(self):
        return f"{self.moisture_readings} {self.recommendation_id}"