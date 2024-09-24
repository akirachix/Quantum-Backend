from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Moisturereadings
class MoistureReadingsModelTest(TestCase):
    def test_create_moisture_reading(self):
        moisture_reading = Moisturereadings.objects.create(
            sensor_id=1,
            farmer_id=1,
            moisture_readings=50,
            moisture_id=1,
            recommendation_id=1
        )
        retrieved_reading = Moisturereadings.objects.get(id=moisture_reading.id)
        self.assertEqual(retrieved_reading.moisture_readings, 50)
        self.assertEqual(retrieved_reading.recommendation_id, 1)
    def test_str_method(self):
        moisture_reading = Moisturereadings(
            sensor_id=1,
            farmer_id=1,
            moisture_readings=50,
            moisture_id=1,
            recommendation_id=1
        )
        moisture_reading.save()
        result = str(moisture_reading)
        self.assertEqual(result, "50 1")
    def test_invalid_moisture_reading_negative_value(self):
        moisture_reading = Moisturereadings(
            sensor_id=1,
            farmer_id=1,
            moisture_readings=-10,
            moisture_id=1,
            recommendation_id=1
        )
    def test_missing_fields(self):
        moisture_reading = Moisturereadings(
            sensor_id=None,
            farmer_id=1,
            moisture_readings=50,
            moisture_id=1,
            recommendation_id=1
        )
        moisture_reading = Moisturereadings(
            sensor_id=1,
            farmer_id=None,
            moisture_readings=50,
            moisture_id=1,
            recommendation_id=1
        )
