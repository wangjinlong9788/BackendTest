#from django.conf.urls import url,include
from django.urls import path
from .views import ListCreateIngredientView,IngredientDetailView


urlpatterns = [
    #url(r'^songs', ListSongsView.as_view(), name="songs-all")
    path('ingredients/', ListCreateIngredientView.as_view(), name="Ingredient-list-create"),
    path('ingredients/<int:pk>/',IngredientDetailView.as_view(),name="Ingredient-detail"),
    #path('songs/', ListCreateSongsView.as_view(), name="songs-list-create"),
    #path('songs/<int:pk>/',SongsDetailView.as_view(),name="songs-detail"),
]
