from django.db import models

class House(models.Model):

    """Model Definition for House"""
    
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length = 140)
    pet_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.name