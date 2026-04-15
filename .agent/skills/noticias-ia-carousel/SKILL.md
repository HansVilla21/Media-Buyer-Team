# Skill: noticias-ia-carousel

## Qué hace
Genera un carrusel de Instagram completo con las últimas noticias de IA,
listo para subir. Busca información real con Perplexity, extrae la og:image
de cada artículo (sin duplicados), y renderiza todos los slides con el estilo
de @hansvilla.ai (Montserrat, paleta Momentum, formato 1080x1350).

## Cuándo usar esta skill
Cuando Hans pida alguna de estas cosas:
- "Dame el carrusel de noticias de esta semana"
- "Quiero publicar las noticias de IA"
- "Haceme el post de novedades de IA"
- Cualquier variación de noticias / novedades / lo que pasó en IA

## Cómo ejecutarla

```bash
cd "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
PYTHONIOENCODING=utf-8 python scripts/noticias_ia_carousel.py
```

## Output
Carpeta: `outputs/noticias/YYYY-MM-DD/`
Total: **10 slides** (cover + 2 por noticia × 4 + CTA)

| Slide | Archivo | Contenido |
|-------|---------|-----------|
| 01 | `slide-01-cover.png` | Cover "LO QUE PASÓ EN IA ESTA SEMANA" + fecha |
| 02 | `slide-02-noticia1.png` | Imagen + titular + resumen de noticia 1 |
| 03 | `slide-03-pqi1.png` | Slide oscuro "¿POR QUÉ TE IMPORTA?" noticia 1 |
| 04 | `slide-04-noticia2.png` | Noticia 2 |
| 05 | `slide-05-pqi2.png` | ¿Por qué te importa? noticia 2 |
| 06 | `slide-06-noticia3.png` | Noticia 3 |
| 07 | `slide-07-pqi3.png` | ¿Por qué te importa? noticia 3 |
| 08 | `slide-08-noticia4.png` | Noticia 4 |
| 09 | `slide-09-pqi4.png` | ¿Por qué te importa? noticia 4 |
| 10 | `slide-10-cta.png` | CTA final oscuro |
| — | `noticias.json` | Data cruda de Perplexity (referencia) |
| — | `img-noticiaX.png` | Imágenes descargadas de los artículos |

## Criterios de selección (SYSTEM_PROMPT actual)

### Incluir — solo estas categorías:
1. Nuevos modelos o actualizaciones importantes (ChatGPT, Claude, Gemini, Grok, Llama)
2. Herramientas nuevas que cualquier persona puede usar hoy (extensiones, apps, integraciones n8n/Make/Zapier)
3. Nuevos usos o casos prácticos virales de IA
4. Cambios en herramientas que la gente ya usa (ChatGPT, Claude, Cursor, Perplexity, Notion AI, etc.)

### Excluir:
- Noticias de inversiones, valoraciones, financiamiento
- Estadísticas macro (McKinsey, Gartner, consultoras)
- Regulación/política sin impacto inmediato
- Investigación académica sin aplicación práctica
- Noticias de más de 10 días
- Fuentes de YouTube, TikTok, Twitch u otras plataformas de video

### Fuentes priorizadas:
The Verge, TechCrunch, Wired, Ars Technica, blogs oficiales de OpenAI/Anthropic/Google.
Cada noticia debe venir de un dominio diferente (evita repetir imágenes).

## Estilo del copy

### Resumen (campo `resumen`)
- Empieza con el hecho concreto: qué lanzaron / qué cambió / qué se puede hacer
- Explica cómo cambia la vida del lector (con ejemplo concreto)
- Cierra con una acción: "Lo podés probar en..." o "Funciona para..."
- 3-4 oraciones, máximo 90 palabras, sin jerga técnica, sin asteriscos ni markdown

### ¿Por qué te importa? (campo `por_que_importa`) — slide oscuro dedicado
- 1-2 oraciones MÁXIMO, 30 palabras máximo
- Habla directo al lector: "Si sos...", "Para vos que...", "Esto significa que..."
- Impacto concreto en su trabajo o ingreso, no en la industria
- **Tiene su propio slide oscuro** después de cada noticia: fondo dark, etiqueta teal, texto blanco extrabold grande
- NO va incrustado en el slide de la noticia — siempre es slide separado

## Lógica de imágenes
1. Se extrae la `og:image` real del artículo (no se pide a Perplexity que la invente)
2. Se descartan URLs duplicadas (misma imagen en varios slides)
3. Se descartan artículos del mismo dominio para garantizar variedad visual
4. Si no hay imagen disponible: se renderiza una banda decorativa azul→teal con el nombre de la fuente en blanco

## Variables de entorno necesarias
- `PERPLEXITY_API_KEY` — para buscar noticias
- Fonts en `Documentos subidos/Montserrat/static/`
- Logo en `Documentos subidos/Momentum_isologo color (1).png`
- Ícono IG en `Documentos subidos/Instagram_logo_2022.svg.png`

## Personalización
Para cambiar el foco de búsqueda (ej: solo automatización, solo OpenAI),
editar el `SYSTEM_PROMPT` y el mensaje de usuario en `buscar_noticias()`
dentro de `scripts/noticias_ia_carousel.py`.
