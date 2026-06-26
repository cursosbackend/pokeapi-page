from django.urls import path
from . import views

urlpatterns = [
    path("", views.pokemon_list, name="pokemon_list"),
    path("<int:numero_pokedex>/", views.pokemon_detail, name="pokemon_detail"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]
