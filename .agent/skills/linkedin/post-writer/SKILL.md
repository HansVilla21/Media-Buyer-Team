---
name: linkedin-post-writer
version: v1
description: Genera posts de LinkedIn por formato y tipo — con guardrails de voz, estructura por formato, validación anti-genérico y output completo listo para publicar.
---

# LinkedIn Post Writer

## Cuándo usar este skill

- Hans pide un post de LinkedIn (cualquier formato)
- El calendario de contenido requiere un post LinkedIn
- El CREADOR necesita adaptar un reel de Instagram a LinkedIn
- Hay un tema oportuno que merece un post rápido

## Cuándo NO usar este skill

- Para contenido de Instagram (usar skills de contenido del CREADOR)
- Para definir estrategia (usar `linkedin/authority-builder`)
- Para escribir comentarios (usar `linkedin/comment-engine`)
- Para scripts de ads de LinkedIn (cuando se active, usar skills de MEDIA BUYER)

## Inputs necesarios

- **Tipo de post**: insight/opinion, framework, story/caso, myth busting, trend commentary, educational, poll, poll follow-up, adaptación de reel
- **Tema o ángulo**: qué punto específico abordar
- **Pilar**: a cuál de los 5 pilares pertenece (ver authority-builder)
- **Contexto de memoria**: brand-voice.md + avatar.md + winning-content.md

## Workflow

1. **Leer contexto**: brand-voice.md, avatar.md, winning-content.md
2. **Identificar tipo de post** y seleccionar estructura correspondiente
3. **Redactar** siguiendo la estructura del tipo + reglas de formato LinkedIn
4. **Aplicar guardrails** anti-genérico (ver checklist abajo)
5. **Generar 3-5 opciones de primera línea** (hook)
6. **Producir output completo** con todos los elementos
7. **Guardar** en `outputs/linkedin/YYYY-MM-DD_[tipo]-[tema].md`

## Instrucciones

### Estructuras por Tipo de Post

---

#### TIPO 1 — Insight / Opinión (POV)

Postura personal de Hans sobre algo del mercado. Genera discusión.

```
[PRIMERA LÍNEA — afirmación fuerte o contraintuitiva, sola]

[Línea en blanco]

[Por qué mucha gente piensa diferente — 2-3 líneas]

[Por qué Hans piensa distinto — con evidencia o experiencia REAL]

[Implicación práctica para el lector — qué puede hacer con esto]

[Pregunta abierta genuina para generar comentarios]

#hashtag1 #hashtag2 #hashtag3
```

---

#### TIPO 2 — Framework / How-to (Carrusel)

Educación técnica estructurada. Máximo engagement.

**Texto del post (acompañando al carrusel):**
```
[PRIMERA LÍNEA — el resultado que obtienen si aplican esto]

[Línea en blanco]

[Contexto breve: por qué esto importa — 2-3 líneas]

[Vista previa de lo que van a encontrar en el carrusel]

[CTA: "Guardá esto para cuando lo necesites" / "¿Qué agregarías?"]

#hashtag1 #hashtag2 #hashtag3
```

**Descripción de slides del carrusel:**
```
SLIDE 1 — HOOK: [Titular fuerte + sublínea + visual limpio]
SLIDE 2: [Primer punto con ejemplo concreto]
...
SLIDE 8-10: [Puntos restantes, uno por slide]
SLIDE FINAL: [Conclusión + CTA + @hansvilla.ai + Momentum AI Academy]
```

---

#### TIPO 3 — Story / Caso Real

Historia corta de alumno, cliente o proyecto con resultado medible.

```
[PRIMERA LÍNEA — el resultado, no la historia]

[Línea en blanco]

[Situación inicial: quién era, qué problema tenía — 3-4 líneas]

[Qué aprendió o implementó — mención específica de herramienta]

[Resultado con número concreto y timeline]

[Por qué importa para el lector — la lección universal]

[CTA: "¿Tienes un perfil similar? Cuéntame en los comentarios."]

#hashtag1 #hashtag2 #hashtag3
```

---

#### TIPO 4 — Myth Busting

Desmonta un mito popular con datos o experiencia.

```
[PRIMERA LÍNEA — el mito, presentado como si fuera verdad]

[Línea en blanco]

[Pausa dramática: "Eso es lo que te dicen." o "Suena bien, ¿verdad?"]

[La realidad — con dato, caso real o experiencia directa]

[Por qué el mito persiste — contexto]

[Qué debería hacer el lector en su lugar]

[Pregunta: "¿Cuál es el mito de IA que más te molesta?"]

#hashtag1 #hashtag2 #hashtag3
```

---

#### TIPO 5 — Trend Commentary

Reacción oportuna a algo que está pasando en el mercado.

```
[PRIMERA LÍNEA — referencia al evento/tendencia + postura clara]

[Línea en blanco]

[Qué pasó — contexto breve, no más de 3 líneas]

[Qué significa para profesionales en LATAM — la implicación real]

[Lo que Hans piensa que deberían hacer — acción concreta]

[Pregunta: "¿Esto ya lo están viendo en sus empresas?"]

#hashtag1 #hashtag2 #hashtag3
```

---

#### TIPO 6 — Educational

Enseñanza pura de un concepto o herramienta. Valor sin venta.

```
[PRIMERA LÍNEA — el concepto que van a aprender, enmarcado como beneficio]

[Línea en blanco]

[Contexto: por qué este concepto importa ahora — 2-3 líneas]

[Explicación clara, paso a paso o por puntos — máx 5 puntos]

[Ejemplo concreto de aplicación con herramienta específica]

[CTA educativo: "Guardá esto" / "¿Quieres que profundice en algún punto?"]

#hashtag1 #hashtag2 #hashtag3
```

