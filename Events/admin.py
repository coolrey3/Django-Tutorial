from django.contrib import admin
from . models import Event, Offer , Product
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','price','description','sponsored','rating')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','event', 'category','price','description','sponsored','rating')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','event', 'description' , 'discount')


admin.site.register(Event, EventAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
