# Skill: tips-ia-carousel

## Qué hace
Genera carruseles de Instagram con tips prácticos de IA para la audiencia de
@hansvilla.ai: profesionales LATAM que CASI NO usan IA todavía. El sistema
investiga qué temas necesita la audiencia, Hans elige uno, y se genera el
carrusel completo con el estilo visual de Momentum AI Academy.

## Cuándo usar esta skill
Cuando Hans pida alguna de estas cosas:
- "Dame ideas para tips de IA"
- "Quiero hacer un carrusel de tips"
- "Hagamos uno sobre [herramienta]"
- "Qué tips puedo publicar esta semana"
- Cualquier variación de tips / consejos / cómo usar X herramienta

---

## Flujo de trabajo (SIEMPRE en dos pasos)

### PASO 1 — Investigar ideas
```bash
cd "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
PYTHONIOENCODING=utf-8 python scripts/tips_carousel.py --ideas
```
Devuelve 10 ideas con título sugerido y por qué funciona para la audiencia.
Hans elige una por número o por nombre.
La lista se guarda en `outputs/tips/YYYY-MM-DD/ideas.json`.

### PASO 2 — Generar el carrusel
```bash
# Básico (5 tips, título auto-generado)
PYTHONIOENCODING=utf-8 python scripts/tips_carousel.py --topic "Claude"

# Con cantidad personalizada
PYTHONIOENCODING=utf-8 python scripts/tips_carousel.py --topic "n8n" --cantidad 6

# Con título personalizado
PYTHONIOENCODING=utf-8 python scripts/tips_carousel.py --topic "Claude vs ChatGPT" --titulo "Por qué todos están cambiando ChatGPT por Claude" --cantidad 5
```
`--cantidad` acepta entre 3 y 7 (default: 5).

---

## Parámetros disponibles

| Flag | Alias | Default | Descripción |
|------|-------|---------|-------------|
| `--ideas` | `-i` | — | Investigar y listar 10 ideas de temas (Paso 1) |
| `--topic` | `-t` | `"Claude"` | Herramienta o tema del carrusel (Paso 2) |
| `--titulo` | `-T` | _(auto)_ | Título personalizado del carrusel |
| `--cantidad` | `-n` | `5` | Número de tips: mínimo 3, máximo 7 |

---

## Output
Carpeta: `outputs/tips/YYYY-MM-DD/[slug-del-tema]/`
- `slide-01-cover.png`     — Cover con título y CTA "Deslizá para aprender →"
- `slide-02-tip1.png`      — Tip 1
- `slide-03-tip2.png`      — Tip 2
- ...
- `slide-NN-cta.png`       — CTA final oscuro
- `tips.json`              — Data cruda de Perplexity (referencia)

---

## Audiencia objetivo
Profesionales LATAM 25-40 años que **CASI NO usan IA**:
empleados, freelancers, contadores, diseñadores, vendedores, dueños de pymes.
La mayoría conoce ChatGPT de nombre pero apenas lo usó.
**No son desarrolladores. Nunca van a instalar nada ni tocar código.**

Todo el contenido debe sentirse como: *"Esto lo puedo probar ahora mismo."*

---

## Criterios del contenido

### Ideas (PASO 1):
- Nivel cero — como si nunca hubieran abierto ChatGPT
- Herramienta gratuita (ChatGPT gratis, Claude gratis, Gemini, Copilot)
- Beneficio claro y cotidiano: ahorrar tiempo, escribir mejor, no olvidar cosas
- Accionable en 10 minutos con lo que ya tienen
- Sin jerga: nada de "agentes", "APIs", "tokens", "embeddings", "LLMs"

### Tips generados (PASO 2):
- Concretos: qué hacer exactamente, no abstracciones
- En español LATAM: "podés", "escribí", "abrí", "andá"
- Con ejemplo o número cuando sea posible
- Sin markdown ni asteriscos en el texto
- Al menos 1 tip por carrusel tiene prompt listo para copiar (`es_prompt: true`)

---

## Layouts de slides

### Layout A — Con prompt (`es_prompt: true`)
```
[badge número azul]
[título grande extrabold]
[línea acento gradiente]
[cuerpo — hasta 5 líneas, font 38px]
┌─────────────────────────────────────┐
│ PROMPT                              │  ← etiqueta teal
│ "texto del prompt listo para        │  ← fondo oscuro #16161e
│  copiar y pegar en la herramienta"  │  ← texto blanco
└─────────────────────────────────────┘
[footer: IG icon · @hansvilla.ai · M logo · N/total]
```

### Layout B — Sin prompt (`es_prompt: false`)
```
[badge número azul]
[título grande extrabold]
[línea acento gradiente]
[cuerpo — hasta 7 líneas, font 44px más grande]

   ← espacio visual respira ←

┌─────────────────────────────────────┐
▌ CLAVE                               │  ← borde izq teal, fondo oscuro #12181e
│ La frase más importante del tip     │  ← texto blanco bold
│ en máx 12 palabras                  │
└─────────────────────────────────────┘
[footer]
```

La caja **CLAVE** siempre está anclada cerca del footer, sin dejar espacio vacío.
Es el resultado concreto que el lector se lleva del tip.

---

## Diferencias con noticias-ia-carousel

| Dimensión | noticias-ia-carousel | tips-ia-carousel |
|-----------|---------------------|-----------------|
| Contenido | Noticias de la semana | Tips evergreen + actuales |
| Fuente | Artículos web reales | Perplexity genera el contenido |
| Imágenes | og:image del artículo | Sin imágenes externas |
| Frecuencia | 1x por semana | On-demand por tema |
| Caja especial | Banda fallback si no hay imagen | PROMPT o CLAVE según el tipo |

---

## Variables de entorno necesarias
- `PERPLEXITY_API_KEY` — para investigar ideas y generar los tips
- Fonts en `Documentos subidos/Montserrat/static/`
- Logo en `Documentos subidos/Momentum_isologo color (1).png`
- Ícono IG en `Documentos subidos/Instagram_logo_2022.svg.png`

---

## Personalización
Para ajustar criterios de audiencia, tono o tipos de tips:
editar `SYSTEM_PROMPT_IDEAS` y `SYSTEM_PROMPT_TIPS` en `scripts/tips_carousel.py`.

Para ajustar el diseño visual:
editar `make_cover_tips()`, `make_tip_slide()`, `make_cta_slide()`.
