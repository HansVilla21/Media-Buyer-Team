# Media Buyer Team — Contexto Global

## Qué es este proyecto

Sistema de agentes de IA que actúa como el equipo de marketing, media buying y posicionamiento en LinkedIn de **Hans Villalobos** para **Momentum AI Academy** (`@hansvilla.ai`).

El sistema funciona como un equipo de marketing personal: investiga, crea contenido para Instagram y LinkedIn, escribe guiones, diseña ads, analiza métricas, construye autoridad profesional y mejora la oferta de forma continua.

---

## El Negocio

**Empresa:** Momentum AI Academy
**Fundador:** Hans Villalobos (`@hansvilla.ai` en Instagram)
**Oferta principal:** Academia para aprender a crear y vender automatizaciones de IA, con promesa de $2,000–$5,000 USD extra/mes
**Canales principales:** Instagram (Reels + Stories, 7 posts/semana) + LinkedIn (carruseles + texto, 3 posts/semana)
**Herramienta de edición:** CapCut
**Stack técnico:** n8n, Make, Perplexity, Airtable, Notion, Gemini (imágenes + modelos)
**Mercado:** LATAM, español, profesionales 25–40 años

Archivos de referencia:
- `memory/offer.md` — Oferta completa y detalles de precios
- `memory/avatar.md` — ICP y buyer persona detallado
- `memory/brand-voice.md` — Tono, estilo y voz de marca
- `memory/hans-profile.md` — Perfil de Hans como operador: cómo trabaja, qué lo abruma, cómo responderle

---

## Los Agentes

### Agentes Core (5)

| Agente | Carpeta | Rol |
|--------|---------|-----|
| **COMANDANTE** | `agents/comandante/` | Orquestador. Punto de contacto de Hans. Delega y consolida. |
| **CREADOR** | `agents/creador/` | Guiones de reels, stories, calendarios, posts de LinkedIn. |
| **INVESTIGADOR** | `agents/investigador/` | Research con Perplexity. Tendencias, competidores, noticias. |
| **MEDIA BUYER** | `agents/media-buyer/` | Scripts de ads, análisis de campañas, optimización Meta. |
| **ESTRATEGA** | `agents/estratega/` | Mejora de oferta, posicionamiento, avatar, estrategia mensual. |

### Agentes LinkedIn (6)

| Agente | Archivo | Rol |
|--------|---------|-----|
| **LINKEDIN RESEARCHER** | `.claude/agents/linkedin-researcher.md` | Señales, tendencias y lenguaje del avatar en LinkedIn |
| **LINKEDIN STRATEGIST** | `.claude/agents/linkedin-strategist.md` | Estrategia de posicionamiento y autoridad LinkedIn |
| **LINKEDIN WRITER** | `.claude/agents/linkedin-writer.md` | Posts de LinkedIn en todos los formatos |
| **LINKEDIN EDITOR** | `.claude/agents/linkedin-editor.md` | Quality gate antes de publicar en LinkedIn |
| **LINKEDIN ANALYST** | `.claude/agents/linkedin-analyst.md` | Retros semanales y mapeo de leads |
| **LINKEDIN PROFILE OPTIMIZER** | `.claude/agents/linkedin-profile-optimizer.md` | Auditoría y optimización de perfil |

Cada agente core tiene su propio `CLAUDE.md` en su carpeta. Los agentes LinkedIn viven en `.claude/agents/`.

---

## Sistema de Memoria

Todos los agentes **leen** la carpeta `memory/` al inicio de cada tarea y **escriben** en ella cuando aprenden algo nuevo o cuando Hans confirma que algo funcionó.

```
memory/
├── hans-profile.md      ← Perfil de Hans como operador: cómo trabaja, preferencias de interacción, red flags
├── brand-voice.md       ← Tono, frases, estilo de Hans (para contenido público)
├── offer.md             ← Oferta actual con todos los detalles
├── avatar.md            ← ICP / buyer persona detallado
├── winning-content.md   ← Contenido que funcionó + por qué
└── learnings.md         ← Aprendizajes acumulados del sistema
```

**Regla de escritura en memoria:** Solo agregar información confirmada por Hans o validada por resultados reales. No especular.

---

## Sistema de Skills

Las skills viven en `.agent/skills/<nombre-del-skill>/SKILL.md`.

Los agentes **pueden y deben** crear nuevas skills, editar las existentes y proponer mejoras cuando detectan un patrón repetible. El skill `creador-de-skills` documenta el estándar de formato.

