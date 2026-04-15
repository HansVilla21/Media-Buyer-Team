"""
Skill: tips-ia-carousel
Genera un carrusel de Instagram con tips prácticos sobre herramientas de IA
para la audiencia de @hansvilla.ai / Momentum AI Academy

── FLUJO RECOMENDADO ────────────────────────────────────────────────────────

  PASO 1: Investigar qué temas le sirven a la audiencia ahora
      python scripts/tips_carousel.py --ideas

      → Devuelve una lista numerada de 8-10 ideas con título sugerido y
        por qué funcionaría. Hans elige uno.

  PASO 2: Generar el carrusel sobre el tema elegido
      python scripts/tips_carousel.py --topic "Claude Code" --cantidad 5
      python scripts/tips_carousel.py --topic "n8n" --titulo "5 automatizaciones para arrancar"

─────────────────────────────────────────────────────────────────────────────
"""

import argparse, json, os, re, io, sys
from datetime import datetime

# Forzar UTF-8 en stdout para compatibilidad con Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw, ImageFont
import urllib.request, urllib.parse
from uploader import publicar_carousel, caption_tips, slides_en_directorio

# ─── Rutas ───────────────────────────────────────────────────────────────────
BASE   = "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
FONTS  = f"{BASE}/Documentos subidos/Montserrat/static"
ASSETS = f"{BASE}/Documentos subidos"
TODAY  = datetime.now().strftime("%Y-%m-%d")

# ─── API Keys ─────────────────────────────────────────────────────────────────
def load_env():
    env = {}
    path = f"{BASE}/.env"
    if not os.path.exists(path):
        return env
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env

ENV            = load_env()
PERPLEXITY_KEY = ENV.get("PERPLEXITY_API_KEY", "")

# ─── Paleta & Constantes ──────────────────────────────────────────────────────
BG          = (252, 251, 249)
TEXT_DARK   = (18, 18, 22)
TEXT_MID    = (90, 90, 100)
TEXT_LIGHT  = (150, 150, 160)
ACCENT_BLUE = (30, 120, 255)
ACCENT_TEAL = (0, 200, 180)
ACCENT_MAG  = (190, 30, 220)
WHITE       = (255, 255, 255)
W, H        = 1080, 1350


# ─── Helpers de render ────────────────────────────────────────────────────────
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

def draw_branding(img, draw, slide_num, total):
    """Footer: [IG icon] [@hansvilla.ai]  ...  [M logo] [2/6]"""
    gradient_line(draw, 60, H - 110, W - 60, ACCENT_BLUE, ACCENT_MAG, 2)
    ig_y = H - 82
    ig = load_ig_icon(30)
    img.paste(ig, (60, ig_y + 2), ig)
    f_h = font("semibold", 26)
    draw.text((60 + ig.width + 10, ig_y + 3), "@hansvilla.ai", font=f_h, fill=TEXT_MID)
    f_n = font("bold", 26)
    num = f"{slide_num}/{total}"
    nw  = draw.textlength(num, font=f_n)
    draw.text((W - 60 - nw, ig_y + 3), num, font=f_n, fill=TEXT_MID)
    logo   = load_logo(36)
    logo_x = W - 60 - int(nw) - 14 - logo.width
    img.paste(logo, (logo_x, ig_y + 2), logo)

