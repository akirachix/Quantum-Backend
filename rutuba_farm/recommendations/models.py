from django.db import models



class Recommendations(models.Model):
    id = models.AutoField(primary_key=True)
    recommendations_content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    def __str__(self):
        return self.recommendations_content  