---

#### TIPO 7 — Poll

Pregunta diagnóstica que el avatar no puede resistir.

```
[Pregunta que describe exactamente el dolor/situación del avatar]

- Opción A
- Opción B
- Opción C
- Opción D (con toque de humor o verdad incómoda)

[2-3 líneas de contexto: por qué preguntas esto]

#hashtag1 #hashtag2 #hashtag3
```

---

#### TIPO 8 — Poll Follow-up

Publicar resultados de un poll anterior con análisis.

```
[PRIMERA LÍNEA — el dato más sorprendente del poll]

[Línea en blanco]

[Resultados resumidos + qué revelan sobre el mercado]

[Interpretación de Hans — qué significa esto para profesionales LATAM]

[Acción recomendada basada en los datos]

[CTA: "¿El resultado te sorprendió? ¿Por qué?"]

#hashtag1 #hashtag2 #hashtag3
```

---

#### TIPO 9 — Adaptación de Reel de Instagram

| Elemento del Reel | Adaptación LinkedIn |
|-------------------|---------------------|
| Hook del video (0-3 seg) | Primera línea del post |
| Cuerpo del guión | 3-5 párrafos cortos con puntos clave |
| Demo de n8n en pantalla | Descripción textual del flujo + captura como imagen adjunta |
| CTA "escríbeme X por DM" | "¿Tú has tenido esta situación? Cuéntame en los comentarios." |
| Prueba social del video | Mismo caso, narrado en texto con nombre + cargo + resultado |

**Regla:** Nunca copiar el texto del reel. Adaptar tono, profundidad y formato.

### Reglas de Formato LinkedIn (TODAS aplican a todos los tipos)

1. **Primera línea es TODO.** LinkedIn corta con "ver más" después de 2-3 líneas. Si la primera línea falla, nadie lee el resto.
2. **Párrafos de 1-2 líneas máximo.** Mobile-first.
3. **Links en el PRIMER COMENTARIO**, nunca en el cuerpo.
4. **3-5 hashtags al final.** Hashtags con 10K-500K seguidores. No dentro del texto.
5. **Máximo 1-2 emojis estratégicos.** El Sub-avatar técnico es sensible al exceso.
6. **No sonar a LinkedIn motivacional.** Nada de "el éxito llega a quienes perseveran".
7. **No texto de IA sin editar.** Todo debe sonar a Hans — sus muletillas, su directness, sus ejemplos.
8. **CTA suave.** "¿Qué agregarías?" > "Comenta SÍ si estás de acuerdo".
9. **Responder TODOS los comentarios** en los primeros 60 minutos.

### Guardrails Anti-Genérico (CHECKLIST antes de entregar)

Antes de entregar cualquier post, verificar:

- [ ] ¿La primera línea engancha sin ser clickbait?
- [ ] ¿Hay al menos 1 dato, nombre de herramienta o número real?
- [ ] ¿Suena a Hans o suena a cualquier "experto en IA"?
- [ ] ¿Tiene punto de vista o solo es información plana?
- [ ] ¿El CTA es natural y no agresivo?
- [ ] ¿Está escrito en español neutro LATAM?
- [ ] ¿Los hashtags son específicos del nicho?
- [ ] ¿Cabría en los pilares definidos en authority-builder?
- [ ] ¿Pasa la regla anti-gurú? (sin hype, sin promesas vacías, sin estadísticas inventadas)
- [ ] ¿Aporta algo accionable al lector?

Si algún check falla, reescribir antes de entregar.

### Librería de Hooks por Tipo

**Hooks con dato:**
- "El 80% de ingenieros que intentan vender automatizaciones fracasan en el primer mes."
- "Una automatización bien vendida vale entre $1,200 y $3,000 USD. No lo digo yo — lo cobran mis alumnos."

**Hooks con postura:**
- "Los cursos de ChatGPT no van a cambiar su carrera. Las automatizaciones de negocios sí."
- "n8n no es difícil. Difícil es vender sin saber qué problema específico resuelve."

**Hooks con story:**
- "Alejandro lleva 4 meses en la academia. El mes pasado facturó $2,000 USD en un fin de semana."
- "Hoy tardé 3 horas en hacer que Claude y n8n se comunicaran correctamente."

**Hooks con pregunta:**
- "¿Cuántas horas semanales pierdes en procesos manuales repetitivos en tu trabajo?"
- "¿Tu empresa adoptó alguna herramienta de IA en los últimos 6 meses?"

**Hooks con mito:**
- "Necesitas saber programar para vender automatizaciones."
- "Con ChatGPT ya estás automatizando."

## Output (formato exacto)

```markdown
# Post LinkedIn: [Tipo] — [Tema]
Fecha: YYYY-MM-DD
Pilar: [nombre del pilar]
Formato: [carrusel / texto largo / texto corto / poll / video]
Serie: [nombre de serie recurrente, si aplica]

---

## Opciones de Primera Línea (hook)
1. [opción A]
2. [opción B]
3. [opción C]

## Texto Completo del Post
[Post completo listo para copiar/pegar]

## Primer Comentario
[Texto del primer comentario — link, dato adicional o contexto]

## Imagen/Visual Recomendado
[Descripción del visual o brief para slides del carrusel]

## Hashtags
#hashtag1 #hashtag2 #hashtag3

## Horario Recomendado
[Día y hora óptima]

## Checklist Anti-Genérico
[x] Hook que engancha
[x] Dato/número real
[x] Voz de Hans
[x] Punto de vista claro
[x] CTA natural
[x] Español LATAM
[x] Alineado a pilar
[x] Anti-gurú pass
[x] Accionable
```

Guardar en: `outputs/linkedin/YYYY-MM-DD_[tipo]-[tema].md`
