---
name: linkedin-authority-builder
version: v1
description: Define la estrategia de posicionamiento y autoridad de Hans en LinkedIn — pilares de contenido, mix de formatos, cadencia, series recurrentes y sistema de crecimiento por fases.
---

# LinkedIn Authority Builder

## Cuándo usar este skill

- Al arrancar la presencia de Hans en LinkedIn (setup inicial de estrategia)
- Cuando se necesita replantear o ajustar la estrategia de contenido LinkedIn
- Trimestralmente para recalibrar pilares, formatos y cadencia
- Cuando cambia la oferta, el avatar o el posicionamiento del negocio
- Cuando el ESTRATEGA necesita alinear LinkedIn con la estrategia general

## Cuándo NO usar este skill

- Para escribir posts individuales (usar `linkedin/post-writer`)
- Para auditar el perfil (usar `linkedin/profile-optimizer`)
- Para analizar resultados semanales (usar `linkedin/retro-analyst`)
- Para contenido de Instagram (el enfoque y las reglas son distintas)

## Inputs necesarios

- **Oferta actual**: `memory/offer.md`
- **Avatar**: `memory/avatar.md`
- **Voz de marca**: `memory/brand-voice.md`
- **Posicionamiento actual**: `memory/brand-voice.md` → sección "Posicionamiento Anti-Gurú"
- **Contenido ganador**: `memory/winning-content.md`
- **Aprendizajes**: `memory/learnings.md`
- **Estado actual de LinkedIn** (si existe): seguidores, engagement promedio, posts publicados

## Workflow

1. **Leer contexto completo** de memoria del proyecto
2. **Definir posicionamiento** diferenciado para LinkedIn (vs. Instagram)
3. **Diseñar 3-5 pilares de contenido** específicos para LinkedIn
4. **Definir mix de formatos** con distribución porcentual
5. **Establecer cadencia** semanal recomendada
6. **Diseñar series recurrentes** (contenido con nombre propio que se repite)
7. **Mapear fases de crecimiento** con tácticas por fase
8. **Producir documento de estrategia** completo
9. **Guardar** en `docs/linkedin-strategy.md` o actualizar si ya existe

## Instrucciones

### Posicionamiento LinkedIn de Hans

Hans ya tiene posicionamiento claro en Instagram. LinkedIn NO es una réplica — es un canal complementario con audiencia y formato distintos.

**Instagram:** Audiencia amplia LATAM, formato video corto, tono informal/energético, Sub-avatar 2 también presente
**LinkedIn:** Sub-avatar 1 (profesional técnico), formato texto/carrusel, tono directo pero más técnico, B2B puro

**Posicionamiento LinkedIn:**
> "El practicante de automatizaciones IA que enseña a profesionales técnicos LATAM a monetizar esa habilidad — con casos reales, herramientas específicas (n8n + Claude) y cero humo."

**Diferenciadores en LinkedIn:**
1. Es el primero en LATAM enseñando monetización de automatizaciones IA con n8n en español
2. Comparte números reales (suyos y de alumnos) — no genéricos
3. Anti-gurú explícito — critica el hype como parte de su contenido
4. Stack técnico visible y específico (n8n, Claude, Make) — no "herramientas de IA" genérico
5. Habla desde primera persona presente — "esto es lo que estoy construyendo HOY"

### Los 5 Pilares de Contenido LinkedIn

| # | Pilar | % del mes | Propósito | Formatos principales |
|---|-------|-----------|-----------|---------------------|
| 1 | **Educación Técnica Aplicada** | 30% | Enseñar algo concreto con nombre de herramienta y caso de uso | Carrusel, texto largo |
| 2 | **Prueba Social / Casos Reales** | 25% | Demostrar que funciona con resultados medibles | Texto largo (story), carrusel de caso |
| 3 | **POV / Autoridad de Mercado** | 20% | Posicionar a Hans como referente con opinión propia | Texto corto/medio, poll |
| 4 | **Proceso Personal / BTS** | 15% | Conexión humana — qué está haciendo Hans hoy | Texto medio, video nativo |
| 5 | **Engagement / Diagnóstico** | 10% | Generar conversación y datos del avatar | Poll, pregunta abierta |

### Mix de Formatos

| Formato | Frecuencia | Engagement esperado | Mejor para |
|---------|-----------|-------------------|------------|
| **Carrusel PDF** (8-12 slides) | 1-2x/semana | 21.77% | Educación técnica, frameworks |
| **Texto largo** (300-600 palabras) | 1-2x/semana | Variable | Casos reales, POV, proceso |
| **Texto corto** (<150 chars + "ver más") | 1x/semana | Alto si hook fuerte | POV provocador, pregunta |
| **Poll** | 1x/semana o quincenal | Alto alcance | Diagnóstico del avatar, engagement |
| **Video nativo** (1-3 min) | 1-2x/mes | 7.35% | Demos técnicas, BTS |

### Cadencia Semanal Recomendada

| Día | Tipo de Post | Pilar | Formato |
|-----|-------------|-------|---------|
| **Martes** | Framework / How-to | Educación Técnica | Carrusel (8-10 slides) |
| **Jueves** | Caso real o POV | Prueba Social / Autoridad | Texto largo |
| **Sábado** | Engagement o BTS | Diagnóstico / Proceso | Poll o texto corto |

