# Skill: publicar-instagram

## Qué hace
Publica o programa carruseles de Instagram desde una carpeta local usando la
Upload Post API. Funciona como módulo compartido para todos los scripts de
carrusel (`tips_carousel.py`, `noticias_ia_carousel.py`) y también como CLI
standalone para publicar slides ya generados.

## Cuándo usar esta skill
Cuando Hans pida alguna de estas cosas:
- "Publicá este carrusel"
- "Programá el post para las [hora]"
- "Subí los slides de [carpeta]"
- "Publicá el de tips / noticias que generé antes"
- Cualquier variación de publicar / subir / programar en Instagram

---

## Flujo de trabajo

### Opción A — Publicar inmediatamente
```bash
cd "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
PYTHONIOENCODING=utf-8 python scripts/uploader.py --dir outputs/tips/2026-03-12/claude-vs-chatgpt
```

### Opción B — Programar para una fecha/hora específica
```bash
PYTHONIOENCODING=utf-8 python scripts/uploader.py \
  --dir outputs/tips/2026-03-12/claude-vs-chatgpt \
  --fecha "2026-03-12T12:00:00-06:00"
```

### Opción C — Caption personalizado
```bash
PYTHONIOENCODING=utf-8 python scripts/uploader.py \
  --dir outputs/noticias/2026-03-12 \
  --caption "Texto personalizado del post\n\n#hashtags"
```

### Opción D — Dry run (verificar sin publicar)
```bash
PYTHONIOENCODING=utf-8 python scripts/uploader.py \
  --dir outputs/tips/2026-03-12/claude-vs-chatgpt \
  --dry-run
```

---

## Parámetros del CLI

| Flag | Alias | Requerido | Descripción |
|------|-------|-----------|-------------|
| `--dir` | `-d` | ✅ | Carpeta con los `slide-*.png` |
| `--caption` | `-c` | No | Caption personalizado. Si se omite, se auto-genera uno de noticias |
| `--fecha` | `-f` | No | ISO-8601 con timezone. Si se omite, publica de inmediato |
| `--dry-run` | — | No | Muestra info completa pero NO envía la request |

---

## Integración en los scripts de carrusel

Ambos scripts de carrusel (`tips_carousel.py`, `noticias_ia_carousel.py`)
soportan publicación directa al finalizar la generación:

```bash
# Generar + publicar ahora
PYTHONIOENCODING=utf-8 python scripts/tips_carousel.py --topic "Gemini" --publicar

# Generar + programar
PYTHONIOENCODING=utf-8 python scripts/tips_carousel.py --topic "Gemini" \
  --publicar --fecha "2026-03-13T09:00:00-06:00"

# Generar + caption personalizado + programar
PYTHONIOENCODING=utf-8 python scripts/noticias_ia_carousel.py \
  --publicar \
  --fecha "2026-03-14T09:00:00-06:00" \
  --caption "Lo mejor de la semana en IA 🤖\n\n#IA #LATAM"
```

Parámetros de publicación disponibles en ambos scripts:

| Flag | Descripción |
|------|-------------|
| `--publicar` / `-p` | Activa la publicación después de generar |
| `--fecha` / `-f` | ISO-8601 con timezone para programar |
| `--caption` / `-c` | Caption personalizado (si se omite, se auto-genera) |
| `--dry-run` | Preview sin enviar |

---

## Formato de fecha

La fecha debe ser **ISO-8601 con timezone explícito**:

| Zona | Offset | Ejemplo |
|------|--------|---------|
| Costa Rica / Centro América | `-06:00` | `2026-03-13T09:00:00-06:00` |
| Colombia / Perú / Ecuador | `-05:00` | `2026-03-13T09:00:00-05:00` |
| Argentina / Chile | `-03:00` | `2026-03-13T09:00:00-03:00` |
| México (Ciudad de México) | `-06:00` | `2026-03-13T09:00:00-06:00` |

---

## Estructura de carpetas de output

Los slides deben seguir el patrón `slide-*.png` dentro de la carpeta:

```
outputs/
├── tips/
│   └── 2026-03-12/
│       └── claude-vs-chatgpt/
│           ├── slide-01-cover.png
│           ├── slide-02-tip1.png
│           ├── slide-03-tip2.png
│           └── slide-07-cta.png
└── noticias/
    └── 2026-03-12/
        ├── slide-01-cover.png
        └── slide-06-cta.png
```

Máximo 10 slides por carrusel (límite de Instagram). Si hay más, se usan los
primeros 10 ordenados por nombre.

---

## Captions auto-generados

Cuando no se pasa `--caption`, el módulo genera uno según el tipo:

**Para tips** (se pasa el título del carrusel):
```
{titulo_carrusel}

Guardá este post para cuando lo necesites 🔖

#IA #InteligenciaArtificial #ChatGPT #Claude #Gemini
#ProductividadIA #Automatizacion #TipsIA #AprendeIA
#LATAM #EmprendimientoDigital #MomentumAI
```

**Para noticias** (se usa la fecha actual):
```
Lo que pasó en IA esta semana (12/03/2026) 🤖

Las noticias más importantes para que nada te pase por alto.

Guardá este post 🔖

#IA ...
```

Para generar un caption de tips desde código:
```python
from uploader import caption_tips
cap = caption_tips("Por qué todos están cambiando ChatGPT por Claude")
```

---

## Variables de entorno necesarias

| Variable | Descripción |
|----------|-------------|
| `UPLOAD_POST_API_KEY` | API key de Upload Post. Obtener en upload-post.com |
| `IG_ACCOUNT` | Nombre del perfil en Upload Post (actualmente: `hansvilla`) |

⚠️ **Importante:** `IG_ACCOUNT` debe coincidir exactamente con el nombre del
perfil en el dashboard de Upload Post, **no** con el handle de Instagram.
En este caso es `hansvilla`, no `hansvilla.ai`.

---

## Módulo `uploader.py`

El archivo `scripts/uploader.py` expone estas funciones importables:

```python
from uploader import publicar_carousel, caption_tips, caption_noticias, slides_en_directorio

# Publicar slides de una carpeta
slides = slides_en_directorio("outputs/tips/2026-03-12/claude-vs-chatgpt")
publicar_carousel(
    slides_paths   = slides,
    caption        = caption_tips("Mi título"),
    scheduled_date = "2026-03-13T09:00:00-06:00",  # None = ahora
    dry_run        = False,
)
```

---

## Errores comunes y soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `"At least one platform is required"` | Falta el campo `platform[]` | Ya corregido en `uploader.py` |
| `"Username not associated with any profile"` | `IG_ACCOUNT` no coincide con el perfil en Upload Post | Verificar en el dashboard y actualizar `.env` |
| `"missing_api_key"` | `UPLOAD_POST_API_KEY` no está en `.env` | Agregar la key al `.env` |
| `"No se encontraron slide-*.png"` | La carpeta está vacía o mal escrita | Verificar la ruta con `ls outputs/...` |