```
.agent/skills/
├── creador-de-skills/SKILL.md       ← Cómo crear nuevas skills
├── contenido/                        ← Skills de contenido (IG + LinkedIn base)
├── ads/                              ← Skills de ads
├── investigacion/                    ← Skills de investigación
├── oferta/                           ← Skills de oferta/estrategia
└── linkedin/                         ← Skills especializados de LinkedIn
    ├── profile-optimizer/SKILL.md    ← Auditoría y optimización de perfil
    ├── authority-builder/SKILL.md    ← Estrategia de posicionamiento y pilares
    ├── signal-researcher/SKILL.md    ← Detección de señales y tendencias
    ├── post-writer/SKILL.md          ← Creación de posts por formato
    ├── comment-engine/SKILL.md       ← Comentarios estratégicos (método 5-5-5)
    ├── retro-analyst/SKILL.md        ← Análisis semanal de resultados + KPIs de señales
    ├── lead-opportunity-mapper/SKILL.md ← Scoring y mapeo de leads
    ├── voice-calibrator/SKILL.md     ← Calibración de voz del founder
    ├── signal-detector/SKILL.md      ← Rutina semanal de detección de señales de interés
    ├── icp-mapper/SKILL.md           ← Listas de cuentas target por tier (alimenta método 5-5-5)
    ├── warm-outreach/SKILL.md        ← Templates de DM para contacto cálido (solo warm, nunca cold)
    └── message-fit-tester/SKILL.md   ← A/B testing de ángulos de contenido (3 ángulos, 3 semanas)
```

**Cuándo crear una skill nueva:**
- Hans repite el mismo tipo de pedido más de 2 veces
- Se descubre una fórmula que produce buenos resultados
- Se identifica un proceso que puede estandarizarse

---

## Convenciones del Sistema

**Idioma:** Todo en español siempre — prompts, outputs, memoria, skills, documentación.

**Formato de outputs:** El agente decide el mejor formato según el contexto. Aprende las preferencias de Hans a través de feedback y las registra en `memory/learnings.md`.

**Flujo de trabajo estándar:**
1. Hans habla con el COMANDANTE
2. COMANDANTE lee contexto en `memory/`
3. COMANDANTE delega a agente(s) especializado(s)
4. Los agentes consultan skills relevantes en `.agent/skills/`
5. Los agentes producen output y lo guardan en `outputs/`
6. Si el output es validado por Hans, actualizan `memory/`

**Autonomía:**
- **Ejecutar directamente:** Crear guiones, calendarios, scripts de ads, investigación, posts de LinkedIn, comentarios
- **Sugerir y esperar confirmación:** Cambios en estrategia, edición de oferta, nueva estructura de campaña, activación de LinkedIn Ads

---

## Módulo LinkedIn

LinkedIn complementa Instagram — NO lo replica. Instagram captura audiencia amplia; LinkedIn construye autoridad técnica y genera leads B2B del Sub-avatar 1.

**Documentación de referencia:**
- `docs/linkedin-strategy.md` — Estrategia completa, pilares, cadencia, fases de crecimiento
- `docs/linkedin-voice.md` — Voice guide para LinkedIn
- `docs/linkedin-content-pillars.md` — Los 5 pilares detallados con ejemplos
- `docs/linkedin-metrics-and-review.md` — Métricas, retros, scoring de leads
- `docs/linkedin-icp-tiers.md` — Listas de cuentas target por tier (1-influencers, 2-peers, 3-avatar)
- `docs/linkedin-lead-signals.md` — Catálogo de señales de interés y qué hacer con cada una
- `docs/linkedin-warm-outreach-playbook.md` — Playbook de outreach no-frío: cuándo, cómo, qué decir

**Skills LinkedIn (en `.agent/skills/linkedin/`):**
- `profile-optimizer` — Audita y reescribe perfil (con framework "perfil como landing page")
- `authority-builder` — Define estrategia de posicionamiento
- `signal-researcher` — Detecta señales y tendencias de mercado
- `signal-detector` — Rutina semanal de detección de señales de interés individual
- `post-writer` — Crea posts por formato con guardrails
- `comment-engine` — Genera comentarios estratégicos (método 5-5-5)
- `retro-analyst` — Análisis semanal de resultados + KPIs de señales
- `lead-opportunity-mapper` — Scoring y mapeo de oportunidades
- `voice-calibrator` — Calibración de voz del founder
- `icp-mapper` — Listas de cuentas target por tier (alimenta método 5-5-5)
- `warm-outreach` — Templates de DM para contacto cálido (solo warm, nunca cold)
- `message-fit-tester` — A/B testing de ángulos de contenido

