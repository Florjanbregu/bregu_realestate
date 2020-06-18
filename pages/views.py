from django.shortcuts import render
from django.http import HttpResponse
# import i pronave 
from listings.models import Listing
# import i agjenteve
from realtors.models import Realtor

# import Bedroom 
from listings.models import Bedroom

# import Bathroom
from listings.models import Bathroom

# import Action
from listings.models import Action

# import City
from listings.models import City

def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:9]

    # funksioni qe na mundeson marrjen e agjenteve nga tabela e agjenteve
    realtors = Realtor.objects.order_by('-hire_date')[:3]

    # extract data from table Bedrooms inside Listings 
    bedrooms = Bedroom.objects.order_by()

    # extract data from table Bathrooms inside Listings 
    bathrooms = Bathroom.objects.order_by()

    # extract data from table Actions inside Listings 
    actions = Action.objects.order_by()

    # extract data from table Cities inside Listings 
    cities = City.objects.order_by()


    context = {
        'listings': listings,
        'realtors': realtors,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'actions' : actions,
        'cities' : cities 
    }
    
    return render(request, 'pages/index.html', context)

def about(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    # funksioni qe na mundeson marrjen e agjenteve nga tabela e agjenteve
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    # krijimi i context i cili mbushet me te dhena nga database 
    context = {
        'listings': listings,
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)
