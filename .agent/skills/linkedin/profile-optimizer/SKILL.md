---
name: linkedin-profile-optimizer
version: v1
description: Audita y optimiza el perfil de LinkedIn de Hans para maximizar distribución algorítmica, conversión de visitantes a seguidores y generación de leads del Sub-avatar 1.
---

# LinkedIn Profile Optimizer

## Cuándo usar este skill

- Hans pide auditar o mejorar su perfil de LinkedIn
- Antes de lanzar cualquier campaña de contenido en LinkedIn (el perfil es prerequisito)
- Cuando cambia la oferta, el posicionamiento o el avatar principal
- Trimestralmente como mantenimiento preventivo
- Cuando las métricas de profile views o follower conversion bajan

## Cuándo NO usar este skill

- Para crear contenido de posts (usar `linkedin/post-writer`)
- Para estrategia general de LinkedIn (usar `linkedin/authority-builder`)
- Si el pedido es sobre Instagram — el perfil de IG tiene reglas distintas

## Inputs necesarios

- **URL o captura del perfil actual** (si disponible)
- **Oferta vigente**: leer `memory/offer.md`
- **Avatar target**: leer `memory/avatar.md` (priorizar Sub-avatar 1)
- **Voz de marca**: leer `memory/brand-voice.md`
- **Objetivos actuales de LinkedIn**: leer `docs/linkedin-strategy.md`

## Workflow

1. **Leer contexto**: offer.md + avatar.md + brand-voice.md + linkedin-strategy.md
2. **Auditar cada sección** del perfil contra los criterios de scoring (ver abajo)
3. **Puntuar** cada sección de 1 a 10
4. **Generar score total** ponderado
5. **Producir rewrites** para cada sección que puntúe < 7
6. **Validar** que los rewrites estén alineados al ICP, oferta y voz de Hans
7. **Entregar** reporte completo + textos listos para copiar/pegar

## Instrucciones

### Secciones a Auditar (con pesos)

| Sección | Peso | Criterio principal |
|---------|------|--------------------|
| **Headline** | 25% | Keywords del nicho + propuesta de valor clara + resultado medible |
| **About / Resumen** | 20% | Primera oración gancho + casos con números + CTA claro |
| **Featured** | 15% | Top 3 posts/recursos que demuestren autoridad |
| **Experience** | 10% | Momentum AI Academy como experiencia actual con descripción orientada a resultados |
| **Banner** | 10% | Propuesta de valor visual en 3-5 palabras + plataformas |
| **URL personalizada** | 5% | Limpia y memorable (linkedin.com/in/hansvilla o similar) |
| **Creator Mode** | 5% | Activado: sí/no (debe ser SÍ) |
| **Hashtags de perfil** | 5% | 5 hashtags del nicho exacto |
| **Skills & Endorsements** | 5% | Top 3 alineados a lo que vende |

### Framework "Perfil como Landing Page"

El perfil NO es una biografía. Es una landing page que convierte visitantes en seguidores o leads.

Cada sección del perfil cumple una función de conversión:

| Sección | Función de conversión | Analogía con landing page |
|---------|----------------------|---------------------------|
| **Banner** | Primera impresión visual | Hero image |
| **Headline** | Propuesta de valor en 1 línea | Headline de landing |
| **About** | Pitch completo + credibilidad + CTA | Body copy + testimonios + botón |
| **Featured** | Prueba social + recursos | Social proof + lead magnets |
| **Experience** | Credenciales que validan la autoridad | Trust badges |
| **Activity** | Contenido reciente que demuestra consistencia | Blog/contenido reciente |

**Principio central:** Cada visitante del perfil debe responder en 5 segundos:
1. Qué hace Hans
2. Para quién lo hace
3. Qué resultado puede esperar
4. Qué hacer ahora (CTA)

**Test de conversión:** Si un ingeniero industrial de LATAM con 8 años de experiencia visita el perfil de Hans, debe pensar "esto es exactamente para mí" en los primeros 5 segundos, sin scroll.

### Criterios de Scoring por Sección

**Headline (150 chars max):**
- 9-10: Incluye keywords del nicho + resultado específico + herramientas + diferenciador
- 7-8: Tiene keywords pero falta especificidad o resultado
- 4-6: Genérico, podría ser de cualquier persona
- 1-3: Solo cargo/empresa sin propuesta de valor

Ejemplo 10/10:
> "Enseño a ingenieros y analistas a crear automatizaciones con IA que generan $2,000-5,000 USD/mes | n8n + Claude"

Ejemplo 3/10:
> "Fundador de Momentum AI Academy"

**Regla headline:** El resultado del avatar va primero, el nombre de Hans/Momentum va después o no va. La headline es para el visitante, no para Hans.

