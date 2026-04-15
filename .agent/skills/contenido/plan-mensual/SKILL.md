# SKILL: Plan de Contenido Mensual
Versión: 1.0
Agente propietario: CREADOR
Agentes que pueden invocarla: COMANDANTE, CREADOR, ESTRATEGA
Última actualización: 2026-03-09

---

## ¿Qué hace este skill?

Genera el plan de contenido completo de un mes para @hansvilla.ai en Instagram.

Output: un archivo listo para copiar y pegar. Hans no necesita pensar nada — solo abrir el archivo, ver qué toca grabar esa semana, y ejecutar.

---

## Cuándo usar este skill

- Hans pide "el plan de contenido de [mes]"
- Han pasado más de 3 semanas desde el último plan generado
- El ESTRATEGA indica que hay un pilar de oferta que reforzar ese mes
- Hay un lanzamiento, campaña o fecha clave que justifica planificar con anticipación

---

## Inputs necesarios

| Input | Obligatorio | Descripción |
|-------|-------------|-------------|
| Mes y año | ✅ | Ej: "abril 2026" |
| Temas o campañas especiales | ❌ | Ej: "lanzamiento de nueva cohorte", "semana de garantía" |
| Qué está funcionando en contenido | ❌ | Leer `memory/winning-content.md` si existe |
| Research de tendencias | ❌ | Si no se provee, el CREADOR invoca al INVESTIGADOR |

---

## Proceso paso a paso

### Paso 1 — Leer memoria del sistema
Antes de generar nada, leer:
- `memory/avatar.md` — para quién es el contenido
- `memory/offer.md` — qué se está vendiendo y con qué ángulos
- `memory/brand-voice.md` — cómo habla Hans
- `memory/winning-content.md` — qué ya funcionó (no repetir, sí ampliar)
- `memory/learnings.md` — qué aprendizajes acumulados hay

### Paso 2 — Obtener tendencias del mes
Invocar al INVESTIGADOR con la búsqueda:
`"tendencias IA automatización n8n LATAM [mes] [año] Instagram content creators"`

Si el INVESTIGADOR ya tiene un reporte reciente (menos de 7 días), usarlo directamente.

### Paso 3 — Definir el enfoque del mes
Con el contexto de memoria + tendencias, definir:
- **Tema central del mes** (ej: "Agentes de IA como servicio")
- **Pilar de oferta a reforzar** (ej: TOFU — atraer nuevos, o MOFU — nutrir leads existentes)
- **1 campaña de conversión** (la semana que más directamente empuja al DM)

### Paso 4 — Distribuir los 30 días

**Frecuencia: 7 posts/semana**

| Día | Tipo de contenido | Pilar |
|-----|------------------|-------|
| Lunes | Reel educativo (enseña algo concreto) | Valor / TOFU |
| Martes | Story sequence (3-5 stories) | Engagement |
| Miércoles | Reel de opinión / POV | Autoridad |
| Jueves | Story sequence (caso real o behind the scenes) | Prueba social |
| Viernes | Reel de demo (n8n en acción o resultado de cliente) | Conversión / MOFU |
| Sábado | Post estático o carrusel (tips, checklist, datos) | Valor / Compartible |
| Domingo | Reel personal / historia (motivación, proceso, vida real) | Conexión |

**Distribución mensual (4 semanas completas + días extra):**
- Reels: ~20 (lunes + miércoles + viernes + domingo = 4 reels/semana)
- Stories: ~8 secuencias (martes + jueves)
- Posts estáticos/carruseles: ~4 (sábados)

### Paso 5 — Generar los contenidos

Para cada reel del mes, el CREADOR produce:
1. **Título interno** (para Hans identificar de qué trata)
2. **Hook** (las primeras palabras exactas + texto en pantalla)
3. **Ángulo** (1 línea que describe de qué trata el video)
4. **Guión completo** solo para los reels de las semanas 1 y 2 — las semanas 3 y 4 van en brief (Hans confirma antes)
5. **Caption** (texto del post en Instagram)
6. **Hashtags** (8-12, mezcla de nicho + tendencia)
7. **Hora de publicación recomendada**

