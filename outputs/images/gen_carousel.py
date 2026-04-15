"""
Sistema de generación de carruseles para @hansvilla.ai
Estilo: Minimal blanco + acento del logo Momentum
Fuente: Montserrat
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, textwrap

# --- Rutas base ---
BASE = "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
FONTS = f"{BASE}/Documentos subidos/Montserrat/static"
ASSETS = f"{BASE}/Documentos subidos"
OUT = f"{BASE}/outputs/images"

def font(weight, size):
    names = {
        "regular":    "Montserrat-Regular.ttf",
        "medium":     "Montserrat-Medium.ttf",
        "semibold":   "Montserrat-SemiBold.ttf",
        "bold":       "Montserrat-Bold.ttf",
        "extrabold":  "Montserrat-ExtraBold.ttf",
    }
    return ImageFont.truetype(f"{FONTS}/{names[weight]}", size)

# --- Paleta ---
BG          = (252, 251, 249)      # crema cálido
TEXT_DARK   = (18, 18, 22)         # casi negro
TEXT_MID    = (90, 90, 100)        # gris medio
ACCENT_BLUE = (30, 120, 255)       # azul logo
ACCENT_TEAL = (0, 200, 180)        # teal logo
ACCENT_MAG  = (190, 30, 220)       # magenta logo
WHITE       = (255, 255, 255)

# Tamaño 4:5 para feed Instagram
W, H = 1080, 1350

def load_logo(size=60):
    """Carga el logo de Momentum redimensionado."""
    logo = Image.open(f"{ASSETS}/Momentum_isologo color (1).png").convert("RGBA")
    ratio = size / logo.height
    new_w = int(logo.width * ratio)
    return logo.resize((new_w, size), Image.LANCZOS)

def load_ig_icon(size=32):
    """Carga el ícono de Instagram."""
    ig = Image.open(f"{ASSETS}/Instagram_logo_2022.svg.png").convert("RGBA")
    return ig.resize((size, size), Image.LANCZOS)

def gradient_line(draw, x0, y, x1, color1, color2, height=4):
    """Dibuja una línea con degradado horizontal."""
    width = x1 - x0
    for i in range(width):
        t = i / width
        r = int(color1[0] + (color2[0] - color1[0]) * t)
        g = int(color1[1] + (color2[1] - color1[1]) * t)
        b = int(color1[2] + (color2[2] - color1[2]) * t)
        draw.line([(x0 + i, y), (x0 + i, y + height)], fill=(r, g, b))

def draw_footer(img, draw, slide_num, total):
    """Footer: [IG icon] [@hansvilla.ai]  ...  [M logo] [slide_num/total]"""
    ig = load_ig_icon(size=30)

    # Línea divisoria footer
    gradient_line(draw, 60, H - 110, W - 60, ACCENT_BLUE, ACCENT_MAG, height=2)

    ig_y = H - 82
    # IG icon + handle (izquierda)
    img.paste(ig, (60, ig_y + 2), ig)
    f_handle = font("semibold", 26)
    draw.text((60 + ig.width + 10, ig_y + 3), "@hansvilla.ai", font=f_handle, fill=TEXT_MID)

    # Número de slide (derecha)
    f_num = font("bold", 26)
    num_text = f"{slide_num}/{total}"
    nw = draw.textlength(num_text, font=f_num)
    draw.text((W - 60 - nw, ig_y + 3), num_text, font=f_num, fill=TEXT_MID)

    # Logo Momentum a la izquierda del número
    logo = load_logo(size=36)
    logo_x = W - 60 - int(nw) - 14 - logo.width
    img.paste(logo, (logo_x, ig_y + 2), logo)


# ─────────────────────────────────────────────
# SLIDE 1: COVER
# ─────────────────────────────────────────────
def make_cover(title_line1, title_line2, subtitle, filename):
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Elemento decorativo: rectángulo de acento top-left
    gradient_line(draw, 60, 80, 360, ACCENT_BLUE, ACCENT_TEAL, height=6)


    # Logo grande centrado arriba
    logo = load_logo(size=90)
    lx = (W - logo.width) // 2
    img.paste(logo, (lx, 140), logo)

    # Título — dos líneas, Montserrat ExtraBold grande
    f_title = font("extrabold", 90)
    y = 290
    for line in [title_line1, title_line2]:
        tw = draw.textlength(line, font=f_title)
        draw.text(((W - tw) / 2, y), line, font=f_title, fill=TEXT_DARK)
        y += 105

    # Línea acento bajo título
    gradient_line(draw, 60, y + 20, W - 60, ACCENT_TEAL, ACCENT_MAG, height=4)

    # Subtítulo
    f_sub = font("medium", 38)
    sw = draw.textlength(subtitle, font=f_sub)
    draw.text(((W - sw) / 2, y + 50), subtitle, font=f_sub, fill=TEXT_MID)

    # CTA "Desliza →"
    f_cta = font("semibold", 34)
    cta = "Desliza para ver →"
    cw = draw.textlength(cta, font=f_cta)
    # Pill background
    px, py = (W - cw) / 2 - 24, H - 220
    draw.rounded_rectangle([px, py, px + cw + 48, py + 58], radius=29, fill=TEXT_DARK)
    draw.text(((W - cw) / 2, py + 12), cta, font=f_cta, fill=WHITE)

    draw_footer(img, draw, 1, 6)

    path = f"{OUT}/{filename}"
    img.save(path, "PNG")
    print(f"Guardado: {path}")
    return img


# ─────────────────────────────────────────────
# SLIDE 2+: CONTENIDO
# ─────────────────────────────────────────────
def embed_screenshot(img, screenshot_path, y_start, padding=60):
    """Embebe un screenshot con bordes redondeados y sombra sutil."""
    shot = Image.open(screenshot_path).convert("RGBA")

    # Calcular tamaño: ancho máximo = W - 2*padding, alto proporcional
    max_w = W - padding * 2
    max_h = 480
    ratio = min(max_w / shot.width, max_h / shot.height)
    new_w = int(shot.width * ratio)
    new_h = int(shot.height * ratio)
    shot = shot.resize((new_w, new_h), Image.LANCZOS)

    # Sombra (rectángulo gris detrás)
    shadow = Image.new("RGBA", (new_w + 12, new_h + 12), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([6, 6, new_w + 10, new_h + 10], radius=16, fill=(0, 0, 0, 40))
    sx = (W - new_w) // 2
    img_rgba = img.convert("RGBA")
    img_rgba.paste(shadow, (sx - 4, y_start - 4), shadow)

    # Pegar screenshot
    img_rgba.paste(shot, (sx, y_start), shot)
    return img_rgba.convert("RGB"), y_start + new_h + 24


def make_content_slide(step_num, heading, body_lines, filename, slide_pos, total, screenshot_path=None):
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Número de paso — grande, color acento, top-left
    f_step = font("extrabold", 120)
    step_str = f"0{step_num}."
    draw.text((60, 60), step_str, font=f_step, fill=(*ACCENT_BLUE, 30))  # translucent

    # Necesitamos dibujarlo en PIL con alpha
    # Overlay el número con opacidad baja
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.text((55, 55), step_str, font=f_step, fill=(*ACCENT_BLUE, 45))
    img = img.convert("RGBA")
    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)

    draw_top_right_logo(img)
    draw = ImageDraw.Draw(img)

    # Heading
    f_head = font("extrabold", 68)
    y = 210
    # Wrap largo
    words = heading.split()
    lines = []
    current = ""
    for w in words:
        test = (current + " " + w).strip()
        if draw.textlength(test, font=f_head) < W - 120:
            current = test
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    for line in lines:
        draw.text((60, y), line, font=f_head, fill=TEXT_DARK)
        y += 80

    # Línea acento
    gradient_line(draw, 60, y + 16, 300, ACCENT_BLUE, ACCENT_TEAL, height=4)
    y += 50

    # Body
    f_body = font("regular", 40)
    for line in body_lines:
        # Wrap del body
        wrapped = textwrap.wrap(line, width=38)
        for wl in wrapped:
            draw.text((60, y), wl, font=f_body, fill=TEXT_DARK)
            y += 54
        y += 16  # espacio entre puntos

    # Screenshot embebido (opcional)
    if screenshot_path:
        img, y = embed_screenshot(img, screenshot_path, y_start=y + 20)
        draw = ImageDraw.Draw(img)

    draw_footer(img, draw, slide_pos, total)

    path = f"{OUT}/{filename}"
    img.save(path, "PNG")
    print(f"Guardado: {path}")
    return img


# ─────────────────────────────────────────────
# GENERAR CARRUSEL DE PRUEBA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    TOTAL = 6

    make_cover(
        title_line1="Gana $3,000",
        title_line2="extra al mes",
        subtitle="con automatizaciones de IA",
        filename="carousel-01-cover.png"
    )

    make_content_slide(
        step_num=1,
        heading="Elige una tarea repetitiva",
        body_lines=[
            "Algo que hagas más de 3 veces",
            "por semana en tu trabajo.",
            "",
            "Facturación, reportes, emails,",
            "seguimiento de clientes...",
        ],
        filename="carousel-02-paso1.png",
        slide_pos=2, total=TOTAL
    )

    make_content_slide(
        step_num=2,
        heading="Automatízala con n8n",
        body_lines=[
            "n8n conecta tus herramientas",
            "sin escribir código.",
        ],
        filename="carousel-03-paso2.png",
        slide_pos=3, total=TOTAL,
        screenshot_path=f"{OUT}/n8n_2026_b.png"
    )

    print("\nCarrusel generado.")
