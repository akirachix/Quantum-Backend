from django.db import models

class PhReading(models.Model):
    PH_TYPES = [
        ('acidic', 'Acidic'),
        ('neutral', 'Neutral'),
        ('alkaline', 'Alkaline'),
    ]
    
    ph_value = models.DecimalField(max_digits=5, decimal_places=2, choices=PH_TYPES)
    farmer = models.ForeignKey('Farmer', on_delete=models.CASCADE)  # Replace 'Farmer' with the actual farmer model
    ph_sensor = models.ForeignKey('PhSensor', on_delete=models.CASCADE)  # Replace 'PhSensor' with the actual sensor model

    class Meta:
        verbose_name = "pH Reading"
        verbose_name_plural = "pH Readings"

    def __str__(self):
        return f"pH Reading {self.id}: {self.ph_value}"
