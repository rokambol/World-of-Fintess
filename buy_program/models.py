from django.db import models

# Create your models here.
class buy_program(models.Model):
   height = models.DecimalField(decimal_places=2,max_digits=3, blank=False)
   weight = models.IntegerField(max_digits=3, blank=False)
   age = models.IntegerField(max_digits=2, blank=False)
   
   def __str__(self):
      return self.age
      
   
