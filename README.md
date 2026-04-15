# Media Buyer Team — Momentum AI Academy

Sistema de agentes de IA que actúa como el equipo de marketing y media buying de Hans Villalobos para `@hansvilla.ai`.

---

## Qué hace este sistema

- Genera guiones de reels y secuencias de stories en la voz de Hans
- Crea calendarios de contenido mensuales listos para ejecutar
- Investiga tendencias de IA y automatización en LATAM con Perplexity
- Escribe y analiza scripts de ads para Meta (Facebook/Instagram)
- Mejora la oferta, el posicionamiento y la estrategia de marketing
- Aprende con el tiempo: crea y actualiza skills conforme trabaja

---

## Requisitos Previos

- [Claude Code](https://claude.ai/code) instalado (`npm install -g @anthropic-ai/claude-code` o el instalador de Windows)
- Una cuenta de Anthropic con API key activa
- Una cuenta de Perplexity con API key activa
- Node.js 18+ (para Claude Code)

---

## Configuración Inicial

### 1. Clonar / abrir el proyecto

Abre la terminal en la carpeta del proyecto:
```bash
cd "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
```

### 2. Configurar variables de entorno

```bash
# Copia el template
cp .env.example .env

# Abre .env y llena los valores reales
# ANTHROPIC_API_KEY=sk-ant-...
# PERPLEXITY_API_KEY=pplx-...
```

### 3. Iniciar Claude Code en el proyecto

```bash
claude
```

Claude Code leerá automáticamente el `CLAUDE.md` de la raíz y tendrá el contexto completo del proyecto.

---

## Crear los Agentes (en este orden)

Ejecuta estos comandos en la terminal **desde la carpeta raíz del proyecto**:

### Agente 1: COMANDANTE (créalo primero)

```bash
claude --agent comandante
```

O desde dentro de Claude Code:
```
/agent create --name comandante --dir agents/comandante
```

**Qué hace:** Orquestador principal. Es el único agente con quien hablas directamente.

---

### Agente 2: CREADOR (prioridad inmediata)

```bash
claude --agent creador
```

O:
```
/agent create --name creador --dir agents/creador
```

**Qué hace:** Guiones de reels, stories, calendarios de contenido.

---

### Agente 3: INVESTIGADOR

```bash
claude --agent investigador
```

O:
```
/agent create --name investigador --dir agents/investigador
```

**Qué hace:** Research en tiempo real con Perplexity. Alimenta al CREADOR y MEDIA BUYER.

---

### Agente 4: MEDIA BUYER

```bash
claude --agent media-buyer
```

O:
```
/agent create --name media-buyer --dir agents/media-buyer
```

**Qué hace:** Scripts de ads, análisis de campañas Meta, optimización.

---

### Agente 5: ESTRATEGA

```bash
claude --agent estratega
```

O:
```
/agent create --name estratega --dir agents/estratega
```

**Qué hace:** Mejora de oferta, posicionamiento, estrategia mensual.

---

## Cómo Usar el Sistema en el Día a Día

### Flujo más simple — hablar con el COMANDANTE

```bash
# Abrir Claude Code en el proyecto
claude

# El COMANDANTE ya tiene contexto de todo. Ejemplos de pedidos:
```

**Pedidos de ejemplo:**

```
"Necesito 3 guiones de reels para esta semana, enfocados en demos de automatizaciones"

"Investiga qué tendencias de IA están viral esta semana en LATAM y dame 5 ideas de contenido"

"Analiza estos datos de mis ads y dime qué pausar, escalar o cambiar: [pegar datos de Meta]"

"Crea el calendario de contenido para abril"

"¿Cómo puedo mejorar mi oferta? Identifica los puntos débiles"
```

---

## Estructura del Proyecto

```
Media Buyer Team/
├── CLAUDE.md                    ← Contexto global (todos los agentes lo leen)
├── README.md                    ← Este archivo
├── ARCHITECTURE.md              ← Arquitectura técnica detallada
├── .env                         ← Variables de entorno (NO subir a Git)
├── .env.example                 ← Template de variables
│
├── .agent/
│   └── skills/
│       └── creador-de-skills/   ← Skill para crear nuevas skills
│           └── SKILL.md
│
├── agents/                      ← Un CLAUDE.md por agente
│   ├── comandante/CLAUDE.md     ← Orquestador principal
│   ├── creador/CLAUDE.md        ← Contenido (reels, stories, calendarios)
│   ├── investigador/CLAUDE.md   ← Research con Perplexity
│   ├── media-buyer/CLAUDE.md    ← Publicidad paga (Meta Ads)
│   └── estratega/CLAUDE.md      ← Estrategia y mejora de oferta
│
├── memory/                      ← Cerebro compartido (todos leen/escriben)
│   ├── brand-voice.md           ← Tono y estilo de Hans
│   ├── offer.md                 ← Oferta actual completa
│   ├── avatar.md                ← ICP / buyer persona
│   ├── winning-content.md       ← Contenido que funcionó
│   └── learnings.md             ← Aprendizajes del sistema
│
├── templates/                   ← Moldes base para los outputs
│   ├── reel-script.md
│   ├── story-sequence.md
│   ├── ad-script.md
│   └── content-calendar.md
│
├── inputs/                      ← Lo que tú le das al sistema
│   ├── ideas/                   ← Ideas crudas que quieres desarrollar
│   ├── ad-data/                 ← Métricas de Meta Ads (copy/paste)
│   └── references/              ← Contenido de referencia o inspiración
│
└── outputs/                     ← Lo que el sistema produce
    ├── reels/                   ← Guiones de reels
    ├── stories/                 ← Secuencias de stories
    ├── calendars/               ← Calendarios de contenido
    ├── ads/
    │   ├── scripts/             ← Scripts de ads
    │   └── analysis/            ← Análisis de campañas
    ├── research/                ← Reportes de investigación
    └── strategy/                ← Análisis estratégicos
```

---

## El Sistema de Skills

Las skills son capacidades estandarizadas que los agentes crean y mejoran solos.

Viven en: `.agent/skills/<nombre-del-skill>/SKILL.md`

El skill `creador-de-skills` ya está instalado. Los agentes lo usarán para crear nuevas skills cuando detecten patrones repetibles en tu forma de trabajar.

**Puedes pedirle al COMANDANTE:**
```
"Crea una skill para generar hooks virales de reels"
"Mejora la skill de guiones de demos"
"¿Qué skills tenemos actualmente?"
```

---

## Variables de Entorno

| Variable | Requerida | Descripción |
|----------|-----------|-------------|
| `ANTHROPIC_API_KEY` | Sí | Para todos los agentes Claude |
| `PERPLEXITY_API_KEY` | Sí | Para el INVESTIGADOR |
| `META_ACCESS_TOKEN` | No (futuro) | Para leer datos de Meta Ads API |
| `META_AD_ACCOUNT_ID` | No (futuro) | ID de tu cuenta de anuncios |
| `SLACK_WEBHOOK_URL` | No | Notificaciones al terminar tareas largas |

---

## Troubleshooting

**El agente no tiene contexto del negocio:**
→ Verificar que `CLAUDE.md` existe en la raíz y que Claude Code lo está leyendo.

**El INVESTIGADOR no puede buscar:**
→ Verificar `PERPLEXITY_API_KEY` en `.env`.

**Los outputs no siguen el formato correcto:**
→ El agente lee los templates en `templates/`. Puedes pedirle al COMANDANTE que los mejore si el formato no te convence.

**Quiero cambiar algo de cómo responde un agente:**
→ Edita directamente el `CLAUDE.md` del agente en `agents/<nombre>/CLAUDE.md`.