def wrap_text(draw, text, f, max_width):
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
# PASO 1: Generar tips con Perplexity
# ─────────────────────────────────────────────────────────────────────────────
SYSTEM_PROMPT_IDEAS = """Eres el agente INVESTIGADOR de @hansvilla.ai / Momentum AI Academy.

La audiencia de Hans son profesionales LATAM de 25-40 años que CASI NO usan IA todavía.
Son empleados, freelancers o emprendedores con trabajo real: contadores, diseñadores,
vendedores, community managers, asistentes, dueños de pymes. NO son desarrolladores.
La mayoría solo conoce ChatGPT de nombre y quizás lo probó una vez.

Los sigue en Instagram porque quieren entender para qué sirve la IA en su vida real,
pero necesitan que les expliquen simple, sin tecnicismos, con ejemplos concretos.

Tu tarea: sugerí exactamente 10 ideas de carruseles de TIPS que Hans debería publicar.

CRITERIOS para cada idea:
1. NIVEL CERO — como si nunca hubieran usado IA antes
2. HERRAMIENTA GRATUITA o muy accesible (ChatGPT gratis, Claude gratis, Gemini, etc.)
3. BENEFICIO CLARO en su trabajo del día a día (ahorrar tiempo, escribir mejor, no olvidar cosas)
4. ACCIONABLE hoy — que puedan probar en 10 minutos con lo que ya tienen
5. SIN JERGA — nada de "agentes", "flujos", "APIs", "tokens", "embeddings", "LLMs"

TEMAS que funcionan para esta audiencia:
- "Cómo usar ChatGPT para [tarea cotidiana del trabajo]"
- "Prompts simples para [resultado concreto]"
- "Cosas que podés pedirle a la IA y la mayoría no sabe"
- "Cómo la IA te ayuda a escribir [emails, propuestas, mensajes de WhatsApp]"
- "Ahorrá tiempo con IA en [tarea tediosa que todos odian]"
- Comparativas simples: "cuándo usar X vs Y" (sin tecnicismos)
- "Tu primer flujo con IA" (los más simples, sin instalar nada)

EVITAR en las ideas:
- Temas para desarrolladores (n8n, APIs, código, automatizaciones complejas)
- Herramientas de pago o muy técnicas (Cursor, Claude Code, edge AI)
- Conceptos abstractos (agentes autónomos, modelos, entrenamiento)
- Cosas que requieren más de 15 minutos para configurar

Respondé SOLO con un JSON válido con exactamente 10 ideas, sin markdown:
{
  "ideas": [
    {
      "numero": 1,
      "tema": "nombre corto del tema (ej: 'ChatGPT para emails')",
      "titulo_sugerido": "Título listo para el carrusel (ej: '5 prompts para escribir emails perfectos con ChatGPT')",
      "por_que": "1-2 oraciones: por qué resuena con alguien que casi no usa IA",
      "tipo": "tips | prompts | flujo | comparativa"
    }
  ]
}"""


def buscar_ideas():
    """Investiga con Perplexity qué temas de tips le sirven a la audiencia ahora."""
    print("🔍 Investigando qué temas necesita tu audiencia...\n")
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_IDEAS},
            {"role": "user", "content": (
                f"Hoy es {TODAY}. Generá exactamente 10 ideas de carruseles de tips de IA para @hansvilla.ai. "
                f"La audiencia son personas que CASI NO usan IA — empleados y freelancers LATAM que conocen "
                f"ChatGPT de nombre pero apenas lo usaron. Necesitan ideas simples, con herramientas gratuitas. "
                f"Considerá: qué preguntas básicas hace la gente que recién empieza con IA, "
                f"qué tareas cotidianas del trabajo se pueden hacer más rápido con IA hoy, "
                f"qué prompts concretos les cambiarían la rutina. "
                f"Incluí variedad: al menos 3 ideas de prompts listos para copiar, "
                f"3 de herramientas gratuitas como ChatGPT/Claude/Gemini, "
                f"2 de tareas cotidianas (emails, reportes, mensajes), "
                f"1 comparativa simple, 1 de ahorro de tiempo. "
                f"Devolvé exactamente 10 ideas numeradas del 1 al 10."
            )}
        ],
        "temperature": 0.6
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
    content = data["choices"][0]["message"]["content"].strip()
    if content.startswith("```"):
        content = re.sub(r"```\w*\n?", "", content).strip()
    start = content.find("{")
    end   = content.rfind("}") + 1
    if start != -1 and end > start:
        content = content[start:end]
    result = json.loads(content)
    for idea in result.get("ideas", []):
        idea["tema"]            = re.sub(r"\*+", "", idea.get("tema", "")).strip()
        idea["titulo_sugerido"] = re.sub(r"\*+", "", idea.get("titulo_sugerido", "")).strip()
        idea["por_que"]         = re.sub(r"\*+", "", idea.get("por_que", "")).strip()
    return result


