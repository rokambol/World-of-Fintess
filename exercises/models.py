from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField
    image = models.ImageField(upload_to='images', default='')
    
    def __self__(self):
        return self.name
