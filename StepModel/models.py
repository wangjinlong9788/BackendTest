
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from RecipeModel.models import Recipe

# Create your models here.
class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipestep',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True,null=False)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
