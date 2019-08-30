
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Ingredient



class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',  'description')
    #list_filter = ('name', 'description')
    #list_editable = ('name',  'description')
admin.site.register(Ingredient, IngredientAdmin)
