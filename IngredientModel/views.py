from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework import permissions

from .models import Ingredient
from RecipeModel.models import Recipe
from .serializers import IngredientSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
class ListCreateIngredientView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_class=(permissions.AllowAny,)


    def post(self,request,*args,**kwargs):
        #id=self.kwargs["user"]
        #user = User.objects.get(id=id)
        #id=self.kwargs["user"]

        id=request.data["recipe"]
        recipe = Recipe.objects.get(id=id)
        a_Ingredient=Ingredient.objects.create(

           name=request.data["name"],
           description=request.data["description"],
           recipe=recipe#self.request.user#User.objects.filter()
        )
        return Response(
          data=IngredientSerializer(a_Ingredient).data,
          status=status.HTTP_201_CREATED
        )




class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Ingredient/:id/
    PUT Ingredient/:id/
    DELETE Ingredient/:id/
    """
    queryset=Ingredient.objects.all()
    serializer_class=IngredientSerializer
    permission_classes=(permissions.AllowAny,)

    def get(self,request,*args,**kwargs):
        try:
            a_Ingredient=self.queryset.get(pk=kwargs['pk'])
            return Response(IngredientSerializer(a_Ingredient).data)
        except Ingredient.DoesNotExist:
            return Response(
               data={
                  "message":"Ingredient with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )

    def put(self,request,*args,**kwargs):
        try:
            a_Ingredient=self.queryset.get(pk=kwargs['pk'])
            serializer=IngredientSerializer()
            #updated_Recipe=serializer.update(a_Recipe,request.data)
            id=request.data["recipe"]
            recipe = Recipe.objects.get(id=id)
            updated_Ingredient=serializer.update(a_Ingredient,{"name":request.data["name"],"description":request.data["description"],"recipe":recipe})
            return Response(IngredientSerializer(updated_Ingredient).data)
        except Ingredient.DoesNotExist:
            return Response(
               data={
                  "message":"Ingredient with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )


    def delete(self,request,*args,**kwargs):
        try:
            a_Ingredient=self.queryset.get(pk=kwargs['pk'])
            a_Ingredient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ingredient.DoesNotExist:
            return Response(
               data={
                  "message":"Ingredient with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )
