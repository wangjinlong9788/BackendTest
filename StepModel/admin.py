from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Step



class StepAdmin(admin.ModelAdmin):
    list_display = ('name',  'description')
    list_filter = ('name','description')
    list_editable = ( 'description',)
admin.site.register(Step, StepAdmin)
