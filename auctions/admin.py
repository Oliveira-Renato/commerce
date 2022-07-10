from django.contrib import admin

# Register your models here.
from .models import AuctionsListing 

class AuctionsListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'inicial_bid', 'active')

admin.site.register(AuctionsListing, AuctionsListingAdmin)