from django.db import models
from datetime import datetime
from realtors.models import Realtor 


# Actions table (example: sales,rent...)
class Action(models.Model):
    name_of_actions = models.TextField(blank=False)
    def __str__(self):
        return str(self.name_of_actions)


class Listing(models.Model):
    # realtor eshte nje foreign Key i nje tabele tjeter qe eshte realtor
    # dhe per kete arsye eshte pak me i veshtire per tu deklaruar
    action = models.ForeignKey(Action, on_delete=models.DO_NOTHING)
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)  
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    # Mqs pershkrimi eshte i gjate perdoret textfield dhe blank=true do te thote
    # qe eshte opsionale
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    # bathrooms mund te jete dhe me presje dhe max_digits=2 do te thote
    # qe max ka 2 shifra dhe decimal_places = 1 do te thote qe ka 1 shifer pas presjes
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    # fotot ne django shkojne tek media folder 
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

# Bedrooms table
class Bedroom(models.Model):
    number_of_bedrooms = models.IntegerField(default=0)
    def __str__(self):
        return str(self.number_of_bedrooms)

# Bathrooms table
class Bathroom(models.Model):
    number_of_bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    def __str__(self):
        return str(self.number_of_bathrooms)


# Cities table
class City(models.Model):
    name_of_cities = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name_of_cities)

# Categories table
class Category(models.Model):
    name_of_categories = models.TextField(blank=False)
    def __str__(self):
        return str(self.name_of_categories)

