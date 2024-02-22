from django.db import models

# Create your models here.
class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    work_time = models.TextField()
    minimal_age = models.IntegerField()
    cover = models.ImageField(upload_to='tourist-attractions/attractions/%Y/%m/', null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.name