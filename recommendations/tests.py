from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Recommendation

class RecommendationModelTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'content': 'Test recommendation',
            'farmer_id': 1,
            'sensor_id': 1,
        }

    def test_create_valid_recommendation(self):
        recommendation = Recommendation.objects.create(**self.valid_data)
        self.assertEqual(str(recommendation), 'Test recommendation')
        self.assertFalse(recommendation.recommendation_inactive)

    def test_create_recommendation_empty_content(self):
        data = self.valid_data.copy()
        data['content'] = ''
        recommendation = Recommendation.objects.create(**data)
        self.assertEqual(recommendation.content, '')  

    def test_create_recommendation_null_content(self):
        data = self.valid_data.copy()
        data['content'] = None
        with self.assertRaises(ValidationError):
            recommendation = Recommendation(**data)
            recommendation.full_clean()  

    def test_create_recommendation_negative_farmer_id(self):
        data = self.valid_data.copy()
        data['farmer_id'] = -1
        recommendation = Recommendation.objects.create(**data)
        self.assertEqual(recommendation.farmer_id, -1)  

    def test_create_recommendation_negative_sensor_id(self):
        data = self.valid_data.copy()
        data['sensor_id'] = -1
        recommendation = Recommendation.objects.create(**data)
        self.assertEqual(recommendation.sensor_id, -1)  

    def test_create_recommendation_non_boolean_inactive(self):
        data = self.valid_data.copy()
        data['recommendation_inactive'] = 'not a boolean'
        with self.assertRaises(ValidationError):
            recommendation = Recommendation(**data)
            recommendation.full_clean() 

    def test_update_recommendation_to_invalid_content(self):
        recommendation = Recommendation.objects.create(**self.valid_data)
        recommendation.content = None
        with self.assertRaises(ValidationError):
            recommendation.full_clean()  

    def test_str_method_with_long_content(self):
        long_content = 'a' * 1000 
        data = self.valid_data.copy()
        data['content'] = long_content
        recommendation = Recommendation.objects.create(**data)
        self.assertEqual(str(recommendation), long_content)  

    def test_create_recommendation_with_max_integer_ids(self):
        data = self.valid_data.copy()
        data['farmer_id'] = 2**31 - 1  
        data['sensor_id'] = 2**31 - 1
        recommendation = Recommendation.objects.create(**data)
        self.assertEqual(recommendation.farmer_id, 2**31 - 1)
        self.assertEqual(recommendation.sensor_id, 2**31 - 1)

    def test_filter_inactive_recommendations(self):
        Recommendation.objects.create(**self.valid_data)
        Recommendation.objects.create(content='Inactive', farmer_id=2, sensor_id=2, recommendation_inactive=True)
        inactive_count = Recommendation.objects.filter(recommendation_inactive=True).count()
        self.assertEqual(inactive_count, 1)


