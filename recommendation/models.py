from django.db import models

class Recommendation(models.Model):
    farmer_id = models.ForeignKey('farmer.Farmer', on_delete=models.CASCADE, null=True)
    recommendation_content = models.TextField(default='No recommendations for this value')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recommendation_content