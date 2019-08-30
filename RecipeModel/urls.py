#from django.conf.urls import url,include
from django.urls import path
from .views import ListCreateRecipeView,RecipeDetailView,RecipeUserDetailView


urlpatterns = [
    #url(r'^songs', ListSongsView.as_view(), name="songs-all")
    path('recipes/', ListCreateRecipeView.as_view(), name="recipe-list-create"),
    path('recipes/<int:pk>/',RecipeDetailView.as_view(),name="recipe-detail"),
    path('userrecipes/<int:pk>/',RecipeUserDetailView.as_view(),name="user-recipe-detail"),

]
