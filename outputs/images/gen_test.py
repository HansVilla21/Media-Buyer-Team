"""
Test: Generación de imagen estilo Instagram sobre "Qué es Claude"
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# --- Config ---
SIZE = 1080
OUTPUT = os.path.join(os.path.dirname(__file__), "test-que-es-claude.png")

img = Image.new("RGB", (SIZE, SIZE), (0, 0, 0))
draw = ImageDraw.Draw(img)

# --- Gradiente de fondo (deep purple → dark navy) ---
for y in range(SIZE):
    t = y / SIZE
    r = int(18 + (8 - 18) * t)
    g = int(10 + (15 - 10) * t)
    b = int(40 + (55 - 40) * t)
    draw.line([(0, y), (SIZE, y)], fill=(r, g, b))

# --- Línea decorativa superior ---
ACCENT_CYAN = (0, 220, 255)
ACCENT_PURPLE = (160, 80, 255)
draw.rectangle([60, 80, SIZE - 60, 83], fill=ACCENT_CYAN)

# --- Punto brillante top-right (decorativo) ---
for r in range(120, 0, -10):
    alpha = int(255 * (1 - r / 120) * 0.15)
    draw.ellipse([SIZE - 200 - r, -r, SIZE - 200 + r, r], fill=(160, 80, 255))

# --- Fonts ---
def load_font(size, bold=False):
    try:
        path = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

font_title    = load_font(88, bold=True)
font_subtitle = load_font(34)
font_tag      = load_font(26, bold=True)
font_label    = load_font(44, bold=True)
font_body     = load_font(30)

# --- Título ---
title = "¿QUÉ ES CLAUDE?"
tw = draw.textlength(title, font=font_title)
draw.text(((SIZE - tw) / 2, 110), title, font=font_title, fill=(255, 255, 255))

# --- Subtítulo ---
sub = "El asistente de IA más avanzado del momento"
sw = draw.textlength(sub, font=font_subtitle)
draw.text(((SIZE - sw) / 2, 220), sub, font=font_subtitle, fill=(180, 180, 220))

# --- Línea divisoria ---
draw.rectangle([60, 290, SIZE - 60, 292], fill=(80, 80, 120))

# --- Helper: tarjeta de sección ---
def draw_card(y_start, icon_char, color, label, body):
    # Fondo de la tarjeta
    draw.rounded_rectangle([60, y_start, SIZE - 60, y_start + 155], radius=18,
                             fill=(25, 18, 55), outline=color, width=2)
    # Número / ícono circular
    cx, cy = 130, y_start + 77
    draw.ellipse([cx - 38, cy - 38, cx + 38, cy + 38], fill=color)
    iw = draw.textlength(icon_char, font=font_label)
    draw.text((cx - iw / 2, cy - 26), icon_char, font=font_label, fill=(10, 8, 30))
    # Texto
    draw.text((190, y_start + 22), label, font=font_label, fill=(255, 255, 255))
    draw.text((190, y_start + 82), body, font=font_body, fill=(180, 180, 220))

draw_card(
    320, "01", ACCENT_CYAN,
    "Conversación natural",
    "Entiende contexto y responde como humano"
)
draw_card(
    500, "02", ACCENT_PURPLE,
    "Razonamiento profundo",
    "Analiza, escribe, programa y crea contenido"
)
draw_card(
    680, "03", (0, 200, 120),
    "Creado por Anthropic",
    "IA diseñada con foco en seguridad y precisión"
)

# --- Línea inferior decorativa ---
draw.rectangle([60, SIZE - 90, SIZE - 60, SIZE - 87], fill=ACCENT_CYAN)

# --- Footer ---
footer = "@hansvilla.ai  ·  Momentum AI Academy"
fw = draw.textlength(footer, font=font_tag)
draw.text(((SIZE - fw) / 2, SIZE - 70), footer, font=font_tag, fill=(120, 120, 180))

# --- Guardar ---
img.save(OUTPUT, "PNG", quality=95)
print(f"Imagen guardada: {OUTPUT}")
