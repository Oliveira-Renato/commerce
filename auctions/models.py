from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionsListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=2000)
    inical_bid = models.FloatField()
    image_url = models.URLField()
    active = models.BooleanField()
    
    def __str__(self):
        return f"{self.title} {self.description} ${self.inical_bid} {self.active}"
class Bids():
    pass

class Comments():
    pass