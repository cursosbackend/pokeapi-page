import requests
from django.core.management.base import BaseCommand
from pokemon.models import Tipo, Pokemon

TYPE_COLORS = {
    "normal": "#A8A77A",
    "fire": "#EE8130",
    "water": "#6390F0",
    "electric": "#F7D02C",
    "grass": "#7AC74C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#735797",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD",
}


class Command(BaseCommand):
    help = "Importa Pokémon desde PokéAPI"

    def add_arguments(self, parser):
        parser.add_argument("--limit", type=int, default=151, help="Cantidad de Pokémon a importar")

    def handle(self, *args, **options):
        limit = options["limit"]
        self.stdout.write(f"Importando {limit} Pokémon desde PokéAPI...")

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset=0")
        response.raise_for_status()
        results = response.json()["results"]

        for i, entry in enumerate(results, 1):
            self.stdout.write(f"[{i}/{limit}] {entry['name']}...")
            self._import_pokemon(entry["url"])

        self.stdout.write(self.style.SUCCESS(f"Importación completada: {limit} Pokémon"))

    def _import_pokemon(self, url):
        data = requests.get(url).json()
        species_data = requests.get(data["species"]["url"]).json()

        numero = data["id"]
        nombre = data["name"]
        imagen = data["sprites"]["other"]["official-artwork"]["front_default"] or data["sprites"]["front_default"]

        stats_map = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}

        descripcion = None
        for entry in species_data["flavor_text_entries"]:
            if entry["language"]["name"] == "en":
                descripcion = entry["flavor_text"].replace("\n", " ").replace("\x0c", " ")
                break

        pokemon, _ = Pokemon.objects.update_or_create(
            numero_pokedex=numero,
            defaults={
                "nombre": nombre,
                "imagen_url": imagen,
                "hp": stats_map.get("hp", 0),
                "ataque": stats_map.get("attack", 0),
                "defensa": stats_map.get("defense", 0),
                "velocidad": stats_map.get("speed", 0),
                "descripcion": descripcion,
            },
        )

        for tipo_data in data["types"]:
            tipo_nombre = tipo_data["type"]["name"]
            tipo, _ = Tipo.objects.get_or_create(
                nombre=tipo_nombre,
                defaults={"color_hex": TYPE_COLORS.get(tipo_nombre, "#A8A77A")},
            )
            pokemon.tipos.add(tipo)
