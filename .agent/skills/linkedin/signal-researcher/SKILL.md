---
name: linkedin-signal-researcher
version: v1
description: Detecta temas, pains, objeciones, lenguaje de mercado y oportunidades comerciales analizando señales de LinkedIn y datos del proyecto para alimentar la creación de contenido y el mapeo de leads.
---

# LinkedIn Signal Researcher

## Cuándo usar este skill

- Antes de planificar el calendario de contenido LinkedIn de la semana/mes
- Cuando Hans quiere saber qué temas están resonando en su nicho
- Para detectar nuevos pains, objeciones o lenguaje que usa el avatar
- Para alimentar al `linkedin/post-writer` con datos frescos
- Para detectar oportunidades comerciales en conversaciones públicas
- Cuando el INVESTIGADOR necesita orientar una búsqueda hacia señales de LinkedIn

## Cuándo NO usar este skill

- Para escribir posts (usar `linkedin/post-writer`)
- Para investigación general de mercado fuera de LinkedIn (usar skills del INVESTIGADOR)
- Para analizar métricas propias (usar `linkedin/retro-analyst`)

## Inputs necesarios

- **Avatar**: `memory/avatar.md` (para saber qué señales buscar)
- **Contenido ganador**: `memory/winning-content.md` (para detectar patrones)
- **Aprendizajes**: `memory/learnings.md` (para no repetir investigaciones)
- **Tema o dirección** (opcional): Hans puede dar un enfoque específico

## Workflow

1. **Leer contexto** de avatar y winning-content
2. **Definir 3-5 señales a buscar** (ver tipos de señales abajo)
3. **Investigar** usando Perplexity (sonar-pro) con queries en español orientadas a LinkedIn LATAM
4. **Clasificar señales** por tipo y prioridad
5. **Extraer lenguaje del avatar** — frases exactas, preguntas, objeciones
6. **Mapear oportunidades de contenido** — qué posts crear a partir de lo encontrado
7. **Mapear oportunidades comerciales** — si hay señales de compra, pasarlas al lead-opportunity-mapper
8. **Producir reporte** estructurado
9. **Guardar** en `outputs/research/YYYY-MM-DD_linkedin-signals.md`

## Instrucciones

### Tipos de Señales a Detectar

| Tipo | Qué buscar | Para qué sirve |
|------|-----------|----------------|
| **Pains activos** | Preguntas frecuentes del avatar sobre automatización, IA, herramientas | Contenido que responde dolor real |
| **Objeciones** | "No tengo tiempo", "Es caro", "No sé programar" | Contenido que desmonta objeciones |
| **Lenguaje del avatar** | Cómo describe su problema, qué palabras usa | Hooks con las palabras exactas del avatar |
| **Tendencias del nicho** | Temas trending en IA/automatización/no-code en LATAM | Contenido oportuno de trend commentary |
| **Competidores** | Qué publican otros creadores del nicho en LinkedIn | Gaps de contenido, ángulos no cubiertos |
| **Señales de compra** | "Alguien sabe de...", "Busco quien me ayude a...", "Recomiendan un curso de..." | Lead opportunity mapping |

### Fuentes de Señales

**Dentro del proyecto (leer primero):**
- `memory/avatar.md` → objeciones documentadas, pains validados
- `memory/winning-content.md` → patrones de contenido que ya funcionó
- `memory/learnings.md` → insights de investigaciones previas
- `outputs/research/` → reportes recientes del INVESTIGADOR

**Externas (vía Perplexity sonar-pro):**
- Búsquedas: "preguntas frecuentes automatización IA LinkedIn LATAM 2026"
- Búsquedas: "tendencias automatización empresas LATAM [mes] [año]"
- Búsquedas: "objeciones cursos automatización IA latinoamérica"
- Búsquedas: "qué publican creadores de IA en LinkedIn español"
- Búsquedas específicas por industria del avatar: manufactura, finanzas, logística, TI

### Priorización de Señales

Clasificar cada señal encontrada:

| Prioridad | Criterio | Acción |
|-----------|---------|--------|
| **Alta** | Pain activo del Sub-avatar 1 + no cubierto por contenido existente | Crear post esta semana |
| **Media** | Tendencia del nicho + alineada a pilares de Hans | Agregar al calendario |
| **Baja** | Interesante pero no directamente accionable | Documentar para referencia futura |
| **Oportunidad comercial** | Señal de compra explícita o implícita | Pasar a lead-opportunity-mapper |

### Extracción de Lenguaje del Avatar

Cuando encuentres las palabras exactas que usa el avatar para describir su problema:

```
FRASE DEL AVATAR: "[frase textual]"
CONTEXTO: [dónde se encontró]
PAIN QUE REFLEJA: [dolor subyacente]
USO SUGERIDO: [hook de post / ángulo de contenido / copy de ad]
```

Esto es ORO para el post-writer — el contenido más efectivo usa las palabras exactas del avatar, no las del creador.

### Reglas de Investigación

1. **Siempre buscar en español** — el avatar de Hans es LATAM
2. **Agregar "2026" o "últimos meses" a las queries** para recencia
3. **No asumir que LinkedIn funciona igual que en mercado angloparlante** — LATAM tiene dinámicas propias
4. **Priorizar señales que puedan convertirse en contenido accionable** — no acumular datos sin propósito
5. **Si una señal contradice lo documentado en avatar.md**, marcarla como "posible actualización de avatar" y notificar al ESTRATEGA
6. **Usar Perplexity via Node.js** (curl falla en Windows con JSON complejo — ver learnings.md)

## Output (formato exacto)

```markdown
# Reporte de Señales LinkedIn
Fecha: YYYY-MM-DD
Enfoque: [tema específico o "general"]

## Señales de Alta Prioridad
### Señal 1: [título]
- **Tipo:** [pain / objeción / tendencia / competidor / señal de compra]
- **Detalle:** [qué se encontró]
- **Fuente:** [de dónde viene]
- **Acción sugerida:** [qué hacer con esto]

[repetir para cada señal alta]

## Lenguaje del Avatar Detectado
| Frase | Contexto | Pain | Uso sugerido |
|-------|---------|------|-------------|
| "[frase]" | [dónde] | [dolor] | [hook/ángulo/copy] |

## Oportunidades de Contenido
1. [Idea de post basada en señal + formato recomendado]
2. [...]
3. [...]

## Oportunidades Comerciales
[Si hay señales de compra, listarlas con contexto]

## Señales Secundarias
[Lista breve de señales media/baja prioridad]

## Actualización Sugerida de Memoria
[Si algún hallazgo debería actualizar avatar.md o learnings.md]
```

Guardar en: `outputs/research/YYYY-MM-DD_linkedin-signals.md`
