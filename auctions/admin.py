from django.contrib import admin

# Register your models here.
from .models import AuctionsListing, User 

class AuctionsListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'inicial_bid', 'active')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email')

admin.site.register(AuctionsListing, AuctionsListingAdmin)
admin.site.register(User, UsersAdmin)