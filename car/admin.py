from webbrowser import register

from django.contrib import admin
from car.models import Car, Brand

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'model_year', 'brand', 'value']
    search_fields = ('model',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields =  ('name',)
