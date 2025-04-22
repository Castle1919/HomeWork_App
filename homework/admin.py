from django.contrib import admin
from . import models

admin.site.register(models.Homework)
admin.site.register(models.Product)
admin.site.register(models.Order)   
admin.site.register(models.Article)

class IceCreamInline(admin.TabularInline):
    model = models.IceCreamKiosk.ice_creams.through

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

@admin.register(models.Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'favorite_ice_cream')

@admin.register(models.IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'flavor')

@admin.register(models.IceCreamKiosk)
class IceCreamKioskAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [IceCreamInline]