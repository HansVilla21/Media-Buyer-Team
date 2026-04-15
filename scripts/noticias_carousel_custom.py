"""
Carrusel de noticias de IA — edición custom
Genera 5 slides PNG con estilo breaking news oscuro para @hansvilla.ai

Paleta: fondo negro #0A0A0F, acento naranja #FF6B00, texto blanco
Formato: 1080x1080px (cuadrado Instagram)
"""

import os
from PIL import Image, ImageDraw, ImageFont

# ─── Rutas ──────────────────────────────────────────────────────────────────
BASE   = "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
FONTS  = f"{BASE}/Documentos subidos/Montserrat/static"
ASSETS = f"{BASE}/Documentos subidos"
OUT    = f"{BASE}/outputs/reels"
os.makedirs(OUT, exist_ok=True)

# ─── Paleta Breaking News ────────────────────────────────────────────────────
BG_DARK    = (10,  10,  15)     # #0A0A0F  — fondo principal
BG_CARD    = (18,  18,  26)     # tarjeta ligeramente más clara
ORANGE     = (255, 107,  0)     # #FF6B00  — acento principal
ORANGE_DIM = (200,  75,  0)     # naranja oscuro para fondos de badge
YELLOW     = (255, 215,  0)     # #FFD700  — acento secundario/highlight
WHITE      = (255, 255, 255)
LIGHT_GRAY = (180, 180, 190)
MID_GRAY   = (110, 110, 120)
RED_ALERT  = (220,  40,  40)    # rojo para "BREAKING"

W, H = 1080, 1080

# ─── Helpers de fuentes ──────────────────────────────────────────────────────
def font(weight, size):
    names = {
        "regular":   "Montserrat-Regular.ttf",
        "medium":    "Montserrat-Medium.ttf",
        "semibold":  "Montserrat-SemiBold.ttf",
        "bold":      "Montserrat-Bold.ttf",
        "extrabold": "Montserrat-ExtraBold.ttf",
        "black":     "Montserrat-Black.ttf",
    }
    return ImageFont.truetype(f"{FONTS}/{names[weight]}", size)

