from django.db import models

# Create your models here.
class Sendsms(models.Model):
    sender_id = models.IntegerField(primary_key=True)
    recipient = models.CharField(max_length=20)
    farmer_id = models.IntegerField()
    sensor_id = models.IntegerField(default=0)
    message=models.CharField(max_length=250)
    
   
    
    def __str__(self):
        return f"{self.message} {self.sender_id}"

