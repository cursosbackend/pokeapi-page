# Control de Progreso - PokéView

## Fase 1: Configuración Inicial ✅
- [x] Configuración de entorno virtual y Django 6.0.
- [x] Configuración de `settings.py` con SQLite.
- [x] Creación de la app `pokemon`.

## Fase 2: Modelos y Base de Datos ✅
- [x] Creación de modelos `Tipo` y `Pokemon`.
- [x] Ejecución de migraciones (`makemigrations` y `migrate`).
- [x] Management command `import_pokemon` para poblar datos desde PokéAPI.

## Fase 3: Autenticación ✅
- [x] Implementación de `register_view`.
- [x] Implementación de `login_view` y `logout_view`.
- [x] Plantillas de login/registro estilizadas con Tailwind.

## Fase 4: Vistas del Catálogo y Filtros ✅
- [x] Vista basada en función `pokemon_list` con lógica `request.GET.get('search')`.
- [x] Filtro por tipo M2M.
- [x] Vista de detalle `pokemon_detail`.

## Fase 5: Despliegue en Render ✅
- [x] Configuración de `WhiteNoise` para estáticos.
- [x] Creación de `build.sh` y `requirements.txt`.
- [x] Despliegue en Render.
