from django.db import models

# Create your models here.
class Farmer(models.Model):
    farmers_name = models.CharField(max_length= 100)
    farmer_location = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, unique=True)
    farmer_id = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.farmer_id}"