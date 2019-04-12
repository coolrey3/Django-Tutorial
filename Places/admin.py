from django.contrib import admin
from . models import Places
# Register your models here.


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','price','description','sponsored','rating')

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','event', 'category','price','description','sponsored','rating')
#
# class OfferAdmin(admin.ModelAdmin):
#     list_display = ('code','event', 'description' , 'discount')


admin.site.register(Places, PlacesAdmin)
# admin.site.register(Offer, OfferAdmin)
# admin.site.register(Product, ProductAdmin)
