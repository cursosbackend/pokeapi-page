from django.db import models


class Tipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    color_hex = models.CharField(max_length=7, default="#A8A77A")

    def __str__(self):
        return self.nombre


class Pokemon(models.Model):
    numero_pokedex = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    imagen_url = models.URLField(max_length=500)
    tipos = models.ManyToManyField(Tipo, related_name="pokemones")
    hp = models.IntegerField(default=0)
    ataque = models.IntegerField(default=0)
    defensa = models.IntegerField(default=0)
    velocidad = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"#{self.numero_pokedex} - {self.nombre}"
