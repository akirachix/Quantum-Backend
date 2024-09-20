from django.db import models
from recommendations.models import Recommendations


# Create your models here.
class NpkReading(models.Model):
    id = models.AutoField(primary_key=True)  
    farmer_id = models.IntegerField()        
    sensor_id = models.IntegerField()
    npk_reading = models.IntegerField()     
    recommendation_id = models.ForeignKey(Recommendations, on_delete=models.CASCADE,related_name='NpkReading' )
    
    def __str__(self):
        return f"NpkReading {self.id}: Farmer {self.farmer_id}, Sensor {self.sensor_id}, Reading {self.npk_reading}"