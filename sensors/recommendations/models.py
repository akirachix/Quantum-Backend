from django.db import models

class Recommendation(models.Model):
    content = models.TextField()
    farmer_id = models.IntegerField()
    sensor_id = models.IntegerField()
    recommendation_inactive = models.BooleanField(default=False)

    def __str__(self):
        return self.content
