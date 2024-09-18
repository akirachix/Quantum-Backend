from django.db import models

class PhReading(models.Model):
    PH_TYPES = [
        ('acidic', 'Acidic (pH < 7)'),
        ('neutral', 'Neutral (pH = 7)'),
        ('alkaline', 'Alkaline (pH > 7)'),
    ]
    
    ph_value = models.FloatField()  # Store the pH as a float value
    farmer_id = models.IntegerField()
    ph_id = models.IntegerField()

    def ph_type(self):
        
        if self.ph_value < 7.0:
            return 'Acidic'
        elif self.ph_value == 7.0:
            return 'Neutral'
        else:
            return 'Alkaline'

    def __str__(self):
        return f"Farmer {self.farmer_id} - pH Value: {self.ph_value} ({self.ph_type()})"
