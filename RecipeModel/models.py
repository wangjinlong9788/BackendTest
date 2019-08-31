from django.db import models
# Create your models here.

from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import User
#from IngredientModel.models import Ingredient
#from StepModel.models import Step


class Recipe(models.Model):
    #user=models.ForeignKey(User,unique=True, related_name='recipes',on_delete=models.CASCADE)
    user=models.OneToOneField(User, related_name='recipes',on_delete=models.CASCADE)
    #ingredient = models.ForeignKey(Ingredient, related_name='ingredient',on_delete=models.CASCADE)
    #step = models.ForeignKey(Step, related_name='step',on_delete=models.CASCADE)

    name = models.CharField(max_length=250,null=False)
    description = models.CharField(max_length=250)



    class Meta:
        ordering = ('-name', )

    def __str__(self):
        return 'Recipe {}'.format(self.id)
