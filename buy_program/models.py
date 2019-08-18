from django.db import models

begginer = 'Begginer'
medium = 'Medium'
advance = 'Advance'

fitness_level = (
      (begginer, 'Begginer'),
      (medium, 'Medium'),
      (advance, 'Advance'),
        
    )

#Create your models here.
class Details(models.Model):
    height = models.CharField(max_length=3, default='')
    weight = models.CharField(max_length=3, default='')
    age = models.CharField(max_length=3, default='')
    levels = models.CharField(max_length=30, choices=fitness_level, default='')
      
      
      
    def __str__(self):
        return '%s %s %s %s' % (self.height, self.weight, self.age, self.level) 