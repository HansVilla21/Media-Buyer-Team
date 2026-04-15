# Arquitectura del Sistema — Media Buyer Team

---

## Visión General

El sistema funciona como un equipo de marketing y media buying coordinado por un agente orquestador (COMANDANTE). Hans solo habla con el COMANDANTE, quien delega tareas a los agentes especializados y consolida los resultados.

```
┌─────────────────────────────────────────────────┐
│                    HANS                          │
│              (@hansvilla.ai)                     │
└───────────────────┬─────────────────────────────┘
                    │ habla con
                    ▼
┌─────────────────────────────────────────────────┐
│               COMANDANTE                        │
│           (Agente Orquestador)                  │
│                                                 │
│  • Lee contexto de memory/ al inicio            │
│  • Entiende el pedido de Hans                   │
│  • Decide qué agentes activar                   │
│  • Consolida resultados                         │
│  • Presenta output listo para usar              │
│  • Gestiona memoria y skills                    │
└──────┬──────────┬──────────┬──────────┬─────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
  CREADOR   INVESTIGADOR  MEDIA     ESTRATEGA
                          BUYER
```

---

## Los 5 Agentes

### COMANDANTE
- **Archivo:** `agents/comandante/CLAUDE.md`
- **Rol:** Orquestador. El único punto de contacto con Hans.
- **Inputs:** Pedidos de Hans en lenguaje natural
- **Outputs:** Resultados consolidados, listos para usar
- **Herramientas:** Acceso a todos los archivos del proyecto
- **Cuándo llamarlo:** Siempre — es la puerta de entrada al sistema

### CREADOR
- **Archivo:** `agents/creador/CLAUDE.md`
- **Rol:** Creación de todo el contenido orgánico
- **Inputs:** Temas, ideas, reportes del INVESTIGADOR, calendario
- **Outputs:** Guiones de reels, secuencias de stories, calendarios
- **Herramientas:** Lee `memory/`, usa `templates/`, escribe en `outputs/`
- **Cuándo llamarlo:** Cuando se necesita contenido

### INVESTIGADOR
- **Archivo:** `agents/investigador/CLAUDE.md`
- **Rol:** Research en tiempo real del mercado
- **Inputs:** Temas a investigar, preguntas de estrategia o contenido
- **Outputs:** Reportes en `outputs/research/`
- **Herramientas:** Perplexity API, archivos del proyecto
- **Cuándo llamarlo:** Antes de crear contenido importante, para análisis de mercado, para alimentar al MEDIA BUYER

### MEDIA BUYER
- **Archivo:** `agents/media-buyer/CLAUDE.md`
- **Rol:** Publicidad paga en Meta (Facebook/Instagram)
- **Inputs:** Objetivos de campaña, datos de ads, research del INVESTIGADOR
- **Outputs:** Scripts de ads, análisis de campañas, recomendaciones
- **Herramientas:** Lee `memory/`, usa `templates/`, escribe en `outputs/ads/`
- **Cuándo llamarlo:** Para crear nuevos ads, analizar rendimiento, optimizar campañas

### ESTRATEGA
- **Archivo:** `agents/estratega/CLAUDE.md`
- **Rol:** Visión macro, oferta y posicionamiento
- **Inputs:** Datos de negocio, research de mercado, feedback de ventas
- **Outputs:** Análisis de oferta, refinamiento de avatar, estrategia mensual
- **Herramientas:** Lee toda la `memory/`, escribe en `outputs/strategy/`
- **Cuándo llamarlo:** Mensualmente para estrategia, cuando algo no está funcionando, antes de lanzamientos

---

## Flujo de Datos

### Flujo 1: Crear contenido para la semana

```
Hans: "Necesito guiones para esta semana"
         │
         ▼
    COMANDANTE
    ├─ Lee memory/learnings.md
    ├─ Lee memory/winning-content.md
    │
    ├──► INVESTIGADOR (opcional)
    │    ├─ Busca tendencias actuales en Perplexity
    │    └─ Guarda reporte en outputs/research/
    │
    └──► CREADOR
         ├─ Lee memory/brand-voice.md + avatar.md
         ├─ Lee reporte del INVESTIGADOR
         ├─ Usa templates/reel-script.md
         └─ Guarda guiones en outputs/reels/
              │
              ▼
         COMANDANTE consolida y presenta a Hans
```

### Flujo 2: Analizar y mejorar ads

```
Hans: [Pega datos de Meta Ads Manager]
         │
         ▼
    COMANDANTE
    │
    ├──► INVESTIGADOR
    │    ├─ Busca benchmarks y qué está funcionando en el nicho
    │    └─ Guarda reporte en outputs/research/
    │
    └──► MEDIA BUYER
         ├─ Analiza métricas vs benchmarks
         ├─ Lee reporte del INVESTIGADOR
         ├─ Genera recomendaciones + scripts de nuevos ads
         └─ Guarda en outputs/ads/analysis/ y outputs/ads/scripts/
              │
              ▼
         COMANDANTE consolida y presenta a Hans
```

