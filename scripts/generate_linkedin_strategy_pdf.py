"""
Genera PDF de la estrategia LinkedIn de arranque (Semanas 1-2)
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch, mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)

OUTPUT_PATH = "../outputs/linkedin/2026-04-01_estrategia-arranque-semanas-1-2.pdf"

# Colors
DARK = HexColor("#1a1a2e")
BLUE = HexColor("#0077B5")  # LinkedIn blue
LIGHT_BLUE = HexColor("#E8F4FD")
ACCENT = HexColor("#00A0DC")
GRAY = HexColor("#666666")
LIGHT_GRAY = HexColor("#F5F5F5")
WHITE = HexColor("#FFFFFF")
GREEN = HexColor("#057642")
RED = HexColor("#CC1016")

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    name='DocTitle',
    parent=styles['Title'],
    fontSize=26,
    textColor=DARK,
    spaceAfter=6,
    fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    name='DocSubtitle',
    parent=styles['Normal'],
    fontSize=13,
    textColor=GRAY,
    spaceAfter=20,
    fontName='Helvetica',
))
styles.add(ParagraphStyle(
    name='SectionHead',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=BLUE,
    spaceBefore=24,
    spaceAfter=10,
    fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    name='SubHead',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=DARK,
    spaceBefore=16,
    spaceAfter=8,
    fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    name='SubHead3',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=ACCENT,
    spaceBefore=12,
    spaceAfter=6,
    fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    name='Body',
    parent=styles['Normal'],
    fontSize=10,
    textColor=DARK,
    spaceAfter=6,
    leading=14,
    fontName='Helvetica',
))
styles.add(ParagraphStyle(
    name='BodyBold',
    parent=styles['Normal'],
    fontSize=10,
    textColor=DARK,
    spaceAfter=6,
    leading=14,
    fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    name='BulletCustom',
    parent=styles['Normal'],
    fontSize=10,
    textColor=DARK,
    spaceAfter=4,
    leading=14,
    leftIndent=20,
    fontName='Helvetica',
))
styles.add(ParagraphStyle(
    name='Quote',
    parent=styles['Normal'],
    fontSize=10,
    textColor=GRAY,
    spaceAfter=6,
    leading=14,
    leftIndent=20,
    rightIndent=20,
    fontName='Helvetica-Oblique',
))
styles.add(ParagraphStyle(
    name='Hook',
    parent=styles['Normal'],
    fontSize=10,
    textColor=DARK,
    spaceAfter=4,
    leading=14,
    leftIndent=15,
    borderColor=BLUE,
    borderWidth=2,
    borderPadding=8,
    fontName='Helvetica-Oblique',
    backColor=LIGHT_BLUE,
))
styles.add(ParagraphStyle(
    name='SmallGray',
    parent=styles['Normal'],
    fontSize=9,
    textColor=GRAY,
    spaceAfter=4,
    fontName='Helvetica',
))
styles.add(ParagraphStyle(
    name='Footer',
    parent=styles['Normal'],
    fontSize=8,
    textColor=GRAY,
    fontName='Helvetica',
    alignment=TA_CENTER,
))


def hr():
    return HRFlowable(width="100%", thickness=1, color=HexColor("#DDDDDD"), spaceBefore=8, spaceAfter=8)


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        leftMargin=0.8 * inch,
        rightMargin=0.8 * inch,
    )

    story = []

    # ========== COVER / HEADER ==========
    story.append(Spacer(1, 30))
    story.append(Paragraph("Estrategia LinkedIn", styles['DocTitle']))
    story.append(Paragraph("Arranque Semanas 1-2", styles['DocTitle']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Hans Villalobos | Momentum AI Academy", styles['DocSubtitle']))
    story.append(Paragraph("Fecha: 1 de abril, 2026 | Fase: Fundacion (0 a 500 seguidores)", styles['SmallGray']))
    story.append(hr())
    story.append(Spacer(1, 10))

    # ========== MARCO ESTRATEGICO ==========
    story.append(Paragraph("Marco Estrategico", styles['SectionHead']))
    story.append(Paragraph(
        "El objetivo de estas dos semanas NO es viralidad. Es establecer el patron de Hans "
        "(herramienta + cliente + resultado medible) y provocar que el avatar correcto diga "
        "\"esto me suena\".",
        styles['Body']
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>3 errores que NO puedes cometer:</b>", styles['Body']))
    story.append(Paragraph("1. El post de presentacion generico -- nadie lo lee, el algoritmo no lo amplifica", styles['BulletCustom']))
    story.append(Paragraph("2. Publicar y desaparecer -- la golden hour (60 min post-publicacion) no es opcional", styles['BulletCustom']))
    story.append(Paragraph("3. El 5-5-5 a medias -- sin engagement previo, el primer post sale en frio", styles['BulletCustom']))

    # ========== CALENDARIO ==========
    story.append(PageBreak())
    story.append(Paragraph("Calendario de Posts -- 6 Posts en 2 Semanas", styles['SectionHead']))

    story.append(Paragraph("SEMANA 1", styles['SubHead']))

    # Post 1
    story.append(Paragraph("Martes 8 Abril -- Post #1", styles['SubHead3']))
    post1_data = [
        ['Pilar', 'Proceso Personal / BTS'],
        ['Formato', 'Texto largo (400-500 palabras)'],
        ['Tema', 'El proyecto que estoy construyendo: un CRM custom a $3,000'],
    ]
    t = Table(post1_data, colWidths=[1.3 * inch, 4.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_BLUE),
        ('TEXTCOLOR', (0, 0), (0, -1), BLUE),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Hans describe el proyecto activo -- el CRM que esta construyendo. Problema del cliente, "
        "stack usado (n8n + Claude + Supabase), donde esta hoy. Como llego el cliente (referidos). Sin hype.",
        styles['Body']
    ))
    story.append(Paragraph(
        "\"Esta semana estoy construyendo un CRM desde cero para una empresa con n8n y Claude. "
        "El proyecto vale $3,000. El cliente llego por referidos, no por redes sociales.\"",
        styles['Hook']
    ))
    story.append(Paragraph("CTA: \"Tu empresa todavia lleva el seguimiento de clientes en Excel? Cuentame en comentarios.\"", styles['SmallGray']))

    story.append(Spacer(1, 8))

    # Post 2
    story.append(Paragraph("Jueves 10 Abril -- Post #2", styles['SubHead3']))
    post2_data = [
        ['Pilar', 'POV / Autoridad de Mercado'],
        ['Formato', 'Texto corto/medio (250-350 palabras)'],
        ['Tema', 'Por que los cursos de ChatGPT no van a darte un cliente'],
    ]
    t = Table(post2_data, colWidths=[1.3 * inch, 4.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_BLUE),
        ('TEXTCOLOR', (0, 0), (0, -1), BLUE),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Diferencia entre saber usar ChatGPT y construir sistemas que resuelven problemas de negocio. "
        "Postura clara. Sin atacar a nadie. Respaldado por experiencia propia.",
        styles['Body']
    ))
    story.append(Paragraph(
        "\"Saber usar ChatGPT no te va a dar clientes. Tampoco a mi me lo habria dado, si me hubiera "
        "quedado ahi. La diferencia esta en una capa mas abajo.\"",
        styles['Hook']
    ))
    story.append(Paragraph("CTA: \"Cual es tu stack de IA actual en tu trabajo? Comenta abajo.\"", styles['SmallGray']))

    story.append(Spacer(1, 8))

    # Post 3
    story.append(Paragraph("Sabado 12 Abril -- Post #3", styles['SubHead3']))
    post3_data = [
        ['Pilar', 'Engagement / Diagnostico'],
        ['Formato', 'Poll'],
        ['Tema', 'Cuantas horas semanales perdes en procesos manuales?'],
    ]
    t = Table(post3_data, colWidths=[1.3 * inch, 4.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_BLUE),
        ('TEXTCOLOR', (0, 0), (0, -1), BLUE),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Pregunta sobre el dolor #1 del avatar. Menos competencia en sabado. Genera impresiones amplias "
        "y da datos reales del avatar para ajustar contenido.",
        styles['Body']
    ))
    story.append(Paragraph(
        "Opciones: Menos de 5 / 5-10 / 10-20 / Mas de 20 (y ya ni cuento)",
        styles['SmallGray']
    ))
    story.append(Paragraph("CTA: \"Si votas, contame en comentarios que tarea te consume mas tiempo.\"", styles['SmallGray']))

    # SEMANA 2
    story.append(PageBreak())
    story.append(Paragraph("SEMANA 2", styles['SubHead']))

    # Post 4
    story.append(Paragraph("Martes 15 Abril -- Post #4", styles['SubHead3']))
    post4_data = [
        ['Pilar', 'Educacion Tecnica Aplicada'],
        ['Formato', 'Carrusel PDF (8-10 slides)'],
        ['Tema', '5 automatizaciones con IA que mas se venden en LATAM'],
    ]
    t = Table(post4_data, colWidths=[1.3 * inch, 4.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_BLUE),
        ('TEXTCOLOR', (0, 0), (0, -1), BLUE),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Lista concreta: herramienta, industria, precio tipico. Hans habla desde sus 20+ proyectos. "
        "No teoria -- experiencia directa. El carrusel llega en semana 2 cuando el lector ya tiene contexto.",
        styles['Body']
    ))
    story.append(Paragraph("<b>Estructura de slides:</b>", styles['Body']))
    story.append(Paragraph("Slide 1: Hook (\"5 automatizaciones que venden solas. Las he construido todas.\")", styles['BulletCustom']))
    story.append(Paragraph("Slides 2-6: Una automatizacion por slide (chatbot WhatsApp, CRM, recordatorios, reportes, calificacion de leads)", styles['BulletCustom']))
    story.append(Paragraph("Slide 7: Como llegaron esos clientes (referidos vs. prospeccion)", styles['BulletCustom']))
    story.append(Paragraph("Slide 8: CTA", styles['BulletCustom']))
    story.append(Paragraph(
        "\"5 automatizaciones con IA que empresas en LATAM estan comprando hoy. Las he construido todas.\"",
        styles['Hook']
    ))

    story.append(Spacer(1, 8))

    # Post 5
    story.append(Paragraph("Jueves 17 Abril -- Post #5", styles['SubHead3']))
    post5_data = [
        ['Pilar', 'Prueba Social / Casos Reales'],
        ['Formato', 'Texto largo (historia)'],
        ['Tema', 'Como una clinica automatizo 200+ consultas/mes con n8n'],
    ]
    t = Table(post5_data, colWidths=[1.3 * inch, 4.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_BLUE),
        ('TEXTCOLOR', (0, 0), (0, -1), BLUE),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Caso real de Hans como constructor. Problema (WhatsApp manual), solucion (n8n + Claude + WhatsApp API), "
        "timeline honesto, resultado (200+ consultas/mes). Es el caso mas concreto con numeros verificables.",
        styles['Body']
    ))
    story.append(Paragraph(
        "\"Una clinica de ortodoncia recibia 200+ consultas al mes por WhatsApp. Las respondian manualmente. "
        "En dos semanas les construi un sistema con n8n y Claude que lo hace solo.\"",
        styles['Hook']
    ))

    story.append(Spacer(1, 8))

    # Post 6
    story.append(Paragraph("Sabado 19 Abril -- Post #6", styles['SubHead3']))
    post6_data = [
        ['Pilar', 'Proceso Personal / BTS'],
        ['Formato', 'Texto medio (300-400 palabras)'],
        ['Tema', 'Lo que aprendi dejando un trabajo de $2,000/mes'],
    ]
    t = Table(post6_data, colWidths=[1.3 * inch, 4.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_BLUE),
        ('TEXTCOLOR', (0, 0), (0, -1), BLUE),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Historia de origen contada desde aprendizajes, no drama. Cierra el ciclo conectando con el CRM del Post #1. "
        "Primero accion, despues historia -- el orden importa.",
        styles['Body']
    ))
    story.append(Paragraph(
        "\"Hace un tiempo tenia trabajo estable, $2,000/mes, y tecnicamente todo en orden. "
        "Decidi dejarlo para construir automatizaciones de IA. Lo que nadie me dijo es lo que te voy a contar hoy.\"",
        styles['Hook']
    ))

    # ========== RUTINA DIARIA ==========
    story.append(PageBreak())
    story.append(Paragraph("Rutina Diaria de Engagement", styles['SectionHead']))

    story.append(Paragraph("Dias de publicacion (Mar/Jue/Sab) -- 20-25 min ANTES de publicar", styles['SubHead']))

    steps = [
        ("<b>Paso 1 -- 5 comentarios Tier 1</b> (10K+ seguidores, nicho IA/automatizacion). "
         "Minimo 2-3 oraciones. Perspectiva propia. Nunca \"Excelente post!\" solo."),
        ("<b>Paso 2 -- 5 comentarios peer</b> (500-5K seguidores, mismo nicho). "
         "Buscar con Sales Navigator: Analista de Procesos, Jefe de Operaciones, Ingeniero Industrial."),
        ("<b>Paso 3 -- 5 comentarios avatar target</b> (Sub-avatar 1). "
         "No influencers -- son posibles clientes/alumnos. Tu comentario los lleva a ver tu perfil."),
        ("<b>Paso 4 -- Publicar en horario exacto.</b> Mar/Jue: 8:30-9:30 AM. Sab: 10:00-11:00 AM."),
        ("<b>Paso 5 -- Golden Hour (60 min, OBLIGATORIO).</b> "
         "Responder TODOS los comentarios. Minimo 1-2 oraciones. Preguntar de vuelta."),
    ]
    for s in steps:
        story.append(Paragraph(s, styles['BulletCustom']))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Dias sin publicacion (Lun/Mie/Vie/Dom) -- 10-15 min", styles['SubHead']))
    story.append(Paragraph("3 comentarios de calidad en posts del nicho", styles['BulletCustom']))
    story.append(Paragraph("Responder comentarios tardios de posts anteriores", styles['BulletCustom']))
    story.append(Paragraph("2-3 solicitudes de conexion nuevas desde Sales Navigator", styles['BulletCustom']))

    # ========== CONEXIONES ==========
    story.append(hr())
    story.append(Paragraph("Estrategia de Conexiones: 447 a 500+", styles['SectionHead']))
    story.append(Paragraph("<b>Meta: 3-4 conexiones nuevas por dia. Solo Sub-avatar 1.</b>", styles['Body']))

    story.append(Paragraph("Busqueda en Sales Navigator:", styles['SubHead']))
    sn_items = [
        "<b>Cargos:</b> Ingeniero Industrial, Analista de Procesos, Jefe de Operaciones, Data Analyst, Coordinador de TI",
        "<b>Industrias:</b> Manufactura, Logistica, Servicios financieros, Salud, Retail",
        "<b>Ubicacion:</b> Costa Rica, Colombia, Mexico, Peru, Chile, Argentina",
        "<b>Empresa:</b> 50-500 empleados",
        "<b>Actividad:</b> Activos en los ultimos 30 dias",
    ]
    for item in sn_items:
        story.append(Paragraph(item, styles['BulletCustom']))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Sin mensaje en la solicitud.</b> LinkedIn penaliza mensajes genericos. Conectar sin nota.", styles['Body']))

    story.append(Spacer(1, 8))
    story.append(Paragraph("DM post-conexion (24-48h despues de que acepten):", styles['SubHead3']))
    story.append(Paragraph(
        "\"Hola [Nombre], gracias por conectar. Vi tu perfil y tu trabajo en [cargo/empresa] -- "
        "justo el tipo de contexto donde las automatizaciones con IA estan generando mas impacto hoy. "
        "Estoy publicando contenido sobre esto cada semana. "
        "En tu empresa ya estan usando algo de automatizacion de procesos?\"",
        styles['Quote']
    ))
    story.append(Paragraph("El DM no vende nada. Abre conversacion. Si responden, es senal de calor.", styles['SmallGray']))

    # ========== METRICAS ==========
    story.append(PageBreak())
    story.append(Paragraph("Metricas de Exito -- Primeras 2 Semanas", styles['SectionHead']))

    story.append(Paragraph("Por post:", styles['SubHead']))
    metrics_post = [
        ['Metrica', 'Objetivo'],
        ['Comentarios sustanciosos (2+ oraciones)', '3+ por post'],
        ['Comentarios de Sub-avatar 1', 'Al menos 1 por post'],
        ['Saves / Bookmarks', '3+ por post'],
        ['DMs recibidos', '1+ en 2 semanas'],
    ]
    t = Table(metrics_post, colWidths=[3.5 * inch, 2.3 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
    ]))
    story.append(t)

    story.append(Spacer(1, 12))
    story.append(Paragraph("De cuenta:", styles['SubHead']))
    metrics_account = [
        ['Metrica', 'Objetivo'],
        ['Seguidores al final de semana 2', '500+'],
        ['Engagement rate promedio', '4%+'],
        ['Aceptacion de conexiones', '40%+'],
        ['Respuesta a DM de bienvenida', '20%+'],
    ]
    t = Table(metrics_account, colWidths=[3.5 * inch, 2.3 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
    ]))
    story.append(t)

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "<b>La metrica que manda:</b> Comento alguien del Sub-avatar 1 en los primeros 6 posts? "
        "Un ingeniero, analista o profesional tecnico que dejo un comentario sustancioso -- "
        "eso es exito de fase 1, independientemente del resto de numeros.",
        styles['Body']
    ))

    # ========== REGLAS ==========
    story.append(hr())
    story.append(Paragraph("Reglas de Engagement", styles['SectionHead']))

    story.append(Paragraph("HACER:", styles['SubHead']))
    hacer = [
        "Publicar en horario exacto y quedarse 60 minutos (Golden Hour)",
        "Responder TODOS los comentarios con 1-2 oraciones y pregunta de vuelta",
        "Enviar DM de bienvenida dentro de 48h cuando alguien acepta conexion",
        "Documentar cada DM recibido (es una senal de lead)",
        "Completar el 5-5-5 ANTES de publicar -- si no hay tiempo, posponer 1 hora",
    ]
    for h in hacer:
        story.append(Paragraph(h, styles['BulletCustom']))

    story.append(Spacer(1, 8))
    story.append(Paragraph("NO HACER:", styles['SubHead']))
    no_hacer = [
        "Publicar sin el 5-5-5 previo",
        "Usar engagement bait: \"Comenta SI\", \"Etiqueta a alguien\"",
        "Poner links en el cuerpo del post -- SIEMPRE en primer comentario",
        "Hacer post de presentacion generico (\"Hola, soy Hans y...\")",
        "Conectar a cualquiera para llegar a 500 -- calidad sobre cantidad",
        "Revisar metricas cada hora -- solo una vez por semana, el lunes",
    ]
    for n in no_hacer:
        story.append(Paragraph(n, styles['BulletCustom']))

    # ========== PROXIMOS PASOS ==========
    story.append(hr())
    story.append(Paragraph("Proximos Pasos -- Esta Semana", styles['SectionHead']))

    pasos = [
        "<b>1.</b> Escribir Post #1 (texto BTS del CRM custom) -- borrador ya generado",
        "<b>2.</b> Configurar busquedas en Sales Navigator con los filtros descritos",
        "<b>3.</b> Enviar 10-15 solicitudes de conexion hoy (sin mensaje)",
        "<b>4.</b> Identificar 5 cuentas Tier 1 y 5 peer para el 5-5-5 del martes",
        "<b>5.</b> Lunes 14 abril: primera retro semanal y ajustar semana 2",
    ]
    for p in pasos:
        story.append(Paragraph(p, styles['BulletCustom']))
        story.append(Spacer(1, 4))

    # Footer
    story.append(Spacer(1, 30))
    story.append(hr())
    story.append(Paragraph(
        "Generado por el Media Buyer Team | Momentum AI Academy | 2026",
        styles['Footer']
    ))

    doc.build(story)
    print(f"PDF generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
