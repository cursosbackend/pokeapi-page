from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Pokemon, Tipo


def pokemon_list(request):
    pokemons = Pokemon.objects.prefetch_related("tipos").all()
    tipos = Tipo.objects.all()

    search = request.GET.get("search", "").strip()
    tipo_filtro = request.GET.get("tipo", "").strip()

    if search:
        if search.isdigit():
            pokemons = pokemons.filter(numero_pokedex=int(search))
        else:
            pokemons = pokemons.filter(nombre__icontains=search)

    if tipo_filtro:
        pokemons = pokemons.filter(tipos__nombre=tipo_filtro)

    return render(request, "home.html", {
        "pokemons": pokemons,
        "tipos": tipos,
        "search": search,
        "tipo_filtro": tipo_filtro,
    })


def pokemon_detail(request, numero_pokedex):
    pokemon = get_object_or_404(
        Pokemon.objects.prefetch_related("tipos"),
        numero_pokedex=numero_pokedex,
    )
    return render(request, "detail.html", {"pokemon": pokemon})


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]
        if password != password_confirm:
            messages.error(request, "Las contraseñas no coinciden")
            return render(request, "auth/register.html")
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return render(request, "auth/register.html")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, "Registro exitoso")
        return redirect("pokemon_list")
    return render(request, "auth/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido, {username}")
            return redirect("pokemon_list")
        messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada")
    return redirect("pokemon_list")