**About (2,600 chars max):**
- Primera oración: debe funcionar como hook (antes del "ver más")
- Párrafo 1: qué hace Hans y para quién — con las PALABRAS del avatar (ver avatar.md)
- Párrafo 2: credibilidad con números reales — proyectos construidos, alumnos, resultados
- Párrafo 3: qué obtiene quien trabaja con él — resultado concreto y timeline
- Último párrafo: CTA claro (DM, newsletter, link)
- NO: muros de texto, lenguaje corporativo, biografía cronológica
- **Estructura recomendada (tipo mini-pitch):**
  1. Hook: dolor del avatar en sus propias palabras
  2. Puente: "Yo ayudo a [avatar] a [resultado] usando [mecanismo]"
  3. Credibilidad: números reales, herramientas específicas, tiempo en el mercado
  4. Diferenciador: qué hace Hans que otros no (casos reales, no teoría, LATAM, español)
  5. CTA: qué hacer ahora (DM, link, seguir para aprender)

**Featured Section:**
- Mínimo 3 items pinneados
- Item 1: Mejor carrusel o post de autoridad técnica — el que demuestre que Hans SABE
- Item 2: Caso de éxito documentado de alumno/cliente — el que demuestre que FUNCIONA
- Item 3: Lead magnet, newsletter o link a la academia — el que CONVIERTA
- Cada item debe tener descripción personalizada, no genérica
- **Orden deliberado:** primero valor, luego prueba social, luego CTA

**Banner:**
- Propuesta de valor en 3-5 palabras legibles en mobile
- Colores alineados a la marca
- Handle de Instagram (@hansvilla.ai) visible
- NO: foto genérica, banner vacío, demasiado texto
- **Tip:** El banner debe complementar la headline, no repetirla. Si la headline dice qué, el banner puede decir para quién.

### Reglas de Optimización

1. **El algoritmo (Causal LLM) lee el perfil como documento** — cada palabra en headline, about y experience afecta a qué clusters te envía. Si el perfil dice "automatización IA + n8n + LATAM + monetización", el algoritmo te distribuye a ese cluster.

2. **Keywords que DEBEN estar en el perfil:**
   - automatización, IA, inteligencia artificial
   - n8n, Claude (herramientas específicas)
   - LATAM, profesionales técnicos
   - ingreso extra, monetizar, proyectos de automatización
   - ingenieros, analistas, contadores (el avatar)

3. **Tono del perfil:** Directo, con números, sin corporativismo. El perfil es una landing page personal — cada sección debe avanzar al visitante hacia seguir o enviar DM.

4. **Creator Mode es obligatorio día 1.** Sin Creator Mode:
   - No hay analytics de contenido
   - El botón muestra "Conectar" en vez de "Seguir"
   - No se desbloquea Newsletter ni Live
   - El perfil está configurado para networking cerrado, no para construir audiencia

5. **Frecuencia de reoptimización:**
   - Después de cambio de oferta → reoptimizar completo
   - Cada trimestre → auditoría rápida de headline + about
   - Cuando profile views bajan >20% → revisar keywords

### Alineación con ICP

Todo rewrite debe pasar este filtro:
- ¿Un ingeniero industrial de LATAM que gana $3,500/mes leería esto y pensaría "esto es para mí"?
- ¿Queda claro qué vende Hans sin tener que leer todo el about?
- ¿Hay al menos 1 número real (no inventado) que demuestre credibilidad?
- ¿El CTA es claro y no agresivo?

## Output (formato exacto)

```markdown
# Auditoría de Perfil LinkedIn — Hans Villalobos
Fecha: YYYY-MM-DD

## Score General: X/10

## Desglose por Sección

### Headline — X/10
**Actual:** [texto actual]
**Diagnóstico:** [qué funciona y qué no]
**Propuesta:** [nuevo texto listo para copiar]

### About — X/10
**Actual:** [resumen o texto completo]
**Diagnóstico:** [análisis]
**Propuesta:**
[Texto completo del About reescrito, listo para copiar/pegar]

### Featured — X/10
**Actual:** [qué hay pinneado]
**Diagnóstico:** [análisis]
**Propuesta:** [qué pinnear y en qué orden]

### Banner — X/10
**Actual:** [descripción]
**Diagnóstico:** [análisis]
**Propuesta:** [brief para diseño de banner]

### Creator Mode — X/10
**Estado:** Activado/No activado
**Acción:** [qué hacer]

### URL — X/10
**Actual:** [URL actual]
**Propuesta:** [URL sugerida]

### Hashtags de Perfil — X/10
**Actuales:** [lista]
**Propuestos:** [5 hashtags]

### Experience — X/10
**Diagnóstico:** [análisis]
**Propuesta:** [descripción reescrita de Momentum AI Academy]

### Skills — X/10
**Propuestos top 3:** [lista]

---

## Acciones Prioritarias (ordenadas por impacto)
1. [Acción más urgente]
2. [Segunda]
3. [Tercera]

## Textos Listos para Copiar/Pegar
[Todos los rewrites consolidados]
```

Guardar en: `outputs/linkedin/YYYY-MM-DD_auditoria-perfil.md`
