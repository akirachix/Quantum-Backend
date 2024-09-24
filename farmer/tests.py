from django.test import TestCase
from django.test import TestCase
from .models import Farmer
from django.core.exceptions import ValidationError

class FarmerModelTests(TestCase):

    def test_farmer_creation_without_required_fields(self):
        
        with self.assertRaises(ValidationError):
            farmer = Farmer(farmers_name="", farmer_location="Farm Location")
            farmer.full_clean()  

    def test_farmer_creation_with_duplicate_phone_number(self):

        Farmer.objects.create(
            farmers_name="John Doe",
            farmer_location="Farm A",
            phone_number="1234567890",
            farmer_id=1,
            sensor_id=1
        )
        
        
        farmer = Farmer(
            farmers_name="Jane Smith",
            farmer_location="Farm B",
            phone_number="1234567890",  
            farmer_id=2,
            sensor_id=2
        )
        
       

    def test_farmer_creation_with_invalid_sensor_id(self):
        
        farmer = Farmer(
            farmers_name="Alice",
            farmer_location="Farm C",
            phone_number="0987654321",
            farmer_id=3,
            sensor_id=-1  
        )
       

    def test_farmer_creation_without_phone_number(self):
    
        farmer = Farmer(
            farmers_name="Bob",
            farmer_location="Farm D",
            farmer_id=4,
            sensor_id=3
        )
        
      

    def test_farmer_creation_with_too_long_name(self):
    
        farmer = Farmer(
            farmers_name="A" * 101,  
            farmer_location="Farm E",
            phone_number="1234567891",
            farmer_id=5,
            sensor_id=4
        )
        
  
