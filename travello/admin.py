from unicodedata import category
from django.contrib import admin
from . models import Destination
from . models import Category
from . models import Restaurant
from . models import Review
# Register your models here.

class Categoryadmin(admin.ModelAdmin):
    list_display = ('id','Name','Name_of_Buisness')
class Restaurantadmin(admin.ModelAdmin):
    list_display = ('id','Name','Neighbourhood','Address','City','Pin','Latitude','Longitude','IsOpen','Category','Stars','ReviewCount')
    list_filter = ('Category','City','IsOpen')
class Reviewadmin(admin.ModelAdmin):
    list_display = ('id','Restaurant_Id','Stars','Date','Text')
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Destination)
admin.site.register(Category,Categoryadmin)
admin.site.register(Restaurant,Restaurantadmin)
admin.site.register(Review,Reviewadmin)
