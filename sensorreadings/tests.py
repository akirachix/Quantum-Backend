from django.test import TestCase
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Sensorreadings
class SensorreadingsModelTest(TestCase):
    def test_missing_sensor_id(self):
        sensor_reading = Sensorreadings(
            sensor_id=None,
            moisture_readings=30,
            npk_readings=10,
            ph_reading=6,
            farmer_id=1
        )
    def test_negative_moisture_readings(self):
        sensor_reading = Sensorreadings(
            sensor_id=1,
            moisture_readings=-10,
            npk_readings=10,
            ph_reading=6,
            farmer_id=1
        )
    def test_invalid_npk_readings(self):
        sensor_reading = Sensorreadings(
            sensor_id=1,
            moisture_readings=30,
            npk_readings=None,
            ph_reading=6,
            farmer_id=1
        )
    def test_missing_farm_id(self):
        sensor_reading = Sensorreadings(
            sensor_id=1,
            moisture_readings=30,
            npk_readings=10,
            ph_reading=6,
            farmer_id=None
        )
    def test_invalid_ph_reading(self):
        sensor_reading = Sensorreadings(
            sensor_id=1,
            moisture_readings=30,
            npk_readings=10,
            ph_reading=-1,
            farmer_id=1
        )
