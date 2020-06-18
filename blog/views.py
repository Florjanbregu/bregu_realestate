from django.shortcuts import render

# import i pronave 
from listings.models import Listing

# BLOG FUNCTION
def index(request):

    
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # funksioni qe na mundeson marrjen e agjenteve nga tabela e agjenteve
    context = {
        'listings': listings
    }

    return render(request, 'blog/blog.html', context)

