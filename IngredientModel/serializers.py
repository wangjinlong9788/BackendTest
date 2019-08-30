from rest_framework import serializers
from . import models
from RecipeModel.models import Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        #fields = ('name', 'description')
        fields ='__all__'
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.save()
        return instance
