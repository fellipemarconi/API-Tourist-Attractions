from django.db import models
from ..attractions.models import Attraction
from ..comments_reviews.models import Comment
from ..address.models import Address
# Create your models here.

class TouristSpot(models.Model):
    class Meta:
        verbose_name = 'Tourist Spot'
        verbose_name_plural = 'Tourist Spots'
        
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=4000)
    is_approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction, default='')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True)
    cover = models.ImageField(upload_to='tourist-attractions/%Y/%m/', blank=True)
    
    def __str__(self):
        return self.name