def imprimir_ideas(resultado):
    """Muestra las ideas de forma legible en la terminal."""
    ideas = resultado.get("ideas", [])
    TIPO_EMOJI = {"tips": "💡", "prompts": "📋", "flujo": "⚙️", "comparativa": "⚡"}

    print("=" * 60)
    print(f"  IDEAS PARA CARRUSEL DE TIPS — {TODAY}")
    print("=" * 60)

    for idea in ideas:
        emoji = TIPO_EMOJI.get(idea.get("tipo", "tips"), "💡")
        print(f"\n  {idea['numero']}. {emoji}  {idea['tema'].upper()}")
        print(f'     "{idea["titulo_sugerido"]}"')
        print(f"     → {idea['por_que']}")

    print("\n" + "=" * 60)
    print("  Para generar un carrusel, ejecutá:")
    print('  python scripts/tips_carousel.py --topic "TEMA" --cantidad 5')
    print("  (podés copiar el título sugerido con --titulo)")
    print("=" * 60 + "\n")

    # Guardar JSON por si se quiere consultar después
    ideas_dir = f"{BASE}/outputs/tips/{TODAY}"
    os.makedirs(ideas_dir, exist_ok=True)
    with open(f"{ideas_dir}/ideas.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print(f"  Lista guardada en: outputs/tips/{TODAY}/ideas.json\n")


SYSTEM_PROMPT_TIPS = """Eres el agente CREADOR de @hansvilla.ai / Momentum AI Academy.

La audiencia son profesionales LATAM de 25-40 años que CASI NO usan IA.
Son empleados, freelancers o emprendedores — contadores, diseñadores, vendedores,
community managers, dueños de pymes. La mayoría conoce ChatGPT pero apenas lo usó.
NO son desarrolladores y nunca van a instalar nada ni tocar código.

Tu trabajo: hacerles sentir que la IA es fácil, útil y para ellos.

OBJETIVO DE CADA TIP:
Que el lector termine el slide pensando: "Esto lo puedo probar ahora mismo."
Si requiere más de 5 minutos para entender o más de 1 herramienta gratuita, es muy complejo.

CRITERIOS PARA CADA TIP:
1. NIVEL CERO — explicalo como si nunca hubieran abierto ChatGPT
2. HERRAMIENTA GRATUITA — ChatGPT gratis, Claude gratis, Gemini, Copilot en Word
3. RESULTADO CLARO — qué van a lograr exactamente (ej: "un email listo en 30 segundos")
4. EN ESPAÑOL LATAM — "podés", "escribí", "abrí", "andá", conversacional
5. CON EJEMPLO CONCRETO — mostrar el antes/después o el prompt exacto

TIPOS DE TIPS VÁLIDOS:
- Prompt listo para copiar y pegar (marcalo con es_prompt: true)
- Caso cotidiano: "Si tenés que escribir X, hacé esto..."
- Truco simple de una herramienta gratuita que poca gente conoce
- Comparación antes/después: cómo lo hacía antes vs con IA
- "Primera vez que..." — ideal para quien nunca probó la herramienta

EVITAR:
- Tecnicismos: "agentes", "flujos", "API", "modelo", "token", "entrenar"
- Herramientas de pago o que requieran instalación
- Pasos que tomen más de 5 minutos en total
- Suposiciones de que ya saben usar la herramienta

FORMATO DEL CUERPO (cuerpo):
- 3-4 oraciones máximo, texto plano
- Empieza con el beneficio: "Con esto podés..." / "La mayoría no sabe que..."
- Incluí números o ejemplos concretos cuando sea posible
- Sin asteriscos, sin markdown, solo texto plano
- Máximo 90 palabras

TITULAR (titulo):
- Máximo 8 palabras
- Empieza con verbo de acción: "Usá...", "Activá...", "Guardá...", "Probá...", "Conectá..."
- Sin markdown ni asteriscos, sin emojis

CLAVE (clave):
- Siempre presente, incluso cuando es_prompt es false
- La frase más importante del tip: el resultado concreto que va a lograr el lector
- Máximo 12 palabras, texto plano, sin verbo introductorio (no "la clave es...")
- Ej: "Un email profesional listo en 30 segundos, sin pensar qué escribir"

PROMPT EJEMPLO (prompt_ejemplo):
- Solo cuando es_prompt: true
- Texto listo para copiar y pegar en la herramienta
- Sin comillas externas ni formato — va a quedar dentro de una caja en el slide

Responde SOLO con un JSON válido, sin markdown, con esta estructura exacta:
{
  "tema": "nombre del tema",
  "titulo_carrusel": "Título del carrusel (ej: '5 tips para usar Claude como un pro')",
  "tips": [
    {
      "numero": 1,
      "titulo": "Título del tip máx 8 palabras",
      "cuerpo": "Explicación práctica en 3-4 oraciones, máx 90 palabras, texto plano.",
      "clave": "El resultado concreto del tip en máx 12 palabras.",
      "es_prompt": false,
      "prompt_ejemplo": null
    },
    {
      "numero": 2,
      "titulo": "Usá este prompt para resumir emails",
      "cuerpo": "La mayoría le pide a Claude 'resumí este email' y obtiene un bloque de texto inútil. Con este prompt obtenés 3 bullets accionables en segundos. Ideal para limpiar la bandeja de entrada cada mañana.",
      "clave": "3 bullets accionables de cualquier email en segundos.",
      "es_prompt": true,
      "prompt_ejemplo": "Resumí este email en 3 puntos: qué me están pidiendo, qué tengo que hacer, y para cuándo. Sé directo y usá lenguaje simple."
    }
  ]
}"""


def buscar_tips(topic, titulo_override, cantidad):
    print(f"💡 Generando {cantidad} tips sobre '{topic}' con Perplexity...")
    titulo_instruccion = (
        f"El título del carrusel debe ser exactamente: '{titulo_override}'."
        if titulo_override else ""
    )
    user_msg = (
        f"Generá {cantidad} tips prácticos y accionables sobre '{topic}' para publicar en Instagram. "
        f"{titulo_instruccion} "
        f"Los tips deben ser cosas que la mayoría de usuarios de {topic} en LATAM NO aprovechan, "
        f"pero que pueden aplicar hoy mismo. "
        f"Incluí al menos 1 tip tipo prompt (es_prompt: true) si aplica al tema. "
        f"Basate en las funciones reales y actuales de {topic}."
    )
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_TIPS},
            {"role": "user",   "content": user_msg}
        ],
        "temperature": 0.5
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
    content = data["choices"][0]["message"]["content"].strip()
    if content.startswith("```"):
        content = re.sub(r"```\w*\n?", "", content).strip()
    start = content.find("{")
    end   = content.rfind("}") + 1
    if start != -1 and end > start:
        content = content[start:end]
    result = json.loads(content)
    # Limpiar markdown residual
    for t in result.get("tips", []):
        t["titulo"]  = re.sub(r"\*+", "", t.get("titulo",  "")).strip()
        t["cuerpo"]  = re.sub(r"\*+", "", t.get("cuerpo",  "")).strip()
        t["clave"]   = re.sub(r"\*+", "", t.get("clave",   "")).strip()
        if t.get("prompt_ejemplo"):
            t["prompt_ejemplo"] = re.sub(r"\*+", "", t["prompt_ejemplo"]).strip()
    return result