**Frecuencia:** 3 posts/semana. LinkedIn amplifica UN post por cuenta cada 24 horas. Más no es mejor.

**Horarios óptimos (hora local del público — Centro/Sur América):**
- Martes y Jueves: 8:30-9:30 AM
- Sábado: 10:00-11:00 AM

### Series Recurrentes (contenido con nombre propio)

Las series crean expectativa, reconocimiento y son más fáciles de producir porque tienen estructura fija.

| Serie | Frecuencia | Formato | Descripción |
|-------|-----------|---------|-------------|
| **Stack Real** | Quincenal | Carrusel | "El stack exacto que usé para [proyecto/resultado]" — muestra herramientas + flujo + resultado |
| **Caso LATAM** | Semanal | Texto largo | Historia de un alumno/cliente con números reales. Siempre: situación → acción → resultado |
| **Mito vs. Realidad** | Quincenal | Texto corto/medio | Desmonta un mito popular sobre IA/automatización con datos o experiencia real |
| **Pregunta del Avatar** | Semanal | Poll o pregunta | Pregunta diagnóstica que el Sub-avatar 1 no puede resistir responder |
| **Lo que Estoy Construyendo** | Quincenal | Texto medio o video | BTS de un proyecto actual — honesto, con dificultades incluidas |

### Fases de Crecimiento

| Fase | Seguidores | Foco | Tácticas |
|------|-----------|------|----------|
| **Fundación** (actual) | 0 → 500 | Perfil + consistencia + red base | Optimizar perfil (skill profile-optimizer), 3 posts/semana, método 5-5-5 de comentarios, conectar 10-20 del avatar/semana, activar Creator Mode |
| **Amplificación** | 500 → 2,000 | Carruseles + advocacy + colaboración | Carruseles técnicos 2x/semana, activar alumnos/clientes como advocacy, guest posts o LinkedIn Lives con peers |
| **Optimización** | 2,000 → 5,000 | Newsletter + retro analítica + ads orgánicos | Lanzar newsletter de LinkedIn, analizar top posts con retro-analyst, explorar Thought Leader Ads |
| **Escala** | 5,000+ | LinkedIn Ads + sistema de leads | LinkedIn Ads sobre posts orgánicos ganadores, lead-opportunity-mapper activo, funnel completo |

### Reglas Estratégicas de LinkedIn (basadas en datos 2025-2026)

1. **Expertise + Autenticidad + Relevancia** — los 3 pilares de contenido que LinkedIn premia
2. **Optimizar para conversación profunda**, no vanity metrics — saves, sends, profile views y quality comments importan más que likes
3. **Video vertical + captions + hooks fuertes** para video nativo — la mayoría ve sin sonido en mobile
4. **Links en el primer comentario**, nunca en el cuerpo del post — reduce distribución hasta 40%
5. **Polls estratégicos**: preguntas diagnósticas que reflejan el dolor del avatar, no trivialidades
6. **Thought leadership accionable**: cada post debe dejar al lector con algo que PUEDE hacer, no solo información
7. **Evitar contenido genérico**: si cualquier "experto en IA" podría publicar lo mismo, no es suficientemente específico para Hans
8. **Regla 80/20**: 80% valor educativo puro, 20% indirecto sobre la academia. LinkedIn penaliza la venta directa.
9. **Consistencia temática**: publicar solo sobre 1-2 temas (automatización IA + monetización técnica). El algoritmo categoriza perfiles dispersos como irrelevantes.
10. **Golden hour**: nunca publicar si Hans no puede responder comentarios en los siguientes 60 minutos

### Diferencias Instagram vs. LinkedIn

| Aspecto | Instagram | LinkedIn |
|---------|-----------|---------|
| Audiencia primaria | Sub-avatar 2 (empleado) + Sub-avatar 1 | Sub-avatar 1 (profesional técnico) |
| Formato principal | Video corto (Reels) | Carrusel PDF + texto largo |
| Tono | Informal, energético, casual | Directo, técnico, profesional pero humano |
| CTA | "Comenta X", "DM para Y" | "¿Qué agregarías?", "Cuéntame en comentarios" |
| Frecuencia | 7 posts/semana | 3 posts/semana |
| Monetización | Directa (links, DMs) | Indirecta (autoridad → inbound leads) |
| Algoritmo | Reels, engagement inmediato, shares | Dwell time, comentarios sustanciosos, perfil semántico |
| Cross-posting | ❌ Nunca copiar texto de LinkedIn | ❌ Nunca copiar formato de IG |

## Output (formato exacto)

```markdown
# Estrategia LinkedIn — Hans Villalobos / Momentum AI Academy
Fecha: YYYY-MM-DD
Fase actual: [Fundación / Amplificación / Optimización / Escala]

## Posicionamiento
[Declaración de posicionamiento en 2-3 líneas]

## Pilares de Contenido
[Tabla de 5 pilares con % y formatos]

## Cadencia Semanal
[Calendario semanal con días, tipos y formatos]

## Series Recurrentes
[Tabla de series con frecuencia y descripción]

## Fase Actual y Tácticas
[Descripción de la fase + 5-7 tácticas priorizadas]

## Métricas a Monitorear
[Las métricas relevantes para esta fase]

## Próxima Revisión
[Fecha sugerida para recalibrar]
```

Guardar en: `docs/linkedin-strategy.md`