### Flujo 3: Aprendizaje del sistema

```
Hans: "Este reel funcionó muy bien, tuvo 50k vistas"
         │
         ▼
    COMANDANTE
    ├─ Registra en memory/winning-content.md
    ├─ Extrae patrón
    ├─ Evalúa si crear/actualizar una skill
    └─ Actualiza memory/learnings.md
```

---

## Sistema de Memoria

La carpeta `memory/` es el cerebro compartido. Todos los agentes la leen antes de trabajar y escriben en ella cuando aprenden algo nuevo.

| Archivo | Quién lo escribe | Quién lo lee | Contenido |
|---------|-----------------|--------------|-----------|
| `brand-voice.md` | COMANDANTE, Hans | Todos | Tono, frases, estilo |
| `offer.md` | ESTRATEGA, Hans | Todos | Oferta completa |
| `avatar.md` | ESTRATEGA, Hans | Todos | ICP detallado |
| `winning-content.md` | COMANDANTE, CREADOR | CREADOR, MEDIA BUYER | Lo que funcionó |
| `learnings.md` | Todos | Todos | Aprendizajes del sistema |

**Regla:** Solo se escribe información confirmada. No especulación.

---

## Sistema de Skills

Las skills son procedimientos estandarizados que los agentes usan para hacer su trabajo mejor y más consistente.

```
.agent/skills/
├── creador-de-skills/    ← El skill que crea otros skills
│   └── SKILL.md
├── contenido/            ← Skills del CREADOR (se van creando)
│   ├── guion-demo/
│   ├── guion-quick-tip/
│   └── ...
├── ads/                  ← Skills del MEDIA BUYER (se van creando)
│   ├── hook-generator/
│   └── ...
├── investigacion/        ← Skills del INVESTIGADOR (se van creando)
│   └── ...
└── estrategia/           ← Skills del ESTRATEGA (se van creando)
    └── ...
```

**Ciclo de vida de una skill:**
1. El agente detecta un proceso repetible
2. Usa `creador-de-skills` para documentarlo
3. Pide confirmación al COMANDANTE
4. Se escribe el archivo SKILL.md
5. Se registra en `memory/learnings.md`
6. En el futuro, el agente la consulta antes de hacer el mismo tipo de tarea

---

## Convenciones de Nombres

### Archivos de outputs
```
YYYY-MM-DD_[descripcion-en-kebab].md

Ejemplos:
2026-03-10_guion-demo-antigravity.md
2026-03-10_v1_hook-problema-empleo.md
2026-03_calendario-contenido.md
```

### Archivos de memoria
```
[nombre-descriptivo].md  (sin fecha — son documentos vivos)
```

### Skills
```
[verbo-objeto]  en kebab-case
guion-demo, analisis-campañas, research-tendencias
```

---

## Integraciones Externas

| Integración | Agente | Estado | Variable | Uso principal |
|-------------|--------|--------|----------|---------------|
| Anthropic API | Todos | Activa | `ANTHROPIC_API_KEY` | Motor de todos los agentes |
| Perplexity Sonar Pro | INVESTIGADOR | Activa | `PERPLEXITY_API_KEY` | Research y búsquedas en tiempo real |
| Google Gemini / Imagen 3 | CREADOR, MEDIA BUYER | Activa | `GEMINI_API_KEY` | Generación de imágenes, análisis visual, modelos alternativos |
| Meta Ads API | MEDIA BUYER | Futuro | `META_ACCESS_TOKEN` | Leer métricas de campañas automáticamente |
| n8n webhooks | COMANDANTE | Futuro | — | Triggers automáticos desde flujos n8n |
| Slack | COMANDANTE | Opcional | `SLACK_WEBHOOK_URL` | Notificaciones al terminar tareas largas |

---

## Evolución del Sistema

El sistema está diseñado para crecer. Fases sugeridas:

**Fase 1 (Ahora):** Fundaciones
- 5 agentes operativos
- Memoria base llena
- Primera skill funcional (creador-de-skills)
- Flujo manual: Hans pide → agente responde

**Fase 2 (Pronto):** Especialización
- Banco de hooks virales documentado como skill
- Fórmulas de guiones probadas como skills
- Patrones de ads ganadores documentados
- INVESTIGADOR con queries optimizadas

**Fase 3 (Futuro):** Automatización
- Conexión con Meta Ads API para leer métricas automáticamente
- Triggers desde n8n para iniciar tareas automáticas
- Notificaciones por Slack cuando hay alertas de ads
- Generación automática del calendario mensual
