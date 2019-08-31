# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from RecipeModel.models import Recipe

# Create your models here.
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes',on_delete=models.CASCADE)
    text = models.CharField(max_length=200, db_index=True,null=False)
    description = models.TextField(blank=True)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    #stock = models.PositiveIntegerField()
    #available = models.BooleanField(default=True)


    class Meta:
        ordering = ('text', )
    #def get_absolute_url(self):
    #    return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.text
