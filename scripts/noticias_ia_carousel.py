"""
Skill: noticias-ia-carousel
Genera un carrusel de Instagram con las últimas noticias de IA
para la audiencia de @hansvilla.ai / Momentum AI Academy

Uso:
    python scripts/noticias_ia_carousel.py

Output:
    outputs/noticias/YYYY-MM-DD/ con todos los slides PNG
"""

import argparse, json, os, textwrap, urllib.request, urllib.parse, io, re
from datetime import datetime
from html.parser import HTMLParser
from PIL import Image, ImageDraw, ImageFont
from uploader import publicar_carousel, caption_noticias, slides_en_directorio

# ─── Rutas ───────────────────────────────────────────────────────────────────
BASE   = "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
FONTS  = f"{BASE}/Documentos subidos/Montserrat/static"
ASSETS = f"{BASE}/Documentos subidos"
_cli_today = None  # se sobrescribe por --today si se pasa antes del módulo
TODAY  = datetime.now().strftime("%Y-%m-%d")
OUT    = f"{BASE}/outputs/noticias/{TODAY}"  # se recalcula en main() si --today

# ─── API Keys ─────────────────────────────────────────────────────────────────
def load_env():
    env = {}
    with open(f"{BASE}/.env") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env

ENV = load_env()
PERPLEXITY_KEY = ENV.get("PERPLEXITY_API_KEY", "")
ANTHROPIC_KEY  = ENV.get("ANTHROPIC_API_KEY", "")

# ─── Paleta & Fuentes (igual que gen_carousel.py) ─────────────────────────────
BG          = (252, 251, 249)
TEXT_DARK   = (18, 18, 22)
TEXT_MID    = (90, 90, 100)
TEXT_LIGHT  = (150, 150, 160)
ACCENT_BLUE = (30, 120, 255)
ACCENT_TEAL = (0, 200, 180)
ACCENT_MAG  = (190, 30, 220)
WHITE       = (255, 255, 255)
W, H        = 1080, 1350

def font(weight, size):
    names = {
        "regular":   "Montserrat-Regular.ttf",
        "medium":    "Montserrat-Medium.ttf",
        "semibold":  "Montserrat-SemiBold.ttf",
        "bold":      "Montserrat-Bold.ttf",
        "extrabold": "Montserrat-ExtraBold.ttf",
    }
    return ImageFont.truetype(f"{FONTS}/{names[weight]}", size)

def load_logo(size=56):
    logo = Image.open(f"{ASSETS}/Momentum_isologo color (1).png").convert("RGBA")
    ratio = size / logo.height
    return logo.resize((int(logo.width * ratio), size), Image.LANCZOS)

def load_ig_icon(size=30):
    ig = Image.open(f"{ASSETS}/Instagram_logo_2022.svg.png").convert("RGBA")
    return ig.resize((size, size), Image.LANCZOS)

def gradient_line(draw, x0, y, x1, c1, c2, h=4):
    for i in range(x1 - x0):
        t = i / (x1 - x0)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.line([(x0 + i, y), (x0 + i, y + h)], fill=(r, g, b))

def draw_branding(img, draw, slide_num, total, light=False):
    """Footer: [IG icon] [@hansvilla.ai]  ...  [M logo] [2/6]"""
    txt_color = (160, 160, 180) if light else TEXT_MID
    gradient_line(draw, 60, H - 110, W - 60, ACCENT_BLUE, ACCENT_MAG, 2)
    ig_y = H - 82
    ig = load_ig_icon(30)
    img.paste(ig, (60, ig_y + 2), ig)
    f_h = font("semibold", 26)
    draw.text((60 + ig.width + 10, ig_y + 3), "@hansvilla.ai", font=f_h, fill=txt_color)
    f_n = font("bold", 26)
    num = f"{slide_num}/{total}"
    nw = draw.textlength(num, font=f_n)
    draw.text((W - 60 - nw, ig_y + 3), num, font=f_n, fill=txt_color)
    # Logo Momentum a la izquierda del número
    logo = load_logo(36)
    logo_x = W - 60 - int(nw) - 14 - logo.width
    img.paste(logo, (logo_x, ig_y + 2), logo)

