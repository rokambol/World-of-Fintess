from django.db import models

begginer = 'Begginer'
medium = 'Medium'
advance = 'Advance'

fitness_level = (
      (begginer, 'Begginer'),
      (medium, 'Medium'),
      (advance, 'Advance'),
        
    )

# Create your models here.
class payment(models.Model):
   height = models.DecimalField(decimal_places=2,max_digits=3, blank=False)
   weight = models.PositiveIntegerField(default=0, blank=False)
   age = models.PositiveIntegerField(default=0, blank=False)
   levels = models.CharField(max_length=30, choices=fitness_level, default=begginer)
      
      
 
   
   def __str__(self):
      return self.age
      
   
