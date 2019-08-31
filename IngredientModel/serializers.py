from rest_framework import serializers
from . import models
from RecipeModel.models import Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields ='__all__'
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.description = validated_data.get('description', instance.description)
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.save()
        return instance
