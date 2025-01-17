
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CropHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    N = models.FloatField()
    P = models.FloatField()
    K = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    recommended_crop = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.recommended_crop} on {self.timestamp}"

