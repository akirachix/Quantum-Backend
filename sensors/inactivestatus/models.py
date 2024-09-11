from django.db import models

class Sensor(models.Model):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Sensor {self.id} - {'Active' if self.is_active else 'Inactive'}"
