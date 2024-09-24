from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import PhReading

class PhReadingModelTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'ph_value': 7.0,
            'farmer_id': 1,
            'ph_id': 1,
        }

    def test_create_valid_ph_reading(self):
        reading = PhReading.objects.create(**self.valid_data)
        self.assertEqual(str(reading), "Farmer 1 - pH Value: 7.0 (Neutral)")

    def test_create_ph_reading_negative_ph(self):
        data = self.valid_data.copy()
        data['ph_value'] = -1.0
        reading = PhReading.objects.create(**data)
        self.assertEqual(reading.ph_type(), 'Acidic')

    def test_create_ph_reading_extremely_high_ph(self):
        data = self.valid_data.copy()
        data['ph_value'] = 15.0
        reading = PhReading.objects.create(**data)
        self.assertEqual(reading.ph_type(), 'Alkaline')

    def test_create_ph_reading_string_ph_value(self):
        data = self.valid_data.copy()
        data['ph_value'] = 'not a number'
        with self.assertRaises(ValueError):
            PhReading.objects.create(**data)

    def test_create_ph_reading_negative_farmer_id(self):
        data = self.valid_data.copy()
        data['farmer_id'] = -1
        reading = PhReading.objects.create(**data)
        self.assertEqual(reading.farmer_id, -1)

    def test_create_ph_reading_negative_ph_id(self):
        data = self.valid_data.copy()
        data['ph_id'] = -1
        reading = PhReading.objects.create(**data)
        self.assertEqual(reading.ph_id, -1)

    def test_ph_type_edge_cases(self):
        reading = PhReading.objects.create(**self.valid_data)
        
        reading.ph_value = 6.99999999
        self.assertEqual(reading.ph_type(), 'Acidic')
        
        reading.ph_value = 7.00000001
        self.assertEqual(reading.ph_type(), 'Alkaline')

    def test_str_method_with_long_ph_value(self):
        data = self.valid_data.copy()
        data['ph_value'] = 7.1234567890123456
        reading = PhReading.objects.create(**data)
        expected_str = f"Farmer 1 - pH Value: {data['ph_value']} (Alkaline)"
        self.assertEqual(str(reading), expected_str)

    def test_create_ph_reading_max_integer_ids(self):
        data = self.valid_data.copy()
        data['farmer_id'] = 2**31 - 1  
        data['ph_id'] = 2**31 - 1
        reading = PhReading.objects.create(**data)
        self.assertEqual(reading.farmer_id, 2**31 - 1)
        self.assertEqual(reading.ph_id, 2**31 - 1)

    def test_filter_by_ph_type(self):
        PhReading.objects.create(ph_value=6.5, farmer_id=1, ph_id=1)
        PhReading.objects.create(ph_value=7.0, farmer_id=2, ph_id=2)
        PhReading.objects.create(ph_value=7.5, farmer_id=3, ph_id=3)
        
        acidic_count = PhReading.objects.filter(ph_value__lt=7.0).count()
        neutral_count = PhReading.objects.filter(ph_value=7.0).count()
        alkaline_count = PhReading.objects.filter(ph_value__gt=7.0).count()
        
        self.assertEqual(acidic_count, 1)
        self.assertEqual(neutral_count, 1)
        self.assertEqual(alkaline_count, 1)