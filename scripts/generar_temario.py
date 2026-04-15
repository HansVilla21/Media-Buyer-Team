"""
Generador de Temario — Momentum AI Academy
Diseño limpio, minimalista, mucho espacio en blanco.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# ─── RUTAS ───────────────────────────────────────────────────────────────────
BASE_DIR = "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
LOGO_PATH = f"{BASE_DIR}/Documentos subidos/Momentum_isologo color (1).png"
OUTPUT_PATH = f"{BASE_DIR}/outputs/temario_momentum_ai_academy.pdf"

# ─── PALETA ──────────────────────────────────────────────────────────────────
C_WHITE    = HexColor("#FFFFFF")
C_BLUE     = HexColor("#1A6FFF")
C_MAGENTA  = HexColor("#CC00FF")
C_BLACK    = HexColor("#111111")
C_GRAY     = HexColor("#6B7280")
C_DIVIDER  = HexColor("#E5E7EB")
C_CARD_BG  = HexColor("#F9FAFB")

# ─── MEDIDAS ─────────────────────────────────────────────────────────────────
W, H = A4  # 595.28 x 841.89 pt
MARGIN_L = 50
MARGIN_R = 50
MARGIN_T = 50
MARGIN_B = 50
CONTENT_W = W - MARGIN_L - MARGIN_R


# ─── HELPERS ─────────────────────────────────────────────────────────────────

def set_font(c, name="Helvetica", size=10, bold=False, italic=False):
    if bold and italic:
        c.setFont(f"{name}-BoldOblique", size)
    elif bold:
        c.setFont(f"{name}-Bold", size)
    elif italic:
        c.setFont(f"{name}-Oblique", size)
    else:
        c.setFont(name, size)


def draw_logo(c, x, y, height):
    """Dibuja el logo centrado en x (usa x como centro horizontal)."""
    img = ImageReader(LOGO_PATH)
    iw, ih = img.getSize()
    ratio = height / ih
    w = iw * ratio
    c.drawImage(LOGO_PATH, x - w / 2, y, width=w, height=height,
                mask="auto", preserveAspectRatio=True)
    return w


def draw_logo_left(c, x, y, height):
    """Dibuja el logo alineado a la izquierda desde x."""
    img = ImageReader(LOGO_PATH)
    iw, ih = img.getSize()
    ratio = height / ih
    w = iw * ratio
    c.drawImage(LOGO_PATH, x, y, width=w, height=height,
                mask="auto", preserveAspectRatio=True)
    return w


def draw_divider(c, y, color=None):
    if color is None:
        color = C_DIVIDER
    c.setStrokeColor(color)
    c.setLineWidth(0.5)
    c.line(MARGIN_L, y, W - MARGIN_R, y)


def draw_header(c, page_num):
    """Header para páginas interiores (2-8)."""
    logo_h = 28
    draw_logo_left(c, MARGIN_L, H - MARGIN_T - logo_h + 4, logo_h)

    # Número de página en esquina derecha
    set_font(c, size=9)
    c.setFillColor(C_GRAY)
    c.drawRightString(W - MARGIN_R, H - MARGIN_T - 10, str(page_num))

    # Línea separadora bajo header
    y_line = H - MARGIN_T - logo_h - 8
    draw_divider(c, y_line)
    return y_line - 16  # cursor debajo del header


def section_label(c, text, x, y):
    """Label estilo 'MÓDULO 1' — azul, 9pt, bold, tracking."""
    set_font(c, size=9, bold=True)
    c.setFillColor(C_BLUE)
    spaced = "  ".join(text)
    c.drawString(x, y, spaced)


def section_title(c, text, x, y, size=18):
    set_font(c, size=size, bold=True)
    c.setFillColor(C_BLACK)
    c.drawString(x, y, text)


def section_desc(c, text, x, y, max_width=None):
    if max_width is None:
        max_width = CONTENT_W
    set_font(c, size=10)
    c.setFillColor(C_GRAY)
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = (current + " " + w).strip()
        if c.stringWidth(test, "Helvetica", 10) <= max_width:
            current = test
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)
    for i, line in enumerate(lines):
        c.drawString(x, y - i * 14, line)
    return y - len(lines) * 14


def draw_card_left_border(c, x, y, w, h, border_color=None):
    """Card con borde izquierdo de color."""
    if border_color is None:
        border_color = C_BLUE
    c.setFillColor(C_CARD_BG)
    c.setStrokeColor(C_DIVIDER)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
    c.setFillColor(border_color)
    c.roundRect(x, y, 3, h, 2, fill=1, stroke=0)


def bullet_list(c, items, x, y, line_h=13):
    """Lista con bullet simple."""
    set_font(c, size=9.5)
    c.setFillColor(C_BLACK)
    for item in items:
        c.drawString(x, y, f"·  {item}")
        y -= line_h
    return y


def wrap_text(c, text, x, y, max_width, font="Helvetica", size=9.5, color=None, line_h=13):
    if color:
        c.setFillColor(color)
    set_font(c, name=font, size=size)
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if c.stringWidth(test, font, size) <= max_width:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    for line in lines:
        c.drawString(x, y, line)
        y -= line_h
    return y


def sub_section(c, title, items, y, x_offset=10, line_h=12):
    """Dibuja una sub-sección con título y bullets en línea."""
    set_font(c, size=9, bold=True)
    c.setFillColor(C_BLACK)
    c.drawString(MARGIN_L + x_offset, y, title)
    y -= 11

    set_font(c, size=8.5)
    c.setFillColor(C_GRAY)
    line = "  ·  ".join(items)
    max_w = CONTENT_W - x_offset - 4
    if c.stringWidth(line, "Helvetica", 8.5) > max_w:
        mid = len(items) // 2
        line1 = "  ·  ".join(items[:mid])
        line2 = "  ·  ".join(items[mid:])
        c.drawString(MARGIN_L + x_offset + 8, y, line1)
        y -= line_h
        c.drawString(MARGIN_L + x_offset + 8, y, line2)
    else:
        c.drawString(MARGIN_L + x_offset + 8, y, line)
    y -= line_h + 3
    return y


# ─── PÁGINA 1: PORTADA ───────────────────────────────────────────────────────

def page_portada(c):
    c.setFillColor(C_WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    logo_h = 135
    center_x = W / 2
    logo_y = H / 2 + 30
    draw_logo(c, center_x, logo_y, logo_h)

    # Nombre academia
    set_font(c, size=28, bold=True)
    c.setFillColor(C_BLACK)
    txt = "Momentum AI Academy"
    tw = c.stringWidth(txt, "Helvetica-Bold", 28)
    c.drawString(center_x - tw / 2, logo_y - 30, txt)

    # Línea separadora
    y_line = logo_y - 46
    draw_divider(c, y_line)

    # Subtítulo
    set_font(c, size=14)
    c.setFillColor(C_GRAY)
    txt2 = "Programa de Estudios"
    tw2 = c.stringWidth(txt2, "Helvetica", 14)
    c.drawString(center_x - tw2 / 2, y_line - 22, txt2)

    # Tagline
    set_font(c, size=11, italic=True)
    c.setFillColor(C_BLUE)
    tag = "Convierte la tecnologia en movimiento"
    tw3 = c.stringWidth(tag, "Helvetica-Oblique", 11)
    c.drawString(center_x - tw3 / 2, y_line - 60, tag)

    # Footer versión
    set_font(c, size=8)
    c.setFillColor(C_DIVIDER)
    c.drawCentredString(center_x, MARGIN_B, "v1.1")

    c.showPage()


# ─── PÁGINA 2: ESTRUCTURA DEL PROGRAMA ──────────────────────────────────────

def page_estructura(c):
    y = draw_header(c, 2)

    section_label(c, "ESTRUCTURA DEL PROGRAMA", MARGIN_L, y)
    y -= 22

    intro = ("Aprende a crear y vender automatizaciones de IA sin programar. "
             "Genera $2,000-$5,000 USD extra al mes ofreciendo soluciones reales a negocios reales.")
    y = wrap_text(c, intro, MARGIN_L, y, CONTENT_W, size=11, color=C_BLACK, line_h=16)
    y -= 20

    col_w = [30, 170, CONTENT_W - 30 - 170 - 10]
    col_x = [MARGIN_L, MARGIN_L + 30, MARGIN_L + 30 + 170]

    row_h = 18
    rows = [
        ("0", "Empieza Aqui", "Orientacion y primeros pasos"),
        ("1", "Fundamentos Tecnicos", "Automatizacion, APIs y Chatbots con IA"),
        ("2", "Construyendo Tu Oferta Vendible", "Nicho, research y empaquetado de servicio"),
        ("3", "Metodologia IMPACT", "Framework propietario de consultoria (6 fases)"),
        ("4", "De Prospecto a Cliente", "Ventas, prospeccion y cierre"),
        ("5", "Implementacion Practica", "Proyectos reales guiados"),
        ("+", "Especializacion ChatGPT & Claude", "Dominio avanzado de LLMs para consultoria"),
        ("+", "Masterizando n8n", "n8n de intermedio a avanzado"),
        ("+", "De 0 a Pro en Airtable", "Bases de datos y automatizacion con Airtable"),
        ("+", "De 0 a Pro en Make", "Automatizacion profesional con Make"),
    ]

    headers = ["#", "Modulo", "Descripcion"]
    set_font(c, size=9)
    c.setFillColor(C_GRAY)
    for i, h in enumerate(headers):
        c.drawString(col_x[i], y, h)
    y -= 6
    draw_divider(c, y)
    y -= row_h

    for idx, (num, mod, desc) in enumerate(rows):
        if idx % 2 == 0:
            c.setFillColor(C_CARD_BG)
            c.rect(MARGIN_L - 4, y - 4, CONTENT_W + 8, row_h, fill=1, stroke=0)

        set_font(c, size=9.5, bold=True)
        c.setFillColor(C_BLUE if num != "+" else C_GRAY)
        c.drawString(col_x[0], y, num)

        set_font(c, size=9.5, bold=(num != "+"))
        c.setFillColor(C_BLACK)
        c.drawString(col_x[1], y, mod)

        set_font(c, size=9)
        c.setFillColor(C_GRAY)
        c.drawString(col_x[2], y, desc)

        y -= row_h
        c.setStrokeColor(C_DIVIDER)
        c.setLineWidth(0.3)
        c.line(MARGIN_L, y + row_h - 14, W - MARGIN_R, y + row_h - 14)

    c.showPage()


# ─── PÁGINA 3: MÓDULOS 0 y 1 ────────────────────────────────────────────────

def module_header(c, label, title, desc, y, max_desc_w=None):
    section_label(c, label, MARGIN_L, y)
    y -= 18
    section_title(c, title, MARGIN_L, y, size=16)
    y -= 16
    y = section_desc(c, desc, MARGIN_L, y, max_width=max_desc_w or CONTENT_W)
    y -= 10
    draw_divider(c, y)
    y -= 14
    return y


def page_modulos_0_1(c):
    y = draw_header(c, 3)

    y = module_header(c, "MODULO 0", "Empieza Aqui",
                      "Orientacion completa para arrancar con claridad desde el primer dia.", y)

    lecciones_0 = [
        "Bienvenidos",
        "Comunidad Momentum AI Academy",
        "Classroom - Modulos y Clases",
        "Soporte y Seccion de Preguntas",
        "Llamadas grupales",
        "Que hago ahora?",
        "Tu primera venta con Automatizaciones",
    ]
    y = bullet_list(c, lecciones_0, MARGIN_L + 10, y, line_h=13)
    y -= 24

    y = module_header(c, "MODULO 1", "Fundamentos Tecnicos",
                      "Base tecnica: automatizacion sin codigo, APIs, webhooks y chatbots con IA.", y)

    secciones_1 = [
        ("Seccion A - Fundamentos de Automatizacion",
         ["Que es automatizacion?", "Tour de n8n", "Conectar Gmail",
          "Sheets-Gmail", "Forms-Telegram", "Tu primera automatizacion"]),
        ("Seccion B - Integraciones API y Webhooks",
         ["Que es una API?", "Que son webhooks?", "Webhook a n8n",
          "Setup VPS", "Instalar n8n en servidor"]),
        ("Seccion C - Chatbots Inteligentes con IA",
         ["Que es un chatbot con IA?", "Prompting efectivo", "ChatGPT a n8n",
          "Chatbot atencion al cliente", "Telegram"]),
        ("Seccion D - Tu propio servidor VPS",
         ["Por que servidor propio?", "Setup completo", "Mantenimiento y monitoreo"]),
    ]

    for sec_title, items in secciones_1:
        y = sub_section(c, sec_title, items, y)
        y -= 4

    c.showPage()


# ─── PÁGINA 4: MÓDULOS 2, 3 y 4 ─────────────────────────────────────────────

def page_modulos_2_3_4(c):
    y = draw_header(c, 4)

    y = module_header(c, "MODULO 2", "Construyendo Tu Oferta Vendible",
                      "El puente entre habilidades tecnicas y monetizacion real.", y)
    items_2 = ["Seleccion de Nicho Estrategica", "Research de Problemas Reales",
               "Disenando la oferta", "Como presentarla"]
    y = bullet_list(c, items_2, MARGIN_L + 10, y, line_h=13)
    y -= 22

    y = module_header(c, "MODULO 3", "Metodologia IMPACT",
                      "Framework propietario construido sobre 150+ implementaciones reales.", y)

    fases = [
        ("I", "Identificar"),
        ("M", "Mapear"),
        ("P", "Priorizar"),
        ("A", "Aplicar"),
        ("C", "Comprobar"),
        ("T", "Transformar"),
    ]
    block_w = CONTENT_W / 6
    bx = MARGIN_L
    for letra, nombre in fases:
        c.setFillColor(C_CARD_BG)
        c.roundRect(bx, y - 22, block_w - 4, 34, 4, fill=1, stroke=0)
        set_font(c, size=16, bold=True)
        c.setFillColor(C_BLUE)
        lw = c.stringWidth(letra, "Helvetica-Bold", 16)
        c.drawString(bx + (block_w - 4) / 2 - lw / 2, y + 4, letra)
        set_font(c, size=7)
        c.setFillColor(C_GRAY)
        nw = c.stringWidth(nombre, "Helvetica", 7)
        c.drawString(bx + (block_w - 4) / 2 - nw / 2, y - 14, nombre)
        bx += block_w

    y -= 34

    fases_lecciones = [
        ("I - Identificar", ["El Framework", "DISCOVERY + ROI"]),
        ("M - Mapear", ["Mapear", "Ejemplo practico", "Framework 4 Preguntas"]),
        ("P - Priorizar", ["Quick Wins", "Matriz 2x2"]),
        ("A - Aplicar", ["Estandares Profesionales", "Error Handling"]),
        ("C - Comprobar", ["Medir Resultados", "Datos para Vender"]),
        ("T - Transformar", ["Especializacion", "Clientes Recurrentes", "Marca Personal"]),
    ]
    for fase_title, items in fases_lecciones:
        set_font(c, size=8.5, bold=True)
        c.setFillColor(C_BLACK)
        c.drawString(MARGIN_L + 10, y, fase_title)
        set_font(c, size=8)
        c.setFillColor(C_GRAY)
        c.drawString(MARGIN_L + 20, y - 11, "  ·  ".join(items))
        y -= 22

    y -= 10

    y = module_header(c, "MODULO 4", "De Prospecto a Cliente",
                      "Todo el ciclo de ventas sin tacticas agresivas.", y)

    items_4 = ["Mentalidad de Negocio", "Entendiendo al Cliente", "Estrategia de Prospeccion",
               "Primer Contacto", "Llamada de Descubrimiento", "Presentacion y Demo",
               "Cierre & Objeciones", "Onboarding"]
    y = bullet_list(c, items_4, MARGIN_L + 10, y, line_h=13)

    c.showPage()


# ─── PÁGINA 5: MÓDULO 5 ──────────────────────────────────────────────────────

def page_modulo_5(c):
    y = draw_header(c, 5)

    y = module_header(c, "MODULO 5", "Implementacion Practica",
                      ("Proyectos reales que podes vender desde el primer dia. "
                       "Cada proyecto es un portfolio piece completo."), y)

    proyectos = [
        ("PROYECTO 1 - Agente de IA",
         ["Introduccion", "Evolution API Setup", "Supabase", "Redis", "Airtable",
          "Agente AI desde 0", "Manychat", "Adaptando al cliente"]),
        ("PROYECTO 2 - Onboarding Automatizado",
         ["Automatizacion del Proceso de Onboarding"]),
        ("PROYECTO 3 - Agendas Automatizadas",
         ["Captura de Leads", "Recordatorios WhatsApp", "Recordatorios por Correo"]),
        ("PROYECTO 4 - Automatizacion en Manychat",
         ["Automatizaciones en ManyChat para Instagram"]),
    ]

    for proy_title, items in proyectos:
        lines_count = 1
        line_str = "  ·  ".join(items)
        max_w = CONTENT_W - 24
        if c.stringWidth(line_str, "Helvetica", 9) > max_w:
            lines_count = 2
        card_h = 14 + lines_count * 13 + 20
        draw_card_left_border(c, MARGIN_L, y - card_h + 8, CONTENT_W, card_h)

        set_font(c, size=10, bold=True)
        c.setFillColor(C_BLUE)
        c.drawString(MARGIN_L + 12, y, proy_title)
        y -= 16

        set_font(c, size=9)
        c.setFillColor(C_GRAY)
        if c.stringWidth(line_str, "Helvetica", 9) > max_w:
            mid = len(items) // 2
            l1 = "  ·  ".join(items[:mid])
            l2 = "  ·  ".join(items[mid:])
            c.drawString(MARGIN_L + 16, y, l1)
            y -= 13
            c.drawString(MARGIN_L + 16, y, l2)
            y -= 13
        else:
            c.drawString(MARGIN_L + 16, y, line_str)
            y -= 13

        y -= 18

    c.showPage()


# ─── PÁGINA 6: Especializaciones ChatGPT & Claude + n8n ──────────────────────

def page_especializaciones(c):
    y = draw_header(c, 6)

    section_label(c, "ESPECIALIZACION", MARGIN_L, y)
    y -= 18
    section_title(c, "Especializacion ChatGPT & Claude", MARGIN_L, y, size=15)
    y -= 14
    y = section_desc(c, "Dominio avanzado de los dos LLMs mas relevantes para consultoria real.", MARGIN_L, y)
    y -= 8
    draw_divider(c, y)
    y -= 14

    secs_chatgpt = [
        ("A - Fundamentos Avanzados de LLMs", ["Leccion 1", "Leccion 2", "Leccion 3"]),
        ("B - Prompting para Consultoria", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("C - GPTs Personalizados", ["Leccion 1", "Leccion 2", "Leccion 3"]),
        ("D - Claude API en n8n", ["Leccion 1", "Leccion 2", "Leccion 3"]),
        ("E - Casos de Negocio Reales", ["Leccion 1", "Leccion 2", "Leccion 3"]),
    ]
    for t, items in secs_chatgpt:
        y = sub_section(c, t, items, y)

    y -= 20

    section_label(c, "ESPECIALIZACION", MARGIN_L, y)
    y -= 18
    section_title(c, "Masterizando n8n", MARGIN_L, y, size=15)
    y -= 14
    y = section_desc(c, "n8n a nivel profesional: workflows complejos y automatizaciones que escalan.", MARGIN_L, y)
    y -= 8
    draw_divider(c, y)
    y -= 14

    secs_n8n = [
        ("A - Repaso y Profundizacion", ["Leccion 1", "Leccion 2", "Leccion 3"]),
        ("B - Nodos Clave", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4", "Leccion 5"]),
        ("C - Workflows de Produccion", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("D - Integraciones Avanzadas", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("E - Escalabilidad y Mantenimiento", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
    ]
    for t, items in secs_n8n:
        y = sub_section(c, t, items, y)

    c.showPage()


# ─── PÁGINA 7: Airtable + Make ───────────────────────────────────────────────

def page_airtable_make(c):
    y = draw_header(c, 7)

    section_label(c, "ESPECIALIZACION", MARGIN_L, y)
    y -= 18
    section_title(c, "De 0 a Pro en Airtable", MARGIN_L, y, size=15)
    y -= 14
    y = section_desc(c, "Bases de datos para clientes, CRMs personalizados y automatizaciones nativas.", MARGIN_L, y)
    y -= 8
    draw_divider(c, y)
    y -= 14

    secs_airtable = [
        ("A - Fundamentos de Airtable", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("B - Diseno de Bases de Datos", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("C - Formularios y Captura de Datos", ["Leccion 1", "Leccion 2", "Leccion 3"]),
        ("D - Automatizaciones Nativas", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("E - Airtable + n8n", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
    ]
    for t, items in secs_airtable:
        y = sub_section(c, t, items, y)

    y -= 20

    section_label(c, "ESPECIALIZACION", MARGIN_L, y)
    y -= 18
    section_title(c, "De 0 a Pro en Make", MARGIN_L, y, size=15)
    y -= 14
    y = section_desc(c, "Make como alternativa profesional a n8n. Ofrece ambas plataformas segun el proyecto.", MARGIN_L, y)
    y -= 8
    draw_divider(c, y)
    y -= 14

    secs_make = [
        ("A - Introduccion a Make", ["Leccion 1", "Leccion 2", "Leccion 3"]),
        ("B - Primeros Escenarios", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("C - Integraciones Clave", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
        ("D - Automatizaciones de Negocio", ["Caso 1", "Caso 2", "Caso 3", "Caso 4"]),
        ("E - Make en Produccion", ["Leccion 1", "Leccion 2", "Leccion 3", "Leccion 4"]),
    ]
    for t, items in secs_make:
        y = sub_section(c, t, items, y)

    c.showPage()


# ─── PÁGINA 8: Informacion del Programa ─────────────────────────────────────

def page_info(c):
    y = draw_header(c, 8)

    logo_h = 60
    draw_logo(c, W / 2, y - logo_h + 4, logo_h)
    y -= logo_h + 20

    set_font(c, size=20, bold=True)
    c.setFillColor(C_BLACK)
    txt = "Informacion del Programa"
    tw = c.stringWidth(txt, "Helvetica-Bold", 20)
    c.drawString(W / 2 - tw / 2, y, txt)
    y -= 30

    datos = [
        ("Precio de contado", "$997 USD (pago unico)"),
        ("Financiamiento", "$100/mes x 12 meses"),
        ("Garantia", "90 dias - devolucion del 100%"),
        ("Modalidad", "100% online, remoto"),
    ]

    card_h = 36
    card_gap = 12
    for label, value in datos:
        c.setFillColor(C_CARD_BG)
        c.setStrokeColor(C_DIVIDER)
        c.setLineWidth(0.5)
        c.roundRect(MARGIN_L, y - card_h + 10, CONTENT_W, card_h, 6, fill=1, stroke=1)
        c.setFillColor(C_BLUE)
        c.roundRect(MARGIN_L, y - card_h + 10, 3, card_h, 2, fill=1, stroke=0)

        set_font(c, size=9)
        c.setFillColor(C_GRAY)
        c.drawString(MARGIN_L + 16, y + 2, label)

        set_font(c, size=11, bold=True)
        c.setFillColor(C_BLACK)
        c.drawString(MARGIN_L + 16, y - 13, value)

        y -= card_h + card_gap

    y -= 16

    garantia = ("Si no generas $2,000-$5,000 USD extra o no quedas conectado a una oportunidad "
                "con ese potencial de ingreso, te devolvemos el 100% del dinero.")
    y = wrap_text(c, garantia, MARGIN_L, y, CONTENT_W, size=9.5, color=C_GRAY, line_h=14)
    y -= 40

    set_font(c, size=16, bold=True)
    c.setFillColor(C_BLUE)
    frase = "Si yo pude, vos tambien podes."
    fw = c.stringWidth(frase, "Helvetica-Bold", 16)
    c.drawString(W / 2 - fw / 2, y, frase)
    y -= 20

    set_font(c, size=10)
    c.setFillColor(C_GRAY)
    attr = "- Hans Villalobos, Momentum AI Academy"
    aw = c.stringWidth(attr, "Helvetica", 10)
    c.drawString(W / 2 - aw / 2, y, attr)

    set_font(c, size=9)
    c.setFillColor(C_DIVIDER)
    fw2 = c.stringWidth("@hansvilla.ai", "Helvetica", 9)
    c.drawString(W / 2 - fw2 / 2, MARGIN_B, "@hansvilla.ai")

    c.showPage()


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    c = canvas.Canvas(OUTPUT_PATH, pagesize=A4)
    c.setTitle("Temario - Momentum AI Academy")
    c.setAuthor("Momentum AI Academy")

    page_portada(c)
    page_estructura(c)
    page_modulos_0_1(c)
    page_modulos_2_3_4(c)
    page_modulo_5(c)
    page_especializaciones(c)
    page_airtable_make(c)
    page_info(c)

    c.save()
    print(f"PDF generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
