from django.urls import path
from recipes.views import RecipeListView, RecipeCreateView, RecipeDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', login_required(RecipeCreateView.as_view()), name='recipe_add')

]