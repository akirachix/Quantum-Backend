from django.test import TestCase

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from .models import Sensor

class SensorModelTests(TestCase):
    def test_create_sensor_default_active(self):
        sensor = Sensor.objects.create()
        self.assertTrue(sensor.is_active)
        self.assertEqual(str(sensor), f"Sensor {sensor.id} - Active")

    def test_create_sensor_inactive(self):
        sensor = Sensor.objects.create(is_active=False)
        self.assertFalse(sensor.is_active)
        self.assertEqual(str(sensor), f"Sensor {sensor.id} - Inactive")

    def test_update_sensor_status(self):
        sensor = Sensor.objects.create()
        sensor.is_active = False
        sensor.save()
        self.assertFalse(Sensor.objects.get(id=sensor.id).is_active)

    def test_create_multiple_sensors(self):
        Sensor.objects.create()
        Sensor.objects.create(is_active=False)
        self.assertEqual(Sensor.objects.count(), 2)

    # Unhappy path tests

    def test_create_sensor_invalid_active_status(self):
        with self.assertRaises(ValidationError):
            sensor = Sensor(is_active="Not a boolean")
            sensor.full_clean()

    def test_update_sensor_invalid_active_status(self):
        sensor = Sensor.objects.create()
        with self.assertRaises(ValidationError):
            sensor.is_active = "Not a boolean"
            sensor.full_clean()

   

    def test_delete_nonexistent_sensor(self):
        
        with self.assertRaises(Sensor.DoesNotExist):
            non_existent_sensor = Sensor.objects.get(id=999)
            non_existent_sensor.delete()

    def test_str_method_with_none_id(self):
        sensor = Sensor(is_active=True)
        self.assertEqual(str(sensor), "Sensor None - Active")

    def test_bulk_create_sensors(self):
        sensors = [Sensor(is_active=i % 2 == 0) for i in range(10)]
        Sensor.objects.bulk_create(sensors)
        self.assertEqual(Sensor.objects.count(), 10)
        self.assertEqual(Sensor.objects.filter(is_active=True).count(), 5)
        self.assertEqual(Sensor.objects.filter(is_active=False).count(), 5)


