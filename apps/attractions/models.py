from django.db import models

# Create your models here.
class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    work_time = models.TextField()
    minimal_age = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name