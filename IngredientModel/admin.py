
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Ingredient



class IngredientAdmin(admin.ModelAdmin):
    list_display = ('text',  'description')
    #list_filter = ('text', 'description')
    #list_editable = ('text',  'description')
admin.site.register(Ingredient, IngredientAdmin)
