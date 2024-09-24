from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Recommendation  
from sendsms.models import SensorData, generate_recommendation  

@receiver(post_save, sender=SensorData)
def create_recommendation_for_sensor_data(sender, instance, created, **kwargs):
    if created:
        recommendations = generate_recommendation(instance)
        for recommendation in recommendations:
            Recommendation.objects.create(farmer_id=instance.farmer_id, recommendation_text=recommendation)