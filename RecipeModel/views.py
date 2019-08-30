from django.shortcuts import render


# Create your views here.
from rest_framework import generics
from rest_framework import permissions

from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class ListCreateRecipeView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_class=(permissions.AllowAny,)


    def post(self,request,*args,**kwargs):


        id=request.data["user"]
        user = User.objects.get(id=id)
        a_Recipe=Recipe.objects.create(

           name=request.data["name"],
           description=request.data["description"],
           user=user#self.request.user#User.objects.filter()
        )
        return Response(
          data=RecipeSerializer(a_Recipe).data,
          status=status.HTTP_201_CREATED
        )




class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET recipe/:id/
    PUT recipe/:id/
    DELETE recipe/:id/
    """
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer
    permission_classes=(permissions.AllowAny,)

    def get(self,request,*args,**kwargs):
        try:
            a_Recipe=self.queryset.get(pk=kwargs['pk'])
            return Response(RecipeSerializer(a_Recipe).data)
        except Recipe.DoesNotExist:
            return Response(
               data={
                  "message":"Recipe with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )
    def put(self,request,*args,**kwargs):
        try:
            a_Recipe=self.queryset.get(pk=kwargs['pk'])
            serializer=RecipeSerializer()
            #updated_Recipe=serializer.update(a_Recipe,request.data)
            id=request.data["user"]
            user = User.objects.get(id=id)
            updated_Recipe=serializer.update(a_Recipe,{"name":request.data["name"],"description":request.data["description"],"user":user})
            return Response(RecipeSerializer(updated_Recipe).data)
        except Recipe.DoesNotExist:
            return Response(
               data={
                  "message":"Recipe with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )

    def delete(self,request,*args,**kwargs):
        try:
            a_Recipe=self.queryset.get(pk=kwargs['pk'])
            a_Recipe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Recipe.DoesNotExist:
            return Response(
               data={
                  "message":"Recipe with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )
class RecipeUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET userrecipe/:id/
    PUT userrecipe/:id/
    DELETE userrecipe/:id/
    """
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer
    permission_classes=(permissions.AllowAny,)

    def get(self,request,*args,**kwargs):
        try:
            a_User=User.objects.get(pk=kwargs['pk'])
            a_Recipe=Recipe.objects.get(user=a_User)
            return Response(RecipeSerializer(a_Recipe).data)
        except User.DoesNotExist:
            return Response(
               data={
                  "message":"User with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )

    def put(self,request,*args,**kwargs):
        try:
            a_User=User.objects.get(pk=kwargs['pk'])
            a_Recipe=Recipe.objects.get(user=a_User)

            #a_Recipe=self.queryset.get(pk=kwargs['pk'])
            serializer=RecipeSerializer()
            id=request.data["user"]
            user = User.objects.get(id=id)
            updated_Recipe=serializer.update(a_Recipe,{"name":request.data["name"],"description":request.data["description"],"user":user})
            return Response(RecipeSerializer(updated_Recipe).data)
        except Recipe.DoesNotExist:
            return Response(
               data={
                  "message":"Recipe with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )

    def delete(self,request,*args,**kwargs):
        try:
            a_User=User.objects.get(pk=kwargs['pk'])
            a_Recipe=Recipe.objects.get(user=a_User)
            a_Recipe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Recipe.DoesNotExist:
            return Response(
               data={
                  "message":"Recipe with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )
