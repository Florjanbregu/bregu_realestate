from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 

from django.http import HttpResponse

# Listing model
from .models import Listing

# Realtors Model
from realtors.models import Realtor

# import Bedroom Model
from listings.models import Bedroom

# import Bathroom Model
from listings.models import Bathroom

# import Action Model
from listings.models import Action

# import City Model
from listings.models import City


from django.shortcuts import render

# LISTINGS FUNCTION
def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # dmth behet order by + publikohen vetem ato qr kane flag
    

    paginator = Paginator(listings, 3)
    # krijimi i nje variabli page i = request.get.get dhe kalimi i parametrit page per te cilin jemi duke kerkuar
    # psh page=1 nese kalojme tek tjetra shkon 2 e kshu me radhe
    page = request.GET.get('page') 
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)
  
# SINGLE LISTING FUNCTION 
def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)
    # krijimi i context i cili mbushet me te dhena nga database 

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context) 

# SEARCH FUNCTION
def search(request):
    # per secilen fushe do te na duhet te krijojme query per te kerkuar
    # query qe ben order by të pronave për datë
    queryset_list = Listing.objects.order_by('-list_date') 

    # Listings Table 
    listing1 = Listing.objects.order_by('-list_date')

    # Table Bedrooms inside listings
    bedrooms = Bedroom.objects.order_by()

    # Table Bedrooms inside listings
    bathrooms = Bathroom.objects.order_by()

    # Table Actions inside listings
    actions = Action.objects.order_by()

    # Table Cities inside listings
    cities = City.objects.order_by()

    # shtimi i filtrave per kampin fjale kyce(keywords)
    # kontrollojme ne fillim nese ekziston
    # | = OR conditions
    # , = AND conditions duhet perdor brenda kllapave
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)  | queryset_list.filter(title__icontains=keywords) | queryset_list.filter(address__icontains=keywords) | queryset_list.filter(city__icontains=keywords) #mqs mund te kerkojme dhe me nje fjale 

    
    # shtimi i filtrave per kampin dhomave(bedrooms)
    # kontrollojme ne fillim nese ekziston
    if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms'] # krijimi i variablit bedrooms
      if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # ben te mundur gjetjen e dhomave te = ose me te vogla se nr i zgjedhur


    # shtimi i filtrave per kampin banjove(bathrooms)
    # kontrollojme ne fillim nese ekziston
    if 'bathrooms' in request.GET:
      bathrooms = request.GET['bathrooms'] # krijimi i variablit bathrooms
      if bathrooms:
        queryset_list = queryset_list.filter(bathrooms__lte=bathrooms) # ben te mundur gjetjen e banjove te = ose me te vogla se nr i zgjedhur
       
    
    # shtimi i filtrave per kampin pronave(listings)
    # kontrollojme ne fillim nese ekziston
    if 'listing1' in request.GET:
      listing1 = request.GET['listing1'] # krijimi i variablit listings
      if listing1:
        queryset_list = queryset_list.filter(title__iexact=listing1)


    
    # shtimi i filtrave per kampin actions
    # kontrollojme ne fillim nese ekziston
    if 'actions' in request.GET:
      actions = request.GET['actions'] # krijimi i variablit actions
      if actions:
        queryset_list = queryset_list.filter(actions__iexact=actions)
    
    # shtimi i filtrave per kampin cities
    # kontrollojme ne fillim nese ekziston
    if 'cities' in request.GET:
      cities = request.GET['cities'] # krijimi i variablit actions
      if cities:
        queryset_list = queryset_list.filter(city__iexact=cities)



    context = {
    'listings': queryset_list,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'listing1': listing1,
    'actions' : actions,
    'cities' : cities,
    'values': request.GET
    }

    
    return render(request, 'listings/search.html', context) 