from django.db import models
from django.contrib.auth.models import User



#Create your models here.
class Details(models.Model):
    height = models.CharField(max_length=3, default='')
    weight = models.CharField(max_length=3, default='')
    age = models.CharField(max_length=3, default='')
    level = models.CharField(max_length=30, default='')
    user = models.ForeignKey(User, blank=True, null=True) 
    
    def __str__(self):
        return '%s %s %s %s' % (self.height, self.weight, self.age, self.level) 