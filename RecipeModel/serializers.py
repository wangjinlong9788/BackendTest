from rest_framework import serializers
from .models import Recipe
#from IngredientModel.serializers import IngredientSerializer


class RecipeSerializer(serializers.ModelSerializer):
    #ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields ='__all__'
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
