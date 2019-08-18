from django.db import models
from django.contrib.auth.models import User

# Create your models here 


class FitnessUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='swimmer')
    
    def __str__(self):
        return self.user.username