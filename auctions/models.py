from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.username}"
class AuctionsListing(models.Model):   
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None,related_name='auctions')
    title = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=2000, blank=False, 
    null=False)
    inicial_bid = models.FloatField()
    image_url = models.URLField(max_length=6000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None,related_name='categories', blank=True, null=True)
    active = models.BooleanField()

    def __str__(self):
        return f"title:{self.title} desc:{self.description} ${self.inicial_bid} img:{self.image_url} active:{self.active}"

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    auction = models.ManyToManyField(AuctionsListing,default=None,related_name='categories')
    name = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"
class Bids():
    pass

class Comments():
    pass


