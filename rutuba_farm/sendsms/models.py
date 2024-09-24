
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
    nutrients = models.IntegerField()
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
        f"Recommendations: {generate_recommendation(sensor_data)}"
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


def generate_recommendation(sensor_data):
    recommendations = []


    if sensor_data.ph_reading < 4.5:
        recommendations.append("Add lime. Plant only tough crops.")
    elif 4.5 <= sensor_data.ph_reading < 5.5:
        recommendations.append("Add lime. Plant crops like potatoes.")
    elif 5.6 <= sensor_data.ph_reading < 6.5:
        recommendations.append("Add a little lime if needed for your crops.")
    elif 6.6 <= sensor_data.ph_reading < 7.2:
        recommendations.append("Perfect for most crops. No need to change.")
    elif 7.3 <= sensor_data.ph_reading < 8.0:
        recommendations.append("Apply sulfur or acidifying fertilizers to lower pH if growing acid-loving plants.")
    elif sensor_data.ph_reading >= 8.0:
        recommendations.append("Apply sulfur or acidifying fertilizers to lower pH. Grow plants tolerant of alkaline soils.")

    if sensor_data.moisture_reading < 10:
        recommendations.append("Your soil is very dry. Water your crops immediately to prevent them from drying out.")
    elif 10 <= sensor_data.moisture_reading < 20:
        recommendations.append("The soil is dry, and your plants may start wilting. It's a good time to water them.")
    elif 20 <= sensor_data.moisture_reading < 30:
        recommendations.append("The soil is a bit dry. Water your crops soon to keep them healthy.")
    elif 30 <= sensor_data.moisture_reading < 40:
        recommendations.append("Your soil has the perfect amount of moisture. Keep up the good work and water as usual.")
    elif 40 <= sensor_data.moisture_reading < 50:
        recommendations.append("The soil is nicely moist. Keep an eye on it and avoid watering too much.")
    elif 50 <= sensor_data.moisture_reading < 70:
        recommendations.append("The soil is already wet. Cut back on watering to avoid problems.")
    elif 70 <= sensor_data.moisture_reading < 80:
        recommendations.append("The soil has too much water. Let it dry out before watering again.")
    elif 80 <= sensor_data.moisture_reading <= 100:
        recommendations.append("There is too much water in the soil. Stop watering until it dries out a bit.")


    if sensor_data.nutrients < 20:
        recommendations.append("Nutrient levels are very low. Apply nitrogen-rich fertilizers immediately.")
    elif 20 <= sensor_data.nutrients < 40:
        recommendations.append("Nutrient levels are low. Consider applying nitrogen-rich fertilizers.")
    elif 40 <= sensor_data.nutrients < 60:
        recommendations.append("Nutrient levels are adequate. Maintain your current fertilization schedule.")
    elif 60 <= sensor_data.nutrients < 80:
        recommendations.append("Nutrient levels are high. Monitor closely to avoid over-fertilization.")
    elif sensor_data.nutrients >= 80:
        recommendations.append("Nutrient levels are very high. Reduce fertilization to prevent nutrient burn.")    

    return " ".join(recommendations)
