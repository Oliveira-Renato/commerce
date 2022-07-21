from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create-listing", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("my-watchlist", views.watchlist_view, name="watchlist_view"),
    path("watchlist/<int:listing_id>/<int:optional_parameter>", views.watchlist, name="watchlist"),
    path("bids/<int:listing_id>", views.bid, name="bid"),
    path("error_message", views.error_message)
    
]
