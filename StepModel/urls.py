#from django.conf.urls import url,include
from django.urls import path
from .views import ListCreateStepView,StepDetailView


urlpatterns = [
    #url(r'^songs', ListSongsView.as_view(), name="songs-all")
    path('steps/', ListCreateStepView.as_view(), name="Step-list-create"),
    path('steps/<int:pk>/',StepDetailView.as_view(),name="Step-detail"),
     
]
