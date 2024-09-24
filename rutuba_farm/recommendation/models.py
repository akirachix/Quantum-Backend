from django.db import models

# Create your models here.

class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    recommendation_content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    def __str__(self):
        return self.recommendation_content  