# ─── Helper: wrap de texto ───────────────────────────────────────────────────
def wrap_text(draw, text, fnt, max_width):
    words = text.split()
    lines, current = [], ""
    for w in words:
        test = (current + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines

# ─── Helper: texto centrado ──────────────────────────────────────────────────
def draw_centered(draw, text, fnt, y, color, max_w=W):
    tw = draw.textlength(text, font=fnt)
    x = (max_w - tw) / 2
    draw.text((x, y), text, font=fnt, fill=color)
    return tw

# ─── Helper: línea de acento ─────────────────────────────────────────────────
def accent_line(draw, x0, y, x1, color=ORANGE, thickness=4):
    draw.rectangle([x0, y, x1, y + thickness], fill=color)

# ─── Helper: badge de texto (pill relleno) ───────────────────────────────────
def draw_badge(draw, text, fnt, x, y, bg, fg, radius=8, pad_x=20, pad_y=8):
    tw = draw.textlength(text, font=fnt)
    bw = tw + pad_x * 2
    bh = fnt.size + pad_y * 2
    draw.rounded_rectangle([x, y, x + bw, y + bh], radius=radius, fill=bg)
    draw.text((x + pad_x, y + pad_y), text, font=fnt, fill=fg)
    return bw, bh

# ─── Helper: cargar logo Momentum ────────────────────────────────────────────
def load_logo(height=42):
    logo = Image.open(f"{ASSETS}/Momentum_isologo color (1).png").convert("RGBA")
    ratio = height / logo.height
    return logo.resize((int(logo.width * ratio), height), Image.LANCZOS)

# ─── Helper: handle @hansvilla.ai en esquina inferior derecha ────────────────
def draw_handle(img, draw, slide_num, total):
    # Línea separadora
    accent_line(draw, 54, H - 88, W - 54, ORANGE_DIM, 1)
    f = font("semibold", 24)
    # Handle izquierda
    draw.text((54, H - 66), "@hansvilla.ai", font=f, fill=MID_GRAY)
    # Contador derecha
    counter = f"{slide_num}/{total}"
    cw = draw.textlength(counter, font=f)
    draw.text((W - 54 - cw, H - 66), counter, font=f, fill=MID_GRAY)

# ─── SLIDE 1: PORTADA ────────────────────────────────────────────────────────
def make_slide_01():
    img  = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # ── Barra de alerta superior (BREAKING NEWS style) ──
    draw.rectangle([0, 0, W, 72], fill=ORANGE)
    f_alert = font("black", 30)
    label = "NOTICIAS DE IA  |  JUEVES 13 DE MARZO, 2026"
    lw = draw.textlength(label, font=f_alert)
    draw.text(((W - lw) / 2, 20), label, font=f_alert, fill=BG_DARK)

    # ── Logo Momentum + handle centrados ──
    logo = load_logo(44)
    logo_x = (W - logo.width) // 2
    img.paste(logo, (logo_x, 102), logo)

    f_handle_top = font("semibold", 22)
    hw = draw.textlength("@hansvilla.ai", font=f_handle_top)
    draw.text(((W - hw) / 2, 158), "@hansvilla.ai", font=f_handle_top, fill=MID_GRAY)

    # ── Línea de acento ──
    accent_line(draw, 54, 204, W - 54, ORANGE, 2)

    # ── Título principal ──
    f_main  = font("black", 96)
    f_main2 = font("black", 88)

    title_lines = [
        ("LAS NOTICIAS DE IA", f_main, WHITE),
        ("QUE NO PUEDES", f_main2, WHITE),
        ("IGNORAR",        f_main2, ORANGE),
    ]

    y = 230
    for line, fnt, color in title_lines:
        tw = draw.textlength(line, font=fnt)
        draw.text(((W - tw) / 2, y), line, font=fnt, fill=color)
        y += fnt.size + 14

    # ── Línea decorativa inferior al título ──
    accent_line(draw, 54, y + 12, W - 54, ORANGE, 2)
    y += 36

    # ── Subtítulo ──
    f_sub = font("medium", 38)
    sub = "Esta semana fue intensa"
    sw = draw.textlength(sub, font=f_sub)
    draw.text(((W - sw) / 2, y), sub, font=f_sub, fill=LIGHT_GRAY)
    y += 70

    # ── 3 badges de noticias ──
    badges = [
        "01  GPT-5.4 opera tu computadora sola",
        "02  CEO Anthropic: IA ya reemplaza el 50%",
        "03  85% de empresas LATAM adoptan agentes",
    ]
    f_badge = font("semibold", 26)
    by = y + 10
    for badge in badges:
        bw = draw.textlength(badge, font=f_badge)
        # fondo de card
        padding_h, padding_v = 20, 12
        card_w = int(bw) + padding_h * 2
        card_h = f_badge.size + padding_v * 2
        card_x = (W - card_w) // 2
        draw.rounded_rectangle(
            [card_x, by, card_x + card_w, by + card_h],
            radius=6, fill=BG_CARD
        )
        # punto naranja
        draw.ellipse([card_x + 14, by + card_h // 2 - 5, card_x + 24, by + card_h // 2 + 5],
                     fill=ORANGE)
        draw.text((card_x + padding_h + 4, by + padding_v), badge, font=f_badge, fill=WHITE)
        by += card_h + 10

    # ── CTA pill inferior ──
    f_cta = font("semibold", 30)
    cta_text = "Desliza para leer  →"
    ctw = draw.textlength(cta_text, font=f_cta)
    cx = (W - ctw - 48) // 2
    cy = H - 160
    draw.rounded_rectangle([cx, cy, cx + ctw + 48, cy + 54], radius=27, fill=ORANGE)
    draw.text((cx + 24, cy + 10), cta_text, font=f_cta, fill=BG_DARK)

    draw_handle(img, draw, 1, 5)
    path = f"{OUT}/2026-03-13_noticias-ia-slide-01.png"
    img.save(path, "PNG")
    print(f"  Slide 01 guardado: {path}")
    return path


# ─── SLIDES 2-4: NOTICIAS ────────────────────────────────────────────────────
def make_noticia_slide(num_str, titular, resumen, dato_clave, dato_label,
                       por_que, slide_pos, total, filename):
    img  = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # ── Barra superior naranja ──
    draw.rectangle([0, 0, W, 58], fill=ORANGE)
    f_top = font("black", 24)
    top_label = f"NOTICIA {num_str}  |  @hansvilla.ai"
    tlw = draw.textlength(top_label, font=f_top)
    draw.text(((W - tlw) / 2, 16), top_label, font=f_top, fill=BG_DARK)

    y = 90

    # ── Número grande de fondo (decorativo) ──
    f_bignum = font("black", 220)
    bw = draw.textlength(num_str, font=f_bignum)
    # Dibujado en gris muy oscuro como watermark
    draw.text((W - bw - 30, y - 40), num_str, font=f_bignum,
              fill=(22, 22, 32))

    # ── Titular con auto-fit de tamaño ──
    # Reduce el tamaño de fuente hasta que el titular quepa en 3 líneas
    max_title_w = W - 108
    title_size = 68
    while title_size >= 36:
        f_title = font("black", title_size)
        title_lines = wrap_text(draw, titular.upper(), f_title, max_title_w)
        if len(title_lines) <= 3:
            break
        title_size -= 4

    ty = y
    for line in title_lines[:3]:
        draw.text((54, ty), line, font=f_title, fill=WHITE)
        ty += f_title.size + 8
    y = ty + 18

    # ── Línea acento corta bajo titular ──
    accent_line(draw, 54, y, 54 + 180, ORANGE, 5)
    y += 28

    # ── Resumen ──
    f_body = font("regular", 34)
    body_lines = wrap_text(draw, resumen, f_body, W - 108)
    for line in body_lines[:5]:
        draw.text((54, y), line, font=f_body, fill=LIGHT_GRAY)
        y += f_body.size + 10
    y += 20

    # ── Card de dato clave ──
    card_y = y
    card_h = 148
    card_margin = 54
    draw.rounded_rectangle(
        [card_margin, card_y, W - card_margin, card_y + card_h],
        radius=12, fill=BG_CARD
    )
    # Borde izquierdo naranja
    draw.rounded_rectangle(
        [card_margin, card_y, card_margin + 7, card_y + card_h],
        radius=4, fill=ORANGE
    )
    # Label del dato
    f_label = font("semibold", 22)
    draw.text((card_margin + 28, card_y + 18), dato_label.upper(),
              font=f_label, fill=ORANGE)
    # Dato clave grande
    f_dato = font("black", 54)
    dato_w = draw.textlength(dato_clave, font=f_dato)
    # Si es muy largo, reducir tamaño
    if dato_w > (W - card_margin * 2 - 56):
        f_dato = font("black", 38)
        dato_w = draw.textlength(dato_clave, font=f_dato)
    draw.text((card_margin + 28, card_y + 46), dato_clave, font=f_dato, fill=YELLOW)
    y = card_y + card_h + 24

    # ── "¿Por qué te importa?" ──
    f_why_label = font("bold", 22)
    draw.text((54, y), "POR QUE TE IMPORTA:", font=f_why_label, fill=ORANGE)
    y += 34
    f_why = font("medium", 30)
    why_lines = wrap_text(draw, por_que, f_why, W - 108)
    for line in why_lines[:3]:
        draw.text((54, y), line, font=f_why, fill=LIGHT_GRAY)
        y += f_why.size + 8

    draw_handle(img, draw, slide_pos, total)
    path = f"{OUT}/{filename}"
    img.save(path, "PNG")
    print(f"  Slide {slide_pos:02d} guardado: {path}")
    return path


# ─── SLIDE 5: CIERRE / CTA ───────────────────────────────────────────────────
def make_slide_05():
    img  = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # ── Barra superior ──
    draw.rectangle([0, 0, W, 58], fill=ORANGE)
    f_top = font("black", 24)
    top_label = "MOMENTUM AI ACADEMY  |  @hansvilla.ai"
    tlw = draw.textlength(top_label, font=f_top)
    draw.text(((W - tlw) / 2, 16), top_label, font=f_top, fill=BG_DARK)

    # ── Logo ──
    logo = load_logo(54)
    img.paste(logo, ((W - logo.width) // 2, 100), logo)

    # ── Línea separadora ──
    accent_line(draw, 54, 172, W - 54, ORANGE, 2)

    # ── Pregunta principal (split en 2 colores) ──
    f_q1   = font("black", 76)
    f_q2   = font("black", 68)

    line1 = "\u00bfESTAS DEL LADO DEL QUE"
    line2 = "AUTOMATIZA"
    line3 = "O DEL QUE ES"
    line4 = "AUTOMATIZADO?"

    y = 200

    for text, fnt, color in [
        (line1, f_q2, LIGHT_GRAY),
        (line2, f_q1, ORANGE),
        (line3, f_q2, LIGHT_GRAY),
        (line4, f_q1, WHITE),
    ]:
        tw = draw.textlength(text, font=fnt)
        draw.text(((W - tw) / 2, y), text, font=fnt, fill=color)
        y += fnt.size + 10

    # ── Línea divisora ──
    accent_line(draw, 54, y + 18, W - 54, ORANGE, 2)
    y += 48

    # ── Subtexto ──
    f_sub1 = font("medium", 32)
    f_sub2 = font("bold", 32)
    sub1 = "Aprende a construir automatizaciones de IA"
    sub2 = "Escribe AGENTES al DM  \u2192  @hansvilla.ai"

    for text, fnt, color in [(sub1, f_sub1, LIGHT_GRAY), (sub2, f_sub2, ORANGE)]:
        tw = draw.textlength(text, font=fnt)
        draw.text(((W - tw) / 2, y), text, font=fnt, fill=color)
        y += fnt.size + 14

    # ── CTA pill ──
    y += 20
    f_cta = font("black", 34)
    cta_text = "EMPIEZA ESTA SEMANA"
    ctw = draw.textlength(cta_text, font=f_cta)
    cx = (W - ctw - 64) // 2
    draw.rounded_rectangle([cx, y, cx + ctw + 64, y + 60], radius=30, fill=ORANGE)
    draw.text((cx + 32, y + 12), cta_text, font=f_cta, fill=BG_DARK)

    draw_handle(img, draw, 5, 5)
    path = f"{OUT}/2026-03-13_noticias-ia-slide-05.png"
    img.save(path, "PNG")
    print(f"  Slide 05 guardado: {path}")
    return path


# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    print("\nGenerando carrusel de noticias de IA — 13 marzo 2026\n")

    # Slide 1 — Portada
    make_slide_01()

    # Slide 2 — Noticia 1
    make_noticia_slide(
        num_str    = "01",
        titular    = "La IA ya opera tu computadora sola",
        resumen    = (
            "GPT-5.4 puede leer correos, procesar archivos, actualizar hojas "
            "de calculo y navegar software de forma autonoma, sin que toques "
            "el teclado. OpenAI acaba de demostrarlo en un benchmark real."
        ),
        dato_clave = "83% vs 72.4%",
        dato_label = "Rendimiento GPT-5.4 vs promedio humano",
        por_que    = (
            "Si la IA ya supera al humano en tareas de oficina, quienes "
            "sepan dirigirla van a valer el doble. Los que no, van a competir "
            "contra una maquina que no descansa."
        ),
        slide_pos  = 2,
        total      = 5,
        filename   = "2026-03-13_noticias-ia-slide-02.png",
    )

    # Slide 3 — Noticia 2
    make_noticia_slide(
        num_str    = "02",
        titular    = "CEO Anthropic: IA reemplaza el 50% del trabajo de oficina",
        resumen    = (
            "Dario Amodei declaro que la IA ya reemplaza tareas en el 50% "
            "de empleos de nivel inicial. Abogados, consultores y analistas "
            "financieros son los primeros afectados. No es prediccion: es lo "
            "que esta pasando ahora mismo."
        ),
        dato_clave = "50% de empleos",
        dato_label = "De oficina nivel inicial ya afectados",
        por_que    = (
            "Si trabajas en finanzas, legal o consultoria, esto ya te afecta. "
            "La pregunta no es si va a pasar, sino que vas a hacer con el "
            "tiempo que la IA te va a liberar."
        ),
        slide_pos  = 3,
        total      = 5,
        filename   = "2026-03-13_noticias-ia-slide-03.png",
    )

    # Slide 4 — Noticia 3
    make_noticia_slide(
        num_str    = "03",
        titular    = "85% de empresas en LATAM ya planea contratar agentes de IA",
        resumen    = (
            "El 85% de organizaciones a nivel global planea adoptar agentes "
            "de IA. En LATAM lideran mineria, banca, retail y salud. La "
            "adopcion de sistemas multiagente va a crecer un 67% para 2027. "
            "El mercado ya decidio."
        ),
        dato_clave = "67% de crecimiento",
        dato_label = "En adopcion multiagente para 2027 en LATAM",
        por_que    = (
            "Quien sepa construir agentes de IA en los proximos 12 meses "
            "va a tener mas trabajo del que puede manejar. "
            "El mercado ya lo esta pidiendo."
        ),
        slide_pos  = 4,
        total      = 5,
        filename   = "2026-03-13_noticias-ia-slide-04.png",
    )

    # Slide 5 — Cierre CTA
    make_slide_05()

    print(f"\nCarrusel completo: 5 slides en {OUT}/\n")


if __name__ == "__main__":
    main()
