from django.test import TestCase
from .models import Recommendation
from django.core.exceptions import ValidationError

class RecommendationTestCase(TestCase):

    def test_create_recommendation_without_content(self):
    
        recommendation = Recommendation(recommendation_content="")
        try:
            recommendation.full_clean()  
        except ValidationError:
            pass  

    def test_create_recommendation_with_exceeding_length(self):
        
        long_content = "x" * 251  
        recommendation = Recommendation(recommendation_content=long_content)
        try:
            recommendation.full_clean()  
        except ValidationError:
            pass  

    def test_create_recommendation_with_invalid_data_type(self):
        
        try:
            Recommendation.objects.create(recommendation_content=12345)  
        except (TypeError, ValidationError):
            pass  

    def test_create_recommendation_without_providing_content(self):
    
        try:
            Recommendation.objects.create()
        except ValidationError:
            pass  