**Reglas estratégicas LinkedIn:**
1. Frecuencia: 3 posts/semana (Martes, Jueves, Sábado)
2. Formato rey: Carrusel PDF (21.77% engagement)
3. Golden hour: responder TODOS los comentarios en los primeros 60 min
4. Links siempre en primer comentario, NUNCA en el cuerpo del post
5. Método 5-5-5 de engagement antes de publicar
6. Regla 80/20: 80% valor educativo, 20% indirecto sobre academia
7. No monetizar prematuramente — LinkedIn penaliza venta directa
8. Todo contenido debe pasar por el editor (linkedin-editor) antes de publicar
9. No cross-postear entre Instagram y LinkedIn — adaptar siempre

---

## Estructura del Proyecto

```
Media Buyer Team/
├── CLAUDE.md                    ← Este archivo
├── README.md                    ← Guía de uso y comandos de terminal
├── ARCHITECTURE.md              ← Arquitectura detallada
├── .env                         ← Variables de entorno (NO subir a Git)
├── .env.example                 ← Template de variables
│
├── .agent/
│   └── skills/
│       └── creador-de-skills/
│           └── SKILL.md
│
├── agents/
│   ├── comandante/CLAUDE.md
│   ├── creador/CLAUDE.md
│   ├── investigador/CLAUDE.md
│   ├── media-buyer/CLAUDE.md
│   └── estratega/CLAUDE.md
│
├── memory/
│   ├── brand-voice.md
│   ├── offer.md
│   ├── avatar.md
│   ├── winning-content.md
│   └── learnings.md
│
├── templates/
│   ├── reel-script.md
│   ├── story-sequence.md
│   ├── ad-script.md
│   └── content-calendar.md
│
├── inputs/
│   ├── ideas/
│   ├── ad-data/
│   └── references/
│
├── docs/
│   ├── linkedin-strategy.md          ← Estrategia LinkedIn completa
│   ├── linkedin-voice.md             ← Voice guide para LinkedIn
│   ├── linkedin-content-pillars.md   ← Pilares de contenido detallados
│   └── linkedin-metrics-and-review.md ← Métricas, retros y scoring de leads
│
└── outputs/
    ├── reels/
    ├── stories/
    ├── calendars/
    ├── ads/
    ├── research/
    └── linkedin/                      ← Posts, retros, auditorías, lead maps
        └── ejemplos/                  ← Ejemplos de referencia
```

---

## Variables de Entorno Requeridas

Ver `.env.example` para la lista completa. Las más críticas:
- `ANTHROPIC_API_KEY` — Para los agentes Claude
- `PERPLEXITY_API_KEY` — Para el INVESTIGADOR (búsquedas en tiempo real)
- `GEMINI_API_KEY` — Para generación de imágenes y modelos Gemini

## APIs Disponibles y Cuándo Usarlas

| API | Variable | Cuándo usarla |
|-----|----------|---------------|
| Anthropic Claude | `ANTHROPIC_API_KEY` | Motor de todos los agentes |
| Perplexity Sonar Pro | `PERPLEXITY_API_KEY` | Research y búsquedas en tiempo real (INVESTIGADOR) |
| Google Gemini / Imagen | `GEMINI_API_KEY` | Generación de imágenes para ads y contenido; análisis visual; tareas donde Gemini complementa a Claude |

### Cómo usar Gemini desde los agentes

**Endpoint:** `https://generativelanguage.googleapis.com/v1beta/models/`

**Modelos disponibles con esta key:**
- `gemini-2.0-flash` — Rápido y eficiente, bueno para texto complementario
- `gemini-2.0-pro` — Análisis profundo, razonamiento complejo
- `imagen-3.0-generate-002` — Generación de imágenes (covers, thumbnails, referencias visuales para ads)

**Cuándo el CREADOR o MEDIA BUYER deben usar Gemini:**
- Generar imagen de referencia para un ad (brief visual para Hans o para pasar a diseñador)
- Analizar una captura de pantalla de un ad de competidor
- Generar variantes de thumbnails o covers de stories
- Cuando se necesite un segundo modelo para contrastar ideas de copy