def wrap_text(draw, text, f, max_width):
    """Divide texto en líneas que quepan en max_width."""
    words = text.split()
    lines, current = [], ""
    for w in words:
        test = (current + " " + w).strip()
        if draw.textlength(test, font=f) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines


# ─────────────────────────────────────────────────────────────────────────────
# PASO 1: Buscar noticias con Perplexity
# ─────────────────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """Eres el agente INVESTIGADOR de @hansvilla.ai / Momentum AI Academy.
Tu audiencia es: profesionales LATAM de 25-40 años que usan IA en su día a día
para ser más productivos o ganar dinero extra. NO son empresas ni corporaciones.
Son personas normales que usan ChatGPT, Claude, n8n, herramientas de automatización.

OBJETIVO DE CADA NOTICIA:
Que el lector termine el slide pensando: "Esto lo voy a probar hoy" o
"No sabía que esto existía, lo voy a usar". Si no genera esa reacción, no sirve.

CRITERIOS DE SELECCIÓN — solo estas categorías:
1. NUEVOS MODELOS o actualizaciones importantes: ChatGPT, Claude, Gemini, Grok, Llama.
   Qué cambió, qué pueden hacer ahora que antes no podían.
2. HERRAMIENTAS NUEVAS que cualquier persona puede usar hoy:
   extensiones de navegador, apps, integraciones nuevas de n8n/Make/Zapier,
   funciones nuevas de herramientas conocidas.
3. NUEVOS USOS o casos prácticos virales de IA:
   "Alguien usó Claude para X y ahorró 20 horas", flujos de trabajo nuevos,
   prompts que están cambiando cómo la gente trabaja.
4. CAMBIOS en herramientas que la gente ya usa:
   ChatGPT, Claude, Cursor, Perplexity, Notion AI, etc.

CRITERIOS DE EXCLUSIÓN — NUNCA incluir:
- Noticias de inversiones, valoraciones, financiamiento de empresas de IA
- Estadísticas macro: "la IA moverá X billones", "el 60% de empresas usa IA"
- McKinsey, Deloitte, Gartner, consultoras, informes corporativos
- Regulación, política, leyes sobre IA
- Investigación académica sin aplicación práctica inmediata
- Noticias de hace más de 10 días
- Cosas que suenan interesantes pero no hacen que el lector tome acción

FORMATO DEL RESUMEN:
- Empieza con el hecho concreto: qué lanzaron / qué cambió / qué se puede hacer
- Explica en qué cambia la vida del lector (con ejemplo concreto si es posible)
- Cierra con una acción: "Lo podés probar en..." o "Funciona para..."
- 3-4 oraciones, máximo 90 palabras, sin jerga técnica
- Sin asteriscos, sin markdown, solo texto plano

FORMATO DEL POR_QUE_IMPORTA:
- 1 o 2 oraciones MÁXIMO, 30 palabras máximo
- Habla directo al lector: "Si sos...", "Para vos que...", "Esto significa que..."
- Explica el impacto concreto en su trabajo o ingreso, no en la industria
- Sin asteriscos, sin markdown, solo texto plano

TITULAR: máximo 9 palabras, impactante, en español, sin asteriscos ni markdown.

