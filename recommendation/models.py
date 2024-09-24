
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save  
from farmer.models import Farmer
from sendsms.models import SensorData, generate_recommendation


class Recommendation(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True)
    recommendation_text = models.TextField(default='No recommendations for this value')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.recommendation_text


@receiver(post_save, sender=SensorData)
def create_recommendation_for_sensor_data(sender, instance, created, **kwargs):
    if created:
        recommendations = generate_recommendation(instance)
        for recommendation in recommendations:
            Recommendation.objects.create(farmer_id=instance.farmer_id, recommendation_text=recommendation)
