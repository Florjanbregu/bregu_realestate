from django.contrib import admin

# ktu bejme te mundur qe te shtojme listings nga admin area 
# importojme Listing sepse kur kemi krijuar models e kemi quajt Listing
# dhe cdo gje qe formohet tek models thirret tek admin.py 

from .models import Listing

# bedrooms
from .models import Bedroom

# bedrooms
from .models import Bathroom

# actions (for sale,booking etc)
from .models import Action

# Cities
from .models import City

# duhet te krijojme nje class listing admin qe duam te perdorim
# ne admin.py dhe do e kalojme ne admin.ModelAdmin

class ListingAdmin(admin.ModelAdmin):
    # ketu do te shtojme te gjithe variablat qe duhet te shfaqim kur hapim listings
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'city', 'realtor')

    # si te klikohet tek nje komponent
    # i tabeles per tu futur brend psh tek id ,titulli etj
    list_display_links = ('id', 'title')

    # si mund te behet is_published i klikueshem
    
    list_editable = ('is_published',)

    # si te bejme search me ane te disa fushave 
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode',  'price')

    # Si mund te filtrojme ne tabele
    list_filter = ('realtor',)

    # si te percaktojme sa recorde do permbaje nje faqe
    list_per_page = 25


 
# duhet qe te definojme te gjitha klasat qe krijohen
admin.site.register(Listing, ListingAdmin)

# Bedroom Table

class BedroomAdmin(admin.ModelAdmin):
    # ketu do te shtojme te gjithe variablat qe duhet te shfaqim kur hapim listings
    list_display = ('id', 'number_of_bedrooms')

    # si te klikohet tek nje komponent
    # i tabeles per tu futur brend psh tek id ,titulli etj
    list_display_links = ('id', 'number_of_bedrooms')

    # si te bejme search me ane te disa fushave 
    search_fields = ('id', 'number_of_bedrooms')
    
    # si te percaktojme sa recorde do permbaje nje faqe
    list_per_page = 25


# duhet qe te definojme te gjitha klasat qe krijohen
admin.site.register(Bedroom, BedroomAdmin)



# Bathroom Table

class BathroomAdmin(admin.ModelAdmin):
    # display data
    list_display = ('id', 'number_of_bathrooms')

    # make clicabile 
    list_display_links = ('id', 'number_of_bathrooms')

    # search from field  
    search_fields = ('id', 'number_of_bathrooms')
    
    # si te percaktojme sa recorde do permbaje nje faqe
    list_per_page = 25


# duhet qe te definojme te gjitha klasat qe krijohen
admin.site.register(Bathroom, BathroomAdmin)


# Action Table

class ActionAdmin(admin.ModelAdmin):
    # display data
    list_display = ('id', 'name_of_actions')

    # make clicabile 
    list_display_links = ('id', 'name_of_actions')

    # search from field  
    search_fields = ('id', 'name_of_actions')
    
    # si te percaktojme sa recorde do permbaje nje faqe
    list_per_page = 25


# duhet qe te definojme te gjitha klasat qe krijohen
admin.site.register(Action, ActionAdmin)



# City Table

class CityAdmin(admin.ModelAdmin):
    # display data
    list_display = ('id', 'name_of_cities')

    # make clicabile 
    list_display_links = ('id', 'name_of_cities')

    # search from field  
    search_fields = ('id', 'name_of_cities')
    
    # si te percaktojme sa recorde do permbaje nje faqe
    list_per_page = 25


# duhet qe te definojme te gjitha klasat qe krijohen
admin.site.register(City, CityAdmin)