Responde SOLO con un JSON válido, sin markdown, con esta estructura exacta:
{
  "noticias": [
    {
      "numero": 1,
      "titular": "Titular impactante máximo 9 palabras",
      "resumen": "3-4 oraciones en texto plano sin markdown. Qué pasó, cómo te afecta, qué podés hacer con esto.",
      "por_que_importa": "1-2 oraciones directas al lector. Por qué le cambia algo concreto en su trabajo o su vida.",
      "fuente_nombre": "The Verge",
      "fuente_url": "https://..."
    }
  ]
}
No incluyas el campo imagen_url — lo obtenemos automáticamente del artículo."""

def buscar_noticias():
    print("🔍 Buscando noticias con Perplexity...")
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": f"Dame las 4 noticias más relevantes de IA de los últimos 7 días (hoy es {TODAY}). Busca específicamente: nuevos modelos o actualizaciones de ChatGPT, Claude, Gemini u otros; herramientas nuevas que cualquier persona pueda usar hoy; nuevas funciones de apps conocidas (Cursor, Perplexity, Notion, n8n, etc.); casos de uso prácticos que estén siendo virales. Nada de noticias corporativas, inversiones ni estadísticas macro. IMPORTANTE: Prioriza artículos de texto de The Verge, TechCrunch, Wired, Ars Technica, blogs oficiales de OpenAI/Anthropic/Google, o medios digitales similares. EVITA fuentes de YouTube, TikTok, Twitch u otras plataformas de video — solo artículos web con imagen propia. Asegúrate de que cada noticia provenga de un dominio diferente para que las imágenes sean variadas."}
        ],
        "temperature": 0.3
    }
    req = urllib.request.Request(
        "https://api.perplexity.ai/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {PERPLEXITY_KEY}"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())
    content = data["choices"][0]["message"]["content"]
    # Extraer JSON limpio
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"```\w*\n?", "", content).strip()
    # Extraer solo el bloque JSON (primer { ... último })
    start = content.find("{")
    end   = content.rfind("}") + 1
    if start != -1 and end > start:
        content = content[start:end]
    data = json.loads(content)
    # Limpiar markdown residual de Perplexity en titulares y resúmenes
    for n in data.get("noticias", []):
        n["titular"]        = re.sub(r"\*+", "", n.get("titular", "")).strip()
        n["resumen"]        = re.sub(r"\*+", "", n.get("resumen", "")).strip()
        n["por_que_importa"] = re.sub(r"\*+", "", n.get("por_que_importa", "")).strip()
    return data


# ─────────────────────────────────────────────────────────────────────────────
# PASO 2: Obtener imagen og:image de cada artículo
# ─────────────────────────────────────────────────────────────────────────────
class OGImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og_image = None
    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            attrs_d = dict(attrs)
            if attrs_d.get("property") == "og:image" or attrs_d.get("name") == "og:image":
                self.og_image = attrs_d.get("content")

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"

VIDEO_DOMAINS = ("youtube.com", "youtu.be", "tiktok.com", "vimeo.com", "twitch.tv")

def get_og_image(url):
    """Intenta obtener la og:image de un artículo. Ignora plataformas de video."""
    try:
        domain = urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
        if any(domain == vd or domain.endswith("." + vd) for vd in VIDEO_DOMAINS):
            print(f"  – Omitiendo fuente de video: {domain}")
            return None
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read(50000).decode("utf-8", errors="ignore")
        parser = OGImageParser()
        parser.feed(html)
        return parser.og_image
    except Exception as e:
        print(f"  ⚠ No se pudo obtener og:image de {url}: {e}")
        return None

def descargar_imagen(url, path):
    """Descarga una imagen desde URL y la guarda."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = r.read()
        img = Image.open(io.BytesIO(data)).convert("RGB")
        img.save(path, "PNG")
        return path
    except Exception as e:
        print(f"  ⚠ No se pudo descargar imagen: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# PASO 3: Render de slides
# ─────────────────────────────────────────────────────────────────────────────
def make_cover_noticias(total_slides):
    """Slide 1: Cover semanal."""
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    gradient_line(draw, 60, 80, 380, ACCENT_BLUE, ACCENT_TEAL, 6)

    # Logo centrado
    logo = load_logo(100)
    img.paste(logo, ((W - logo.width) // 2, 130), logo)

    # Etiqueta "SEMANA" pequeña
    f_tag = font("semibold", 30)
    tag = f"NOTICIAS DE IA · {datetime.strptime(TODAY, '%Y-%m-%d').strftime('%d %b %Y').upper()}"
    tw = draw.textlength(tag, font=f_tag)
    draw.text(((W - tw) / 2, 290), tag, font=f_tag, fill=TEXT_LIGHT)

    # Título grande
    f_title = font("extrabold", 88)
    lines = ["LO QUE PASÓ", "EN IA ESTA", "SEMANA"]
    y = 360
    for line in lines:
        tw = draw.textlength(line, font=f_title)
        draw.text(((W - tw) / 2, y), line, font=f_title, fill=TEXT_DARK)
        y += 100

    # Línea acento
    gradient_line(draw, 60, y + 20, W - 60, ACCENT_TEAL, ACCENT_MAG, 4)

    # Subtítulo
    f_sub = font("medium", 36)
    sub = f"{(total_slides - 2) // 2} noticias que te impactan directamente"
    sw = draw.textlength(sub, font=f_sub)
    draw.text(((W - sw) / 2, y + 50), sub, font=f_sub, fill=TEXT_MID)

    # CTA pill
    f_cta = font("semibold", 34)
    cta = "Desliza para leer →"
    cw = draw.textlength(cta, font=f_cta)
    px, py = (W - cw) / 2 - 24, H - 220
    draw.rounded_rectangle([px, py, px + cw + 48, py + 58], radius=29, fill=TEXT_DARK)
    draw.text(((W - cw) / 2, py + 12), cta, font=f_cta, fill=WHITE)

    draw_branding(img, draw, 1, total_slides)
    path = f"{OUT}/slide-01-cover.png"
    img.save(path, "PNG")
    print(f"  ✓ Slide 1 (cover)")
    return img


def make_noticia_slide(noticia, img_path, slide_pos, total_slides):
    """Slide de noticia: imagen + número + titular + resumen + fuente."""
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    y = 60

    # ── Imagen del artículo ──
    if img_path and os.path.exists(img_path):
        try:
            article_img = Image.open(img_path).convert("RGB")
            # Crop centrado a 1080x400
            img_h = 400
            img_w = W
            ratio = max(img_w / article_img.width, img_h / article_img.height)
            new_w = int(article_img.width * ratio)
            new_h = int(article_img.height * ratio)
            article_img = article_img.resize((new_w, new_h), Image.LANCZOS)
            # Recorte centrado
            left = (new_w - img_w) // 2
            top  = (new_h - img_h) // 2
            article_img = article_img.crop((left, top, left + img_w, top + img_h))
            img.paste(article_img, (0, y))
            # Overlay sutil al pie de la imagen
            overlay = Image.new("RGBA", (W, 80), (252, 251, 249, 0))
            for row in range(80):
                alpha = int(255 * (row / 80) ** 1.5)
                for col in range(W):
                    overlay.putpixel((col, row), (*BG, alpha))
            img_rgba = img.convert("RGBA")
            img_rgba.paste(overlay, (0, y + img_h - 80), overlay)
            img = img_rgba.convert("RGB")
            draw = ImageDraw.Draw(img)
            y += img_h + 20
        except Exception as e:
            print(f"  ⚠ Error al pegar imagen: {e}")
            y += 20
    else:
        # Sin imagen: banda decorativa con gradiente + fuente destacada
        band_h = 220
        for row in range(band_h):
            t = row / band_h
            r_val = int(ACCENT_BLUE[0] * (1 - t) + 10 * t)
            g_val = int(ACCENT_BLUE[1] * (1 - t) + ACCENT_TEAL[1] * t)
            b_val = int(ACCENT_BLUE[2] * (1 - t) + ACCENT_TEAL[2] * t)
            # Fade a blanco crema al final
            fade = min(1.0, max(0.0, (row - band_h * 0.75) / (band_h * 0.25)))
            r_val = int(r_val * (1 - fade) + BG[0] * fade)
            g_val = int(g_val * (1 - fade) + BG[1] * fade)
            b_val = int(b_val * (1 - fade) + BG[2] * fade)
            draw.line([(0, y + row), (W, y + row)], fill=(r_val, g_val, b_val))
        # Nombre de fuente sobre la banda
        src_display = noticia.get("fuente_nombre", "") or \
            urllib.parse.urlparse(noticia.get("fuente_url", "")).netloc.replace("www.", "")
        if src_display:
            f_src_big = font("bold", 38)
            sw = draw.textlength(src_display.upper(), font=f_src_big)
            draw.text(((W - sw) / 2, y + 82), src_display.upper(), font=f_src_big, fill=WHITE)
        y += band_h + 10

    # ── Número de noticia ──
    f_num = font("extrabold", 42)
    num_str = f"0{noticia['numero']}."
    draw.rounded_rectangle([60, y, 60 + 90, y + 56], radius=12,
                            fill=ACCENT_BLUE)
    nw = draw.textlength(num_str, font=f_num)
    draw.text((60 + (90 - nw) / 2, y + 8), num_str, font=f_num, fill=WHITE)
    y += 74

    # ── Titular ──
    f_head = font("extrabold", 60)
    head_lines = wrap_text(draw, noticia["titular"], f_head, W - 120)
    for line in head_lines[:3]:
        draw.text((60, y), line, font=f_head, fill=TEXT_DARK)
        y += 70
    y += 8

    # Línea acento corta
    gradient_line(draw, 60, y, 260, ACCENT_BLUE, ACCENT_TEAL, 4)
    y += 22

    # ── Resumen ──
    f_body = font("regular", 36)
    resumen_lines = wrap_text(draw, noticia["resumen"], f_body, W - 120)
    for line in resumen_lines[:6]:  # máximo 6 líneas
        draw.text((60, y), line, font=f_body, fill=TEXT_DARK)
        y += 48
    y += 16

    # ── Tag de fuente ──
    fuente = noticia.get("fuente_nombre", "")
    url_short = urllib.parse.urlparse(noticia.get("fuente_url", "")).netloc.replace("www.", "")
    if fuente or url_short:
        f_src = font("semibold", 26)
        src_text = f"🔗 {fuente}  ·  {url_short}" if fuente and url_short else f"🔗 {fuente or url_short}"
        draw.text((60, y), src_text, font=f_src, fill=TEXT_LIGHT)

    draw_branding(img, draw, slide_pos, total_slides)
    path = f"{OUT}/slide-{slide_pos:02d}-noticia{noticia['numero']}.png"
    img.save(path, "PNG")
    print(f"  ✓ Slide {slide_pos} (noticia {noticia['numero']}: {noticia['titular'][:40]}...)")
    return img


def make_pqi_slide(noticia, slide_pos, total_slides):
    """Slide oscuro dedicado al '¿Por qué te importa?' de cada noticia."""
    img  = Image.new("RGB", (W, H), TEXT_DARK)
    draw = ImageDraw.Draw(img)

    gradient_line(draw, 60, 80, 380, ACCENT_TEAL, ACCENT_BLUE, 6)

    # Número de noticia
    y = 140
    f_num = font("extrabold", 42)
    num_str = f"0{noticia['numero']}."
    draw.rounded_rectangle([60, y, 60 + 90, y + 56], radius=12, fill=ACCENT_TEAL)
    nw = draw.textlength(num_str, font=f_num)
    draw.text((60 + (90 - nw) / 2, y + 8), num_str, font=f_num, fill=TEXT_DARK)
    y += 80

    # Titular pequeño (contexto)
    f_ctx = font("semibold", 30)
    ctx_lines = wrap_text(draw, noticia["titular"], f_ctx, W - 120)
    for line in ctx_lines[:2]:
        draw.text((60, y), line, font=f_ctx, fill=(160, 160, 180))
        y += 38
    y += 30

    # Etiqueta
    f_label = font("semibold", 28)
    draw.text((60, y), "¿POR QUÉ TE IMPORTA?", font=f_label, fill=ACCENT_TEAL)
    y += 50

    gradient_line(draw, 60, y, 340, ACCENT_TEAL, ACCENT_BLUE, 4)
    y += 36

    # Texto grande
    pqi = noticia.get("por_que_importa", "").strip()
    f_pqi = font("extrabold", 62)
    pqi_lines = wrap_text(draw, pqi, f_pqi, W - 120)
    for line in pqi_lines[:5]:
        draw.text((60, y), line, font=f_pqi, fill=WHITE)
        y += 76

    draw_branding(img, draw, slide_pos, total_slides, light=True)
    path = f"{OUT}/slide-{slide_pos:02d}-pqi{noticia['numero']}.png"
    img.save(path, "PNG")
    print(f"  ✓ Slide {slide_pos} (¿por qué? noticia {noticia['numero']})")
    return img


def make_cta_slide(total_slides):
    """Último slide: CTA para seguir y guardar."""
    img  = Image.new("RGB", (W, H), TEXT_DARK)
    draw = ImageDraw.Draw(img)

    # Fondo oscuro con acento
    gradient_line(draw, 60, 80, 380, ACCENT_BLUE, ACCENT_TEAL, 6)

    # Logo centrado
    logo = load_logo(90)
    img.paste(logo, ((W - logo.width) // 2, 160), logo)

    f_big   = font("extrabold", 80)
    f_sub   = font("medium", 38)
    f_small = font("semibold", 32)

    lines_big = ["¿Te sirvió?", "Guarda esto"]
    y = 340
    for line in lines_big:
        tw = draw.textlength(line, font=f_big)
        draw.text(((W - tw) / 2, y), line, font=f_big, fill=WHITE)
        y += 94

    gradient_line(draw, 60, y + 10, W - 60, ACCENT_TEAL, ACCENT_MAG, 4)
    y += 50

    sub = "Cada semana traigo las noticias de IA"
    sub2 = "que más te importan. Sin tecnicismos."
    for s in [sub, sub2]:
        sw = draw.textlength(s, font=f_sub)
        draw.text(((W - sw) / 2, y), s, font=f_sub, fill=(200, 200, 210))
        y += 54

    y += 30
    follow = "→ Seguime en @hansvilla.ai"
    fw = draw.textlength(follow, font=f_small)
    draw.text(((W - fw) / 2, y), follow, font=f_small, fill=ACCENT_TEAL)

    # Footer sobre fondo oscuro
    ig = load_ig_icon(30)
    gradient_line(draw, 60, H - 110, W - 60, ACCENT_BLUE, ACCENT_MAG, 2)
    ig_y = H - 80
    img.paste(ig, (60, ig_y), ig)
    f_handle = font("semibold", 26)
    draw.text((60 + ig.width + 10, ig_y + 1), "@hansvilla.ai", font=f_handle, fill=(160, 160, 180))
    f_n = font("bold", 26)
    num = f"{total_slides}/{total_slides}"
    nw = draw.textlength(num, font=f_n)
    draw.text((W - 60 - nw, ig_y + 1), num, font=f_n, fill=(160, 160, 180))

    path = f"{OUT}/slide-{total_slides:02d}-cta.png"
    img.save(path, "PNG")
    print(f"  ✓ Slide {total_slides} (CTA final)")
    return img


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Genera el carrusel de noticias de IA para @hansvilla.ai"
    )
    parser.add_argument("--publicar", "-p", action="store_true",
                        help="Publica el carrusel en Instagram al terminar")
    parser.add_argument("--fecha",    "-f", default=None,
                        help="Programa la publicación en ISO-8601 (ej: 2026-03-13T09:00:00-06:00). "
                             "Requiere --publicar.")
    parser.add_argument("--caption",  "-c", default=None,
                        help="Caption personalizado. Si se omite, se auto-genera.")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Con --publicar: muestra la info pero no envía la request.")
    parser.add_argument("--today",    "-t", default=None,
                        help="Fecha a mostrar en el carrusel, formato YYYY-MM-DD (ej: 2026-03-13). "
                             "Por defecto usa la fecha actual.")
    parser.add_argument("--skip-fetch", "-s", action="store_true",
                        help="Salta Perplexity y carga el noticias.json existente en la carpeta output.")
    args = parser.parse_args()

    global TODAY, OUT
    if args.today:
        TODAY = args.today
        OUT   = f"{BASE}/outputs/noticias/{TODAY}"
    os.makedirs(OUT, exist_ok=True)

    print(f"\n🚀 Generando carrusel de noticias de IA — {TODAY}\n")

    # 1. Buscar noticias (o cargar JSON existente)
    json_path = f"{OUT}/noticias.json"
    if args.skip_fetch and os.path.exists(json_path):
        print(f"⏭  --skip-fetch: cargando {json_path}\n")
        with open(json_path, encoding="utf-8") as f:
            resultado = json.load(f)
    else:
        resultado = buscar_noticias()
        # Guardar JSON de referencia
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2)
    noticias = resultado["noticias"]
    print(f"✓ {len(noticias)} noticias encontradas\n")

    # 2. Descargar imágenes og:image (sin duplicados por URL ni por dominio)
    print("📷 Descargando imágenes de artículos...")
    img_paths = {}
    used_image_urls = set()
    used_domains    = set()
    for n in noticias:
        num = n["numero"]
        fuente_url = n.get("fuente_url", "")
        # Verificar que el dominio de fuente no se repita (evita og:images idénticas del mismo sitio)
        domain = urllib.parse.urlparse(fuente_url).netloc.lower().replace("www.", "")
        if domain and domain in used_domains:
            print(f"  – Noticia {num}: dominio '{domain}' repetido, se omite imagen")
            img_paths[num] = None
            continue
        if domain:
            used_domains.add(domain)
        # Obtener og:image real del artículo
        img_url = get_og_image(fuente_url) if fuente_url else ""
        # Descartar si ya fue usada en otro slide (mismo CDN / misma imagen)
        if img_url and img_url in used_image_urls:
            print(f"  – Noticia {num}: imagen duplicada (misma URL), se omite")
            img_url = ""
        if img_url:
            used_image_urls.add(img_url)
            local_path = f"{OUT}/img-noticia{num}.png"
            result = descargar_imagen(img_url, local_path)
            img_paths[num] = result
            if result:
                print(f"  ✓ Imagen noticia {num} descargada")
            else:
                img_paths[num] = None
        else:
            img_paths[num] = None
            if fuente_url:
                print(f"  – Noticia {num}: sin imagen disponible")

    # 3. Generar slides
    print("\n🎨 Generando slides...")
    TOTAL = len(noticias) * 2 + 2  # cover + (noticia + pqi) × N + CTA

    make_cover_noticias(TOTAL)

    pos = 2
    for noticia in noticias:
        make_noticia_slide(noticia, img_paths.get(noticia["numero"]), pos, TOTAL)
        pos += 1
        make_pqi_slide(noticia, pos, TOTAL)
        pos += 1

    make_cta_slide(TOTAL)

    print(f"\n✅ Carrusel completo: {TOTAL} slides en {OUT}/\n")

    # 4. Publicar en Instagram (si se pidió)
    if args.publicar:
        cap    = args.caption or caption_noticias(TODAY)
        slides = slides_en_directorio(OUT)
        publicar_carousel(
            slides_paths   = slides,
            caption        = cap,
            scheduled_date = args.fecha,
            dry_run        = args.dry_run,
        )


if __name__ == "__main__":
    main()
