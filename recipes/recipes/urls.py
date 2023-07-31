from django.urls import path, re_path
from calculator.views import recipe_view

urlpatterns = [
    # re_path(r'^[a-zA-Z]*<str:product>$/', recipe_view, name='recipe')
    path('<str:product>/', recipe_view, name='recipe')
]
