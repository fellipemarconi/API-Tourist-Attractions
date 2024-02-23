from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    review = models.DecimalField(max_digits=3, decimal_places=2)

    
    def __str__(self) -> str:
        return self.user.first_name
    