# ─────────────────────────────────────────────────────────────────────────────
# PASO 2: Render de slides
# ─────────────────────────────────────────────────────────────────────────────
def make_cover_tips(titulo_carrusel, tema, total_slides, out_dir):
    """Slide 1: Cover con título del carrusel."""
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    gradient_line(draw, 60, 80, 380, ACCENT_BLUE, ACCENT_TEAL, 6)

    # Logo centrado
    logo = load_logo(100)
    img.paste(logo, ((W - logo.width) // 2, 130), logo)

    # Tag "TIPS · [TEMA]"
    f_tag = font("semibold", 28)
    tag   = f"TIPS  ·  {tema.upper()}"
    tw    = draw.textlength(tag, font=f_tag)
    draw.text(((W - tw) / 2, 290), tag, font=f_tag, fill=TEXT_LIGHT)

    # Título grande del carrusel
    f_title     = font("extrabold", 78)
    title_lines = wrap_text(draw, titulo_carrusel.upper(), f_title, W - 120)
    y = 352
    for line in title_lines[:4]:
        tw = draw.textlength(line, font=f_title)
        draw.text(((W - tw) / 2, y), line, font=f_title, fill=TEXT_DARK)
        y += 92

    # Línea acento
    gradient_line(draw, 60, y + 14, W - 60, ACCENT_TEAL, ACCENT_MAG, 4)

    # Subtítulo
    f_sub = font("medium", 34)
    sub   = "Guardá esto para usarlo después"
    sw    = draw.textlength(sub, font=f_sub)
    draw.text(((W - sw) / 2, y + 42), sub, font=f_sub, fill=TEXT_MID)

    # CTA pill
    f_cta = font("semibold", 34)
    cta   = "Deslizá para aprender →"
    cw    = draw.textlength(cta, font=f_cta)
    px, py = (W - cw) / 2 - 24, H - 220
    draw.rounded_rectangle([px, py, px + cw + 48, py + 58], radius=29, fill=TEXT_DARK)
    draw.text(((W - cw) / 2, py + 12), cta, font=f_cta, fill=WHITE)

    draw_branding(img, draw, 1, total_slides)
    path = f"{out_dir}/slide-01-cover.png"
    img.save(path, "PNG")
    print(f"  ✓ Slide 1 (cover)")
    return img


def make_tip_slide(tip, slide_pos, total_slides, out_dir):
    """Slide de tip individual con número decorativo.

    Dos layouts:
      - Con prompt  (es_prompt=True):  body corto + caja PROMPT oscura
      - Sin prompt  (es_prompt=False): body grande + caja CLAVE al fondo
    """
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # ── Número decorativo (watermark de fondo) ──
    f_big_num   = font("extrabold", 200)
    num_str_big = f"0{tip['numero']}"
    big_nw      = int(draw.textlength(num_str_big, font=f_big_num))
    num_layer   = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    nd = ImageDraw.Draw(num_layer)
    nd.text(
        (W - 50 - big_nw, 20), num_str_big,
        font=f_big_num,
        fill=(ACCENT_BLUE[0], ACCENT_BLUE[1], ACCENT_BLUE[2], 18)
    )
    img_rgba = img.convert("RGBA")
    img_rgba.alpha_composite(num_layer)
    img  = img_rgba.convert("RGB")
    draw = ImageDraw.Draw(img)

    y = 60

    # ── Badge de número ──
    f_badge   = font("extrabold", 44)
    badge_txt = f"0{tip['numero']}."
    bw        = int(draw.textlength(badge_txt, font=f_badge))
    draw.rounded_rectangle([60, y, 60 + bw + 28, y + 62], radius=14, fill=ACCENT_BLUE)
    draw.text((74, y + 9), badge_txt, font=f_badge, fill=WHITE)
    y += 82

    # ── Título del tip ──
    f_title     = font("extrabold", 62)
    title_lines = wrap_text(draw, tip["titulo"], f_title, W - 120)
    for line in title_lines[:2]:
        draw.text((60, y), line, font=f_title, fill=TEXT_DARK)
        y += 76
    y += 10

    # Línea acento corta
    gradient_line(draw, 60, y, 280, ACCENT_BLUE, ACCENT_TEAL, 4)
    y += 26

    has_prompt = tip.get("es_prompt") and tip.get("prompt_ejemplo")
    clave      = tip.get("clave", "")

    if has_prompt:
        # ─────────────────────────────────────────────────────────
        # LAYOUT A: body corto (5 líneas) + caja PROMPT oscura
        # ─────────────────────────────────────────────────────────
        f_body     = font("regular", 38)
        body_lines = wrap_text(draw, tip["cuerpo"], f_body, W - 120)
        for line in body_lines[:5]:
            draw.text((60, y), line, font=f_body, fill=TEXT_DARK)
            y += 52
        y += 20

        f_label  = font("semibold", 24)
        f_prompt = font("medium", 30)
        box_x, box_y = 60, y
        box_w        = W - 120
        prompt_lines = wrap_text(
            draw, f'"{tip["prompt_ejemplo"]}"', f_prompt, box_w - 48
        )[:5]
        box_h = 44 + len(prompt_lines) * 42 + 28
        draw.rounded_rectangle(
            [box_x, box_y, box_x + box_w, box_y + box_h],
            radius=16, fill=(22, 22, 30)
        )
        draw.text((box_x + 24, box_y + 14), "PROMPT", font=f_label, fill=ACCENT_TEAL)
        py = box_y + 50
        for line in prompt_lines:
            draw.text((box_x + 24, py), line, font=f_prompt, fill=(215, 215, 228))
            py += 42

    else:
        # ─────────────────────────────────────────────────────────
        # LAYOUT B: body grande (7 líneas) + caja CLAVE al fondo
        # ─────────────────────────────────────────────────────────
        f_body     = font("regular", 44)
        body_lines = wrap_text(draw, tip["cuerpo"], f_body, W - 120)
        for line in body_lines[:7]:
            draw.text((60, y), line, font=f_body, fill=TEXT_DARK)
            y += 60

        if clave:
            # Caja CLAVE — posición fija a ~300px del footer
            f_label = font("semibold", 24)
            f_clave = font("bold", 38)
            box_x   = 60
            box_w   = W - 120
            clave_lines = wrap_text(draw, clave, f_clave, box_w - 56)[:2]
            box_h   = 48 + len(clave_lines) * 50 + 24
            box_y   = H - 130 - box_h  # ancla al footer, sube según contenido

            # Fondo oscuro
            draw.rounded_rectangle(
                [box_x, box_y, box_x + box_w, box_y + box_h],
                radius=16, fill=(18, 24, 38)
            )
            # Borde izquierdo de acento (teal sólido, 5px)
            draw.rounded_rectangle(
                [box_x, box_y, box_x + 5, box_y + box_h],
                radius=3, fill=ACCENT_TEAL
            )
            # Etiqueta
            draw.text((box_x + 24, box_y + 14), "CLAVE", font=f_label, fill=ACCENT_TEAL)
            # Texto clave
            cy = box_y + 50
            for line in clave_lines:
                draw.text((box_x + 24, cy), line, font=f_clave, fill=WHITE)
                cy += 50

    draw_branding(img, draw, slide_pos, total_slides)
    path = f"{out_dir}/slide-{slide_pos:02d}-tip{tip['numero']}.png"
    img.save(path, "PNG")
    print(f"  ✓ Slide {slide_pos} (tip {tip['numero']}: {tip['titulo'][:45]}...)")
    return img


def make_cta_slide(total_slides, out_dir):
    """Último slide: CTA para guardar y seguir."""
    img  = Image.new("RGB", (W, H), TEXT_DARK)
    draw = ImageDraw.Draw(img)

    gradient_line(draw, 60, 80, 380, ACCENT_BLUE, ACCENT_TEAL, 6)

    logo = load_logo(90)
    img.paste(logo, ((W - logo.width) // 2, 160), logo)

    f_big   = font("extrabold", 80)
    f_sub   = font("medium", 38)
    f_small = font("semibold", 32)

    lines_big = ["¿Te sirvió?", "Guardá esto"]
    y = 340
    for line in lines_big:
        tw = draw.textlength(line, font=f_big)
        draw.text(((W - tw) / 2, y), line, font=f_big, fill=WHITE)
        y += 94

    gradient_line(draw, 60, y + 10, W - 60, ACCENT_TEAL, ACCENT_MAG, 4)
    y += 50

    sub  = "Cada semana comparto tips de IA para"
    sub2 = "que trabajés menos y ganés más."
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
    nw  = draw.textlength(num, font=f_n)
    draw.text((W - 60 - nw, ig_y + 1), num, font=f_n, fill=(160, 160, 180))

    path = f"{out_dir}/slide-{total_slides:02d}-cta.png"
    img.save(path, "PNG")
    print(f"  ✓ Slide {total_slides} (CTA final)")
    return img


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Genera un carrusel de tips de IA para @hansvilla.ai"
    )
    parser.add_argument("--ideas",    "-i", action="store_true",
                        help="Investigar y listar ideas de temas antes de elegir")
    parser.add_argument("--topic",    "-t", default="Claude",
                        help="Herramienta o tema (ej: 'Claude', 'n8n', 'Perplexity', 'ChatGPT')")
    parser.add_argument("--titulo",   "-T", default="",
                        help="Título personalizado del carrusel (opcional)")
    parser.add_argument("--cantidad", "-n", type=int, default=5,
                        help="Cantidad de tips: entre 3 y 7 (default: 5)")
    parser.add_argument("--publicar", "-p", action="store_true",
                        help="Publica el carrusel en Instagram al terminar")
    parser.add_argument("--fecha",    "-f", default=None,
                        help="Programa la publicación en ISO-8601 (ej: 2026-03-13T09:00:00-06:00). "
                             "Requiere --publicar.")
    parser.add_argument("--caption",  "-c", default=None,
                        help="Caption personalizado. Si se omite, se auto-genera del título.")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Con --publicar: muestra la info pero no envía la request.")
    parser.add_argument("--json",     "-j", default=None,
                        help="Ruta a un JSON pre-generado. Omite la llamada a Perplexity y "
                             "renderiza directamente con ese contenido.")
    args = parser.parse_args()

    # ── Modo ideas: investigar temas y mostrar lista ──
    if args.ideas:
        resultado = buscar_ideas()
        imprimir_ideas(resultado)
        return

    topic    = args.topic
    titulo   = args.titulo
    cantidad = max(3, min(args.cantidad, 7))

    # Output: outputs/tips/YYYY-MM-DD/[slug]/
    slug    = re.sub(r"[^a-zA-Z0-9]", "-", topic.lower()).strip("-")
    out_dir = f"{BASE}/outputs/tips/{TODAY}/{slug}"
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n🚀 Generando carrusel de tips: '{topic}' — {TODAY}\n")

    # 1. Generar tips (desde JSON pre-aprobado o vía Perplexity)
    if args.json:
        print(f"📂 Usando contenido pre-aprobado desde: {args.json}")
        with open(args.json, encoding="utf-8") as f:
            resultado = json.load(f)
    else:
        resultado = buscar_tips(topic, titulo, cantidad)
    tips            = resultado.get("tips", [])
    titulo_carrusel = resultado.get("titulo_carrusel", f"{cantidad} tips para usar {topic}")
    tema            = resultado.get("tema", topic)
    print(f'✓ {len(tips)} tips listos: "{titulo_carrusel}"\n')

    # Guardar JSON de referencia
    with open(f"{out_dir}/tips.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    # 2. Generar slides
    print("🎨 Generando slides...")
    TOTAL = len(tips) + 2  # cover + tips + CTA

    make_cover_tips(titulo_carrusel, tema, TOTAL, out_dir)

    for i, tip in enumerate(tips, start=2):
        make_tip_slide(tip, i, TOTAL, out_dir)

    make_cta_slide(TOTAL, out_dir)

    print(f"\n✅ Carrusel completo: {TOTAL} slides en {out_dir}/\n")

    # 3. Publicar en Instagram (si se pidió)
    if args.publicar:
        cap    = args.caption or caption_tips(titulo_carrusel)
        slides = slides_en_directorio(out_dir)
        publicar_carousel(
            slides_paths   = slides,
            caption        = cap,
            scheduled_date = args.fecha,
            dry_run        = args.dry_run,
        )


if __name__ == "__main__":
    main()
