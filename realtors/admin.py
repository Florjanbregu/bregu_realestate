from django.contrib import admin

# ktu bejme te mundur qe te shtojme listings nga admin area 
# importojme Realtor sepse kur kemi krijuar models e kemi quajt Realtor
# dhe cdo gje qe formohet tek models thirret tek admin.py 

from .models import Realtor

# Duhet te krijojme class e cila do te marr si parameter 
# admin.ModelAdmin

class RealtorAdmin(admin.ModelAdmin):
    # duhet te deklarojme variablat qe do shfaqen
    list_display = ('id', 'name', 'email', 'hire_date')

    # fushat e klikueshme
    list_display_links = ('id', 'name', 'email', 'hire_date')
     
    # fushat qe mund te bejme search
    search_fields = ('id', 'name', 'email', 'hire_date')

    # numri i rekordeve per faqe
    list_per_page = 25


# duhet te kalojme parametrin e 2 i cili eshte RealtorAdmin
admin.site.register(Realtor, RealtorAdmin)
