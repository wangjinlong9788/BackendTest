from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Step



class StepAdmin(admin.ModelAdmin):
    list_display = ('step_txt',  'description')
    list_filter = ('step_txt','description')
    list_editable = ( 'description',)
admin.site.register(Step, StepAdmin)
