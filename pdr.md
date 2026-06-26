Markdown# Product Requirement Document (PRD)
## Proyecto: PokéView - Plataforma de Visualización y Gestión de Pokémon

---

## 1. Visión General del Proyecto
**PokéView** es una aplicación web interactiva que permite a los usuarios explorar, buscar y filtrar Pokémon. El sistema contará con un módulo de autenticación (registro, inicio de sesión y cierre de sesión) para ofrecer una experiencia personalizada. Estará construido con **Django 6.0**, utilizará **SQLite** como motor de base de datos local y su interfaz gráfica estará potenciada por **Tailwind CSS** mediante CDN. El despliegue final se realizará en **Render**.

### Objetivos Principales
* Proporcionar un catálogo visual, rápido y responsivo de Pokémon.
* Implementar un sistema robusto de búsqueda por nombre/número y filtrado por tipos.
* Garantizar la persistencia de usuarios mediante el sistema nativo de autenticación de Django.
* Mantener una arquitectura limpia utilizando **Vistas Basadas en Funciones (FBVs)**.

---

## 2. Alcance y Características (Scope)

### 2.1. Funcionalidades Core (MVP)
* **Autenticación de Usuarios:** Registro de nuevos usuarios, Login y Logout utilizando el sistema de `auth` nativo de Django.
* **Dashboard / Home:** Galería de tarjetas (Cards) de Pokémon que muestra su número de Pokédex, imagen, nombre y tipos asociados.
* **Buscador en Tiempo Real/Filtros:** Barra de búsqueda que procesa coincidencias por nombre o número exacto, complementado con selectores para filtrar por tipo (Fuego, Agua, Planta, etc.).
* **Vista de Detalle:** Página individual para cada Pokémon que detalla sus estadísticas base (HP, Ataque, Defensa, etc.), habilidades y descripción.

### 2.2. Restricciones Técnicas
* **Framework:** Django 6.0
* **Base de Datos:** SQLite (archivo local).
* **Frontend:** Django Templates tradicionales + **Tailwind CSS vía CDN**.
* **Arquitectura de Vistas:** Estrictamente **Vistas Basadas en Funciones (FBVs)**.
* **Plataforma de Despliegue:** Render.

---

## 3. Arquitectura del Sistema y Estructura de Datos

### 3.1. Modelos de Base de Datos (`models.py`)
```python
from django.db import models
from django.contrib.auth.models import User

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
    
    # Estadísticas Base
    hp = models.IntegerField(default=0)
    ataque = models.IntegerField(default=0)
    defensa = models.IntegerField(default=0)
    velocidad = models.IntegerField(default=0)
    
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"#{self.numero_pokedex} - {self.nombre}"
4. Diseño de Rutas y Vistas (Endpoints)Todas las vistas serán procesadas mediante funciones (def) en views.py.4.1. Mapeo de URLs (urls.py)URL PatrónNombre de la RutaVista AsociadaDescripción/homepokemon_listCatálogo general con búsqueda y filtros./pokemon/<int:pokedex_num>/pokemon_detailpokemon_detailDetalle extendido de un Pokémon específico./login/loginlogin_viewFormulario e inicio de sesión de usuarios./logout/logoutlogout_viewCierre de sesión y redirección./register/registerregister_viewFormulario de registro y creación de cuenta.5. Estructura de Carpetas RecomendadaPlaintextpokeview/
│
├── core/                  # Configuración de Django
│   ├── settings.py
│   └── urls.py
│
├── pokemon/               # Aplicación principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── detail.html
│       └── auth/
│           ├── login.html
│           └── register.html
│
├── docs/                  # Documentación del progreso
│   ├── PROGRESO.md
│   └── FUTURE_FEATURES.md
│
├── requirements.txt
├── build.sh               # Script de construcción para Render
└── PRD.md                 # Este documento
6. Documentación del Progreso (docs/)Archivo: docs/PROGRESO.mdMarkdown# Control de Progreso - PokéView

## Fase 1: Configuración Inicial ⏳
- [ ] Configuración de entorno virtual y Django 6.0.
- [ ] Configuración de `settings.py` con SQLite.
- [ ] Creación de la app `pokemon`.

## Fase 2: Modelos y Base de Datos ⏳
- [ ] Creación de modelos `Tipo` y `Pokemon`.
- [ ] Ejecución de migraciones (`makemigrations` y `migrate`).
- [ ] Script o Fixture para poblar datos iniciales.

## Fase 3: Autenticación ⏳
- [ ] Implementación de `register_view`.
- [ ] Implementación de `login_view` y `logout_view`.
- [ ] Plantillas de login/registro estilizadas con Tailwind.

## Fase 4: Vistas del Catálogo y Filtros ⏳
- [ ] Vista basada en función `pokemon_list` con lógica `request.GET.get('search')`.
- [ ] Filtro por tipo M2M.
- [ ] Vista de detalle `pokemon_detail`.

## Fase 5: Despliegue en Render ⏳
- [ ] Configuración de `WhiteNoise` para estáticos.
- [ ] Creación de `build.sh` y `requirements.txt`.
- [ ] Despliegue en Render.
Archivo: docs/FUTURE_FEATURES.mdMarkdown# Futuras Implementaciones y Roadmaps

1. **Integración con PokéAPI Sincrónica**: Automatizar un comando de Django (`python manage.py import_pokemon`) para traer datos directo de la API oficial a SQLite de forma local.
2. **HTMX para Búsqueda Asíncrona**: Filtrar y buscar Pokémon en tiempo real sin recargar la página completa.
3. **Paginación Infinita (Scroll Infinito)**: Cargar dinámicamente más tarjetas de Pokémon a medida que el usuario baja en la web.
4. **Sistema de Favoritos**: Permitir que los usuarios autenticados guarden sus Pokémon preferidos en su perfil.
7. Estrategia de Despliegue (Render)Archivo build.shBash#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

---

### Instrucciones para la carpeta `docs/`
Para estructurar el proyecto tal como lo pediste:
1. Crea una carpeta llamada **`docs`** en la raíz de tu proyecto Django.
2. Dentro de esa carpeta, crea un archivo llamado **`PROGRESO.md`** y pega el fragmento de la *Fase 1 a la 5* que está en la sección 6 del documento.
3. Crea otro archivo llamado **`FUTURE_FEATURES.md`** y pega las ideas de la hoja de ruta que dejé especificadas arriba.

¡Con esto ya tienes toda la base documental guardada localmente en Markdown para empezar a codear! Si necesitas ayuda con las funciones de las vistas (`views.py`) o las plantillas HTML con Tailwind CDN, me avisas