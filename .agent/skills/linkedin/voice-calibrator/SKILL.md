---
name: founder-voice-calibrator
version: v1
description: Extrae y documenta la voz real de Hans — tono, postura, vocabulario, ritmo, nivel de detalle, temas recurrentes, ejemplos favoritos y anti-patterns — para producir una referencia reusable que garantice contenido auténtico en cualquier plataforma.
---

# Founder Voice Calibrator

## Cuándo usar este skill

- Al iniciar la presencia en una nueva plataforma (LinkedIn, newsletter, podcast)
- Cuando el contenido generado "no suena a Hans" (feedback de Hans o del equipo)
- Trimestralmente para recalibrar la voz contra contenido real publicado
- Cuando se incorpora un nuevo agente o skill que genera contenido
- Cuando Hans cambia su enfoque o posicionamiento

## Cuándo NO usar este skill

- Para escribir posts directamente (usar post-writer o las skills del CREADOR)
- Para definir estrategia de contenido (usar authority-builder)
- Para investigación de mercado (usar signal-researcher o INVESTIGADOR)

## Inputs necesarios

- **brand-voice.md actual**: `memory/brand-voice.md`
- **Contenido real de Hans**: posts publicados, reels grabados, mensajes de voz, transcripciones
- **Feedback acumulado**: preferencias expresadas por Hans en sesiones anteriores
- **winning-content.md**: qué contenido funcionó y por qué
- **learnings.md**: patrones de estilo documentados

## Workflow

1. **Leer brand-voice.md** actual como baseline
2. **Analizar contenido real** de Hans (posts, scripts que aprobó, correcciones que hizo)
3. **Extraer patrones de voz** en 8 dimensiones (ver abajo)
4. **Identificar anti-patterns** — lo que definitivamente NO es Hans
5. **Documentar "voice fingerprint"** — la referencia que todo agente/skill debe consultar
6. **Comparar con brand-voice.md** — actualizar si hay divergencias
7. **Producir Voice Guide** actualizada
8. **Guardar** en `docs/linkedin-voice.md` (para LinkedIn) y actualizar `memory/brand-voice.md` si aplica

## Instrucciones

### Las 8 Dimensiones de Voz

#### 1. Tono General
- **¿Formal o informal?** Informal pero profesional. Como hablar con un amigo inteligente.
- **¿Optimista o realista?** Realista con optimismo calibrado. "Esto funciona, pero tardó 3 meses."
- **¿Autoritativo o accesible?** Ambos — autoridad ganada con experiencia, entregada de forma accesible.
- **¿Emocional o analítico?** Analítico con momentos emocionales estratégicos.

#### 2. Vocabulario
- **Palabras que USA frecuentemente**: automatización, IA, flujo, workflow, proceso, cobrar, proyecto, cliente, resultado, n8n, Claude, negocio, herramienta, construir, vender
- **Expresiones CR naturales**: "diay", "mae", "póngale"
- **Frases identitarias**: "Si yo pude, vos también podés", "La realidad es...", "No me caso con una sola herramienta"
- **Palabras que EVITA**: implementar sinergias, maximizar ROI, emprendimiento (sin contexto), gamechanger, disruptivo, brutal, increíble (sin sustancia)

#### 3. Ritmo y Estructura
- **Largo de oraciones**: Cortas. Impacto. Pausa. Luego desarrolla.
- **Estructura de párrafos**: 1-2 oraciones por párrafo en social media
- **Patrón narrativo**: Resultado → Proceso → Prueba → CTA
- **Preguntas retóricas**: Frecuentes, para involucrar al lector
- **Repetición estratégica**: Repite la idea central en diferentes palabras para fijarla

#### 4. Nivel de Detalle Técnico
- **¿Nombra herramientas?** Sí, siempre con nombre propio: n8n, Claude, Make, Airtable
- **¿Muestra código o flujos?** En demos sí, en texto lo describe como proceso
- **¿Asume conocimiento previo?** Medio — no explica qué es IA, pero sí explica herramientas específicas
- **¿Usa jerga técnica?** Solo cuando agrega valor. Siempre conecta a resultado de negocio.

#### 5. Postura y Opinión
- **¿Tiene opiniones fuertes?** Sí — anti-gurú, anti-hype, pro-resultados reales
- **¿Las expresa directamente?** Sí, sin rodeos: "Los cursos de ChatGPT no van a cambiar su carrera"
- **¿Contradice consenso?** Frecuentemente, pero con evidencia o experiencia
- **¿Reconoce incertidumbre?** Sí cuando es genuina: "No sé si esto funcione para todos"

