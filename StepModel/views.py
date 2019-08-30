from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework import permissions

from .models import Step
from RecipeModel.models import Recipe
from .serializers import StepSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
class ListCreateStepView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_class=(permissions.AllowAny,)


    def post(self,request,*args,**kwargs):


        id=request.data["recipe"]
        recipe = Recipe.objects.get(id=id)
        a_Step=Step.objects.create(

           name=request.data["name"],
           description=request.data["description"],
           recipe=recipe#self.request.user#User.objects.filter()
        )
        return Response(
          data=StepSerializer(a_Step).data,
          status=status.HTTP_201_CREATED
        )




class StepDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Step/:id/
    PUT Step/:id/
    DELETE Step/:id/
    """
    queryset=Step.objects.all()
    serializer_class=StepSerializer
    permission_classes=(permissions.AllowAny,)

    def get(self,request,*args,**kwargs):
        try:
            a_Step=self.queryset.get(pk=kwargs['pk'])
            return Response(StepSerializer(a_Step).data)
        except Step.DoesNotExist:
            return Response(
               data={
                  "message":"Step with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )

    def put(self,request,*args,**kwargs):
        try:
            a_Step=self.queryset.get(pk=kwargs['pk'])
            serializer=StepSerializer()
            #updated_Recipe=serializer.update(a_Recipe,request.data)
            id=request.data["recipe"]
            recipe = Recipe.objects.get(id=id)
            updated_Step=serializer.update(a_Step,{"name":request.data["name"],"description":request.data["description"],"recipe":recipe})
            return Response(StepSerializer(updated_Step).data)
        except Step.DoesNotExist:
            return Response(
               data={
                  "message":"Step with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )


    def delete(self,request,*args,**kwargs):
        try:
            a_Step=self.queryset.get(pk=kwargs['pk'])
            a_Step.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Step.DoesNotExist:
            return Response(
               data={
                  "message":"Step with id: {} dose not exist".format(kwargs["pk"])
               },
               status=status.HTTP_404_NOT_FOUND
            )
