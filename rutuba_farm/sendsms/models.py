
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_sms
from farmer.models import Farmer
import logging
import pytz

logger = logging.getLogger(__name__)

class SensorData(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    ph_reading = models.FloatField()
    moisture_reading = models.FloatField()
    nutrients = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"pH: {self.ph_reading}, "
            f"Moisture: {self.moisture_reading}, "
            f"Nutrients: {self.nutrients}"
        )

def validate_phone_number(phone_number):
    return phone_number.startswith('0') and phone_number.isdigit() and len(phone_number) == 10

def send_sms_to_farmer(sensor_data):
    eat = pytz.timezone('Africa/Nairobi')
    
    formatted_timestamp = sensor_data.created_at.astimezone(eat).strftime('%Y-%m-%d %H:%M:%S')

    message = (
        f"New sensor data recorded:\n"
        f"pH Level: {sensor_data.ph_reading}\n"
        f"Moisture Level: {sensor_data.moisture_reading}\n"
        f"Nutrients: {sensor_data.nutrients}\n"
        f"Timestamp: {formatted_timestamp} EAT\n"
        f"Please water your plants, and ensure you use fertilizers rich in nitrogen and phosphorus!"
    )

    phone_number = sensor_data.farmer_id.phone_number  
    if validate_phone_number(phone_number):  
        send_sms(phone_number, message) 
        logger.info(f"SMS sent to {phone_number}")
    else:
        logger.error(f"Invalid phone number format: {phone_number}")

@receiver(post_save, sender=SensorData)
def send_sms_on_new_sensor_data(sender, instance, created, **kwargs):
    if created:
        send_sms_to_farmer(instance)
