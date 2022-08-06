from django.urls import path

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

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
    path("error_message", views.error_message),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing"),
    path("comments/<int:listing_id>", views.comments, name="comments"),
    path("categories/<int:category_id>", views.categories, name="categories"),
    path("user-listing", views.winner, name="winner"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('auctions/images/favicon/android-chrome-192x192.png'))),
]
