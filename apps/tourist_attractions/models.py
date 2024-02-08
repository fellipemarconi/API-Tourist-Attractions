from django.db import models

# Create your models here.

class TouristSpot(models.Model):
    class Meta:
        verbose_name = 'Tourist Spot'
        verbose_name_plural = 'Tourist Spots'
        
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=4000)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name