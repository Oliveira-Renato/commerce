from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .models import User, AuctionsListing, Watchlist, Bids, Winner, Comments


def error_message(request,message):
    return render(request, "auctions/error_message.html", {
        "message": message
    })   
# just a comment
def index(request): 
    return render(request, "auctions/index.html", {
        "teste": AuctionsListing.objects.all()
    })

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image = request.POST["image"]
        user = request.user
        listing = AuctionsListing(title=title, description=description, inicial_bid=price, image_url=image, user=user, active=1)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_listing.html")

def listing(request, listing_id):
    if request.user.is_authenticated:
        winner = Winner.objects.filter(listing=listing_id)
        comments = Comments.objects.filter(listing=listing_id)
        if winner and str(winner[0].winner_user) == str(request.user):
            return render(request, "auctions/listing.html", {
                "listing": AuctionsListing.objects.get(id=listing_id),
                "message": "You are the winner!"
            })
        elif comments:
            return render(request, "auctions/listing.html", {
                "listing": AuctionsListing.objects.get(id=listing_id),
                "bids": Bids.objects.filter(listing=listing_id),
                "watchlist": Watchlist.objects.filter(user=request.user, listing=listing_id),
                "comments": comments
            })
        
        return render(request, "auctions/listing.html", {
            "listing": AuctionsListing.objects.get(id=listing_id),
            "watchlist": Watchlist.objects.filter(user=request.user, listing=listing_id),
            "bids": Bids.objects.filter(listing=listing_id)
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": AuctionsListing.objects.get(id=listing_id),
            "bids": Bids.objects.filter(listing=listing_id)
        })

def watchlist_view(request):
    if request.user.is_authenticated:   
        user = request.user 
        return render(request, "auctions/watchlist.html", {
        "watchlist": Watchlist.objects.filter(user=user)
        }) 
    else:
        return render(request, "auctions/watchlist.html")

def watchlist(request, listing_id, optional_parameter):
    if listing_id and optional_parameter == 0:
        user = request.user
        listing = AuctionsListing.objects.get(id=listing_id)
        watchlist = Watchlist(user=user, listing=listing)
        watchlist.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        user = request.user
        listing = AuctionsListing.objects.get(id=listing_id)
        watchlist = Watchlist.objects.get(user=user, listing=listing)
        watchlist.delete()
        return HttpResponseRedirect(reverse("watchlist_view"))

def bid(request, listing_id):
    if request.method == "POST":
        user = request.user
        listing = AuctionsListing.objects.get(id=listing_id)
        bid = request.POST["bid"]
        if float(bid) > float(listing.inicial_bid):
            bids = Bids.objects.filter(listing=listing_id)
            new_bid = Bids(user=user, listing=listing, bid=bid)

            if bids.count() == 0 or float(bid) > float(bids.last().bid):
                new_bid.save()
                return HttpResponseRedirect(reverse("listing", args=(listing_id,)))
            else:
                return HttpResponse(error_message(request, "The bid must be higher than the last bid"))
        else:
           return HttpResponse(error_message(request, "The bid must be higher than the last bid"))
    else:
        return render(request, "auctions/listing.html", {
            "listing": AuctionsListing.objects.get(id=listing_id)
        })

def close_listing(request, listing_id):
    if request.user == AuctionsListing.objects.get(id=listing_id).user:
        listing = AuctionsListing.objects.get(id=listing_id)
        higher_bid = Bids.objects.filter(listing=listing_id).last()

        if higher_bid:
            higher_bid_user = higher_bid.user
            winner = Winner(winner_user=higher_bid_user, listing=listing, winner_bid=higher_bid.bid)
            winner.save()
            listing.active = 0
            listing.save()

        return HttpResponseRedirect(reverse("index"))
        
def comments(request, listing_id):
    if request.method == "POST":
        user = request.user
        listing = AuctionsListing.objects.get(id=listing_id)
        comment = request.POST["comment"]
        comment = Comments(user=user, listing=listing, comment=comment)
        comment.save()
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))
    else:
        return render(request, "auctions/listing.html", {
            "listing": AuctionsListing.objects.get(id=listing_id),
            "comments": Comments.objects.filter(listing=listing_id)
        })
