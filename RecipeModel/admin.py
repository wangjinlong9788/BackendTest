from django.contrib import admin

# Register your models here.
from .models import Recipe


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'description']#'work_address'


admin.site.register(Recipe, RecipeAdmin)