#### 6. Uso de Ejemplos
- **¿De dónde vienen?** De sus propios proyectos, alumnos, o clientes reales
- **¿Tienen números?** Siempre que sea posible: "$2,500 primer cliente", "200+ consultas/mes"
- **¿Incluyen fracasos?** Sí: "Esto tardó 3 meses en funcionar", "La primera versión era horrible"
- **¿Son específicos o genéricos?** Muy específicos: industria, herramienta, timeline, resultado

#### 7. Relación con la Audiencia
- **¿Habla de tú o de usted?** De tú/vos (dependiendo del contexto LATAM)
- **¿Condescendiente?** Nunca — trata a la audiencia como capaz
- **¿Se incluye en el grupo?** A veces: "Nosotros los que trabajamos en esto..."
- **¿Pide acción?** Siempre — CTA específico, nunca genérico

#### 8. Anti-Patterns (lo que NO es Hans)

| Si suena así... | NO es Hans |
|-----------------|-----------|
| "El secreto que nadie te dice" | Hooks de gurú |
| "Esto cambia todo!" (sin contexto) | Hipérbole vacía |
| "Implementar sinergias estratégicas" | Corporativismo |
| "¡Vos podés! ¡A darle!" | Motivación vacía |
| "Gana $10K en 30 días" | Promesa irreal |
| Párrafos de 5+ líneas seguidas | Muro de texto |
| Exceso de emojis y signos de exclamación | Estilo vendedor |
| "Te cuento mi historia..." (larga y autoindulgente) | Storytelling sin valor |
| "Según estudios..." (sin fuente específica) | Autoridad prestada |

### Proceso de Calibración

**Método de extracción (cuando hay contenido real disponible):**

1. Seleccionar 10-15 piezas de contenido que Hans aprobó y que tuvieron buen resultado
2. Analizar: ¿qué tienen en común? ¿tono? ¿estructura? ¿vocabulario?
3. Seleccionar 5 piezas que Hans rechazó o corrigió
4. Analizar: ¿qué corrigió? ¿qué eliminó? ¿qué cambió?
5. El delta entre lo aprobado y lo rechazado = la voz real de Hans

**Método de entrevista (cuando se necesita más profundidad):**

Preguntas clave para Hans:
- "¿Cuál fue tu momento de mayor frustración con el negocio? ¿Cómo lo describirías en 2 frases?"
- "¿Qué contenido de otros creadores te da vergüenza ajena? ¿Por qué?"
- "¿Cómo le explicarías a un amigo inteligente lo que haces, en 30 segundos?"
- "¿Qué frase tuya te define?"
- "¿Cuándo fue la última vez que cambiaste de opinión sobre algo del negocio?"
- "¿Qué es lo que más te molesta del nicho de educación en IA?"

### Reglas de Uso del Voice Guide

1. **Todo agente que genere contenido público** debe leer el voice guide antes de escribir
2. **El voice guide no reemplaza brand-voice.md** — lo complementa con más profundidad
3. **Actualizar cada vez que Hans corrija algo** — una corrección es un dato de calibración
4. **La voz evoluciona** — recalibrar trimestralmente
5. **LinkedIn tiene ajustes** vs. Instagram: más técnico, más largo, menos coloquial, misma esencia

## Output (formato exacto)

```markdown
# Voice Guide — Hans Villalobos
Última calibración: YYYY-MM-DD
Fuente: [contenido analizado / entrevista / feedback acumulado]

## Voice Fingerprint (resumen en 3 líneas)
[Cómo suena Hans en su mejor contenido]

## Las 8 Dimensiones
### 1. Tono General
[descripción calibrada]

### 2. Vocabulario
**USA:** [lista]
**EVITA:** [lista]
**Frases identitarias:** [lista]

### 3. Ritmo y Estructura
[descripción]

### 4. Nivel Técnico
[descripción]

### 5. Postura
[descripción]

### 6. Uso de Ejemplos
[descripción + ejemplos reales]

### 7. Relación con Audiencia
[descripción]

### 8. Anti-Patterns
[tabla de lo que NO es Hans]

## Test de Voz (verificación rápida)
Antes de publicar, verificar:
- [ ] ¿Hans diría esto en una conversación real?
- [ ] ¿Hay al menos 1 ejemplo específico con número?
- [ ] ¿Suena a Hans o a "cualquier experto en IA"?
- [ ] ¿Pasa el filtro anti-gurú?
- [ ] ¿Las frases son cortas y directas?
```

Guardar Voice Guide LinkedIn en: `docs/linkedin-voice.md`
Actualizar si es necesario: `memory/brand-voice.md`
