from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionsListing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=2000, blank=False, null=False)
    inicial_bid = models.FloatField()
    image_url = models.URLField()
    active = models.BooleanField()

    def __str__(self):
        return f"{self.title} {self.description} ${self.inical_bid} {self.active}"
class Bids():
    pass

class Comments():
    pass