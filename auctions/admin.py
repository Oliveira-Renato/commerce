from django.contrib import admin

# Register your models here.
from .models import AuctionsListing, User, Category, Watchlist, Bids, Winner 


class WinnerAdmin(admin.ModelAdmin):
    list_display = ('winner_user', 'listing', 'winner_bid', 'date')
    list_filter = ('winner_user', 'listing', 'winner_bid', 'date')
    search_fields = ('winner_user', 'listing', 'winner_bid', 'date')
    ordering = ('winner_user', 'listing', 'winner_bid', 'date')
    date_hierarchy = 'date'


class BidsAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing', 'bid')
    list_filter = ('user', 'listing', 'bid')
    search_fields = ('user', 'listing', 'bid')
    

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'listing')
    list_filter = ('user', 'listing')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class AuctionsListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'inicial_bid', 'active')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(AuctionsListing, AuctionsListingAdmin)
admin.site.register(User, UsersAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(Winner, WinnerAdmin)