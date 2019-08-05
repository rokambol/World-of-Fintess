from django.db import models

# Create your models here.

class Fitness_Programs(models.Model):
    day1 = models.TextField(blank=True, default='')
    day2 = models.TextField(blank=True, default='')
    day3 = models.TextField(blank=True, default='')
    day4 = models.TextField(blank=True, default='')
    day5 = models.TextField(blank=True, default='')
    day6 = models.TextField(blank=True, default='')
    day7 = models.TextField(blank=True, default='')
    
    def __str__(self):
        return '%s %s' % (self.day1, self.day2)
    
    
