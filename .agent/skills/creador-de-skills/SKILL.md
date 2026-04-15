---
name: creador-de-skills
version: v2
description: Diseña y genera nuevas Skills para el Media Buyer Team. Produce estructura de carpetas, SKILL.md con frontmatter estandarizado y lógica reutilizable adaptada al dominio de marketing, contenido y ads.
---

# Creador de Skills — Media Buyer Team

## Cuándo usar este skill

- Hans repite el mismo tipo de pedido más de 2 veces en sesiones distintas.
- Un agente identifica un proceso que produce buenos resultados y quiere estandarizarlo.
- Se necesita convertir un prompt largo o flujo complejo en un procedimiento reutilizable.
- Se detecta un patrón recurrente en: creación de guiones, análisis de ads, investigación de tendencias, mejora de oferta.
- Hans pide explícitamente crear o mejorar una skill.

## Cuándo NO usar este skill

- El pedido es una tarea única que no se va a repetir.
- El proceso tiene menos de 3 pasos claramente definidos (un simple template basta).
- La skill que se pide ya existe — en ese caso, editar la existente.
- El proceso requiere decisión humana en cada paso (no es automatizable ni estandarizable).

## Inputs necesarios

- **Objetivo**: Qué debe lograr la skill. Qué problema resuelve.
- **Dominio**: (contenido / ads / investigación / estrategia / sistema)
- **Contexto**: (Opcional) Ejemplos de outputs buenos, pedidos previos de Hans, referencia de skills similares.
- **Nivel de Libertad**: Alta (brainstorming), Media (contenido estructurado), Baja (proceso exacto con pasos fijos).

## Workflow

1. **Analizar**: Leer el pedido. Identificar dominio, objetivo, triggers y nivel de libertad adecuado.
2. **Verificar duplicados**: Revisar `.agent/skills/` para asegurarse de que no existe una skill similar. Si existe, proponer edición en vez de creación.
3. **Nombrar**: Definir `nombre-kebab-case` (máx. 40 caracteres, solo minúsculas y guiones).
4. **Estructurar**: Decidir qué archivos adicionales necesita (recursos/, ejemplos/, scripts/).
5. **Redactar**: Generar `SKILL.md` siguiendo la plantilla estricta de esta skill.
6. **Validar**: Verificar frontmatter, secciones obligatorias y directrices de calidad antes de entregar.
7. **Entregar**: Presentar el contenido completo con ruta clara. Esperar confirmación antes de escribir el archivo.
8. **Registrar**: Anotar la nueva skill en `memory/learnings.md` con fecha y propósito.

## Instrucciones

### 1. Estructura de Carpetas

Cada skill vive en: `.agent/skills/<nombre-del-skill>/`

```
.agent/skills/<nombre>/
├── SKILL.md           ← Obligatorio siempre
├── recursos/          ← Opcional: guías de referencia, brand guidelines, datos
├── ejemplos/          ← Opcional: outputs de calidad para usar como referencia
└── scripts/           ← Opcional: utilidades bash o código auxiliar
```

### 2. Frontmatter Obligatorio

```yaml
---
name: <nombre-kebab-case-max-40-chars>
version: v1
description: <descripción-en-tercera-persona-max-220-chars-operativa-no-marketing>
---
```

Reglas:
- `name`: solo minúsculas y guiones, sin espacios ni caracteres especiales.
- `version`: empieza en `v1`, incrementa al editar significativamente.
- `description`: describe qué hace el skill de forma operativa. Evitar adjetivos vacíos.

### 3. Secciones Obligatorias (en este orden)

1. `# Título del Skill`
2. `## Cuándo usar este skill` — Lista de triggers concretos y observables.
3. `## Cuándo NO usar este skill` — Anti-triggers para evitar uso incorrecto.
4. `## Inputs necesarios` — Datos requeridos para operar el skill.
5. `## Workflow` — Pasos numerados, fases, o ciclo Plan/Ejecutar/Validar.
6. `## Instrucciones` — Reglas, principios, decisiones, manejo de errores.
7. `## Output (formato exacto)` — Plantilla de respuesta que el agente debe seguir.

### 4. Niveles de Libertad

- **Alta (Brainstorming/Ideación)**: Heurísticas generales. El agente tiene flexibilidad creativa. Ejemplos: generación de ideas de contenido, ángulos de ads.
- **Media (Contenido estructurado)**: Plantillas con estructura fija pero contenido variable. Ejemplos: guiones de reels, secuencias de stories, calendarios.
- **Baja (Procesos exactos)**: Pasos fijos, validaciones estrictas, poco margen de variación. Ejemplos: análisis de métricas de ads, publicación de contenido, setup de campañas.

### 5. Dominios del Media Buyer Team

Al crear una skill, identifica a qué dominio pertenece para ubicarla conceptualmente:

| Dominio | Ejemplos de skills |
|---------|-------------------|
| `contenido` | guiones-reels, story-sequences, content-calendar |
| `ads` | ad-scripts, analisis-campañas, ab-testing |
| `investigacion` | research-perplexity, analisis-competidores, tendencias-ia |
| `estrategia` | mejora-oferta, refinamiento-avatar, posicionamiento |
| `sistema` | creador-de-skills, actualizar-memoria, registro-aprendizajes |

### 6. Manejo de Errores

- Si los inputs son insuficientes: preguntar antes de generar. No asumir.
- Si la skill resultante es muy genérica: agregar ejemplos concretos del negocio de Hans.
- Si el output no cumple las secciones obligatorias: regenerar antes de entregar.
- Si existe una skill parecida: mostrar la existente y preguntar si editar o crear nueva.

## Output (formato exacto)

Al generar una skill nueva, la respuesta debe seguir este formato:

---

**Nueva skill:** `nombre-del-skill`
**Ruta:** `.agent/skills/nombre-del-skill/SKILL.md`
**Dominio:** contenido / ads / investigación / estrategia / sistema
**Nivel de libertad:** Alta / Media / Baja

**Contenido de SKILL.md:**

```markdown
---
name: nombre-del-skill
version: v1
description: Descripción operativa de qué hace el skill.
---

# Título del Skill

## Cuándo usar este skill
...

## Cuándo NO usar este skill
...

## Inputs necesarios
...

## Workflow
...

## Instrucciones
...

## Output (formato exacto)
...
```

*(Opcional) Archivos adicionales sugeridos:*
- `recursos/ejemplo.md`: [descripción breve]

---

**Acción requerida:** Confirmar para escribir el archivo. ¿Procedo?
