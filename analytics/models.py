from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class reading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)
    date = models.DateTimeField(default= timezone.now)
    temperature = models.DecimalField(decimal_places=2, default=8, max_digits=5)
    spo2 = models.DecimalField(decimal_places=2, default=8, max_digits=4)
