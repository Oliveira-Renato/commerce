from django.contrib import admin

# Register your models here.
from .models import AuctionsListing, User, Category, Watchlist, Bids 

class BidsAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing', 'bid')

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'listing')
    list_filter = ('user', 'listing')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class AuctionsListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'inicial_bid', 'active')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(AuctionsListing, AuctionsListingAdmin)
admin.site.register(User, UsersAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Bids, BidsAdmin)