Para cada story sequence:
1. Tema de la secuencia (3-5 historias)
2. Copy de cada story + tipo de sticker (poll, slider, pregunta, link)
3. CTA de cierre de la secuencia

Para cada post estático/carrusel:
1. Título del carrusel
2. Copy de cada slide (máx 7 slides)
3. Caption

---

## Estructura del output

El output se guarda en:
`outputs/calendars/[año]-[mes]_plan-contenido.md`

```
# Plan de Contenido — [Mes] [Año]
## Resumen del mes
## Tema central
## Semana 1 (fechas)
### Lunes [fecha] — [Título del reel]
  - Hook:
  - Ángulo:
  - Guión:
  - Caption:
  - Hashtags:
  - Hora de publicación:
### Martes [fecha] — Story sequence: [tema]
  ...
[y así para cada día de las 4 semanas]
```

---

## Reglas de contenido para @hansvilla.ai

1. **Nunca tutear** — Hans usa "usted" en contenido educativo y de valor. Solo usa "vos" en contenido muy casual/personal.
2. **No sonar a guru de hacerse rico** — El tono es de profesional serio que enseña algo real. Frases como "hazte millonario" o "libertad financiera total" están prohibidas.
3. **Siempre nombre herramientas específicas** — n8n, Claude, Make, Perplexity. No "herramientas de IA" genérico.
4. **El avatar técnico primero** — El Sub-avatar 1 (ingeniero/contador/analista) es el que más rápido cierra. Al menos 50% del contenido debe resonar con ese perfil.
5. **Demos > teoría** — Cuando sea posible, el contenido muestra flujos reales de n8n, resultados reales de clientes, procesos reales. No solo conceptos.
6. **Un CTA claro por post** — No más de un llamado a la acción. La mayoría van a DM ("escríbeme X por DM") o a seguir la cuenta.
7. **Contenido evergreen primero** — Que el 70% del contenido pueda funcionar en cualquier mes. El 30% puede ser de tendencia actual.

---

## Pillares de contenido de @hansvilla.ai

| Pilar | % del mes | Descripción |
|-------|-----------|-------------|
| Educación técnica | 35% | Cómo funciona n8n, automatizaciones, IA aplicada — enseñar algo concreto |
| Prueba social | 20% | Casos reales de alumnos o clientes (Alejandro, Daniela, Rafael...) |
| Autoridad / POV | 20% | Opinión de Hans sobre el mercado, la IA, el trabajo del futuro |
| Conversión directa | 15% | Posts que empujan al DM / a la academia directamente |
| Personal / Conexión | 10% | Proceso de Hans, vida real, motivación sin perder la seriedad |

---

## Notas para el CREADOR

- **Semanas 1 y 2:** guiones completos (Hans puede grabar sin pensar)
- **Semanas 3 y 4:** briefs y ángulos solamente (Hans confirma tendencias antes de producir)
- Si Hans da feedback sobre la semana 1, aplicarlo antes de entregar la semana 3
- Si hay un ad activo, al menos 1 reel orgánico/semana debe reforzar el mismo ángulo del ad para consistencia de mensaje
- Guardar en `memory/winning-content.md` cualquier formato o ángulo que Hans confirme como bueno

---

## Ejemplo de invocación

**Hans dice:** "Dame el plan de contenido de abril"

**COMANDANTE hace:**
1. Invoca INVESTIGADOR → tendencias de abril en IA/automatización LATAM
2. Invoca CREADOR con este skill → genera el plan completo
3. Entrega el archivo `outputs/calendars/2026-04_plan-contenido.md`

**Hans recibe:** archivo completo, semanas 1 y 2 con guiones, semanas 3 y 4 con briefs listos para confirmar.
