---
name: linkedin-retro-analyst
version: v1
description: Revisa resultados semanales de LinkedIn — detecta patrones, identifica qué doblar y qué cortar, prioriza señales profundas sobre vanity metrics y propone ajustes para la próxima semana.
---

# LinkedIn Retro Analyst

## Cuándo usar este skill

- Al final de cada semana de publicación en LinkedIn (viernes o lunes)
- Cuando Hans comparte métricas o screenshots de LinkedIn analytics
- Cuando hay una caída o subida notable de performance
- Mensualmente para hacer retro más profunda

## Cuándo NO usar este skill

- Para crear contenido (usar `linkedin/post-writer`)
- Para analizar métricas de Meta Ads (usar skills del MEDIA BUYER)
- Para estrategia general (usar `linkedin/authority-builder`)

## Inputs necesarios

- **Métricas de la semana** (Hans debe proporcionar o compartir screenshots):
  - Impresiones por post
  - Engagement rate por post
  - Profile views del período
  - Follower growth
  - Comentarios (cantidad y calidad)
  - Saves y shares (si disponible)
- **Posts publicados**: qué se publicó, cuándo, qué formato, qué pilar
- **Contexto de memoria**: winning-content.md, learnings.md
- **Estrategia actual**: docs/linkedin-strategy.md

## Workflow

1. **Recibir datos** de la semana (métricas + posts publicados)
2. **Analizar por post** — qué funcionó y qué no, con hipótesis
3. **Analizar tendencias** — patrones across posts
4. **Evaluar métricas que importan** (no vanity metrics)
5. **Comparar con benchmarks** del nicho
6. **Generar recomendaciones** priorizadas para la próxima semana
7. **Actualizar memoria** si hay hallazgos confirmados
8. **Guardar reporte** en `outputs/linkedin/YYYY-MM-DD_retro-semanal.md`

## Instrucciones

### Métricas que Importan vs. Vanity Metrics

| Métrica | Importancia | Por qué |
|---------|-----------|---------|
| **Comentarios sustanciosos** | ALTA | Señal de resonancia real. El 360Brew amplifica posts con discusión bidireccional (5.2x) |
| **Profile views** | ALTA | Indica que el contenido genera curiosidad sobre Hans como persona/marca |
| **Follower growth** | ALTA | Métrica compuesta de todo lo demás — crece si el contenido es consistente |
| **Saves/Bookmarks** | ALTA | Señal de que el contenido tiene valor de referencia |
| **Shares/Reposts** | ALTA | Amplificación orgánica real |
| **Impresiones** | MEDIA | Útil para tendencia, pero no indica calidad del engagement |
| **Likes/Reactions** | BAJA | Fáciles de dar, no indican interés profundo |
| **Engagement rate %** | MEDIA | Útil como ratio, pero depende del denominador (impresiones) |

### Benchmarks de Referencia (LinkedIn 2025-2026)

| Métrica | Benchmark general | Benchmark nicho técnico LATAM |
|---------|------------------|------------------------------|
| Engagement rate | 6.2% promedio | 4-8% (varía por formato) |
| Carrusel engagement | 21.77% | El más alto de todos los formatos |
| Video nativo engagement | 7.35% | Segundo lugar |
| Texto largo engagement | 3-5% | Depende del hook |
| Follower growth semanal | 1-3% | En fase fundación puede ser mayor |
| Profile views / semana | Variable | Correlaciona con posts publicados + engagement |

### Framework de Análisis por Post

Para cada post publicado:

```
POST: [título/tema]
FORMATO: [carrusel / texto / poll / video]
PILAR: [educación / prueba social / autoridad / proceso / engagement]
DÍA/HORA: [cuándo se publicó]

MÉTRICAS:
- Impresiones: X
- Engagement rate: X%
- Comentarios: X (calidad: alta/media/baja)
- Saves: X
- Profile views generados: ~X

ANÁLISIS:
- Hook effectiveness: [¿La primera línea generó clics en "ver más"?]
- Engagement quality: [¿Los comentarios son sustanciosos o superficiales?]
- Audience match: [¿Quiénes interactuaron — son del avatar target?]

HIPÓTESIS: [Por qué funcionó o no funcionó]
ACCIÓN: [Doblar / Iterar / Cortar / Probar variante]
```

### Decisiones de Acción

| Señal | Acción |
|-------|--------|
| Post con >2x engagement promedio + comentarios del avatar | **DOBLAR**: hacer más de este tipo/formato/ángulo |
| Post con engagement promedio pero 0 comentarios del avatar | **ITERAR**: mismo formato, diferente ángulo o hook |
| Post con <0.5x engagement promedio | **ANALIZAR**: ¿fue el hook? ¿el formato? ¿el horario? ¿el tema? |
| Post con muchas impresiones pero bajo engagement | **HOOK ISSUE**: el tema tiene interés pero la ejecución no enganchó |
| Post con pocos impresiones pero alto engagement | **DISTRIBUCIÓN ISSUE**: contenido bueno, algo falló en el timing o la golden hour |
| Poll con >100 respuestas | **OPORTUNIDAD**: hacer follow-up post con los resultados |
| Post que genera DMs o profile views altos | **SEÑAL DE LEAD**: documentar el ángulo que generó esto |

### Análisis Semanal de Tendencias

Buscar patrones across posts:
1. **¿Qué formato tuvo mejor performance?** → Aumentar frecuencia
2. **¿Qué pilar generó más engagement?** → Reforzar ese pilar
3. **¿Qué día/hora funcionó mejor?** → Ajustar calendario
4. **¿Los comentarios son del avatar target?** → Si no, ajustar hooks
5. **¿El follower growth fue positivo?** → Si estancado, revisar frecuencia de comentarios (método 5-5-5)

### KPIs de Señales y Conversión (complementarios a engagement)

Además de las métricas de contenido, trackear semanalmente:

| Métrica de señales | Qué indica | Benchmark |
|-------------------|-----------|-----------|
| **Profile views / semana** | Interés en Hans como persona | Tendencia creciente semana a semana |
| **Nuevas conexiones del avatar** | Alcance en la audiencia correcta | >5/semana en fase fundación |
| **DMs inbound** | Interés directo no solicitado | Cualquier DM del avatar = señal fuerte |
| **Warm conversations activas** | Relaciones en construcción | >3 activas por semana |
| **Comentaristas recurrentes** | Comunidad formándose | Identificar top 5-10 recurrentes |
| **Calls agendadas desde LinkedIn** | Conversión real del canal | Trackear desde que empiecen |

**Conexión con otros skills:**
- Los datos de señales alimentan al `linkedin/signal-detector`
- Los ángulos ganadores alimentan al `linkedin/message-fit-tester`
- Los profile views y DMs validan la efectividad del perfil (ver `linkedin/profile-optimizer`)
- Las conexiones del avatar validan las listas del `linkedin/icp-mapper`

### Actualización de Memoria

Si el análisis revela algo confirmado (no una hipótesis):
- Agregar a `memory/winning-content.md` si un post fue claramente ganador
- Agregar a `memory/learnings.md` si se descubrió un patrón de LinkedIn
- Actualizar la skill de `authority-builder` si la cadencia o formatos deben cambiar

**Regla:** Solo actualizar memoria con patrones confirmados (3+ datapoints), no con un solo post.

## Output (formato exacto)

```markdown
# Retro Semanal LinkedIn
Período: [fecha inicio] — [fecha fin]

## Resumen Ejecutivo
[2-3 líneas: qué funcionó, qué no, tendencia general]

## Performance por Post
[Análisis de cada post con el framework descrito arriba]

## Tendencias de la Semana
- **Mejor formato:** [cuál y por qué]
- **Mejor pilar:** [cuál y por qué]
- **Mejor horario:** [cuál]
- **Audiencia que interactúa:** [descripción — ¿es el avatar target?]

## Decisiones para Próxima Semana
| Acción | Justificación |
|--------|--------------|
| **Doblar:** [qué] | [por qué] |
| **Iterar:** [qué] | [por qué] |
| **Cortar:** [qué] | [por qué] |
| **Probar:** [qué nuevo] | [hipótesis] |

## Métricas Acumuladas
- Seguidores: X (+ X esta semana)
- Profile views promedio: X/semana
- Engagement rate promedio: X%

## Métricas de Señales y Conversión
| Métrica | Esta semana | Semana anterior | Tendencia |
|---------|------------|----------------|-----------|
| Profile views | X | X | ↑/↓/→ |
| Conexiones del avatar | X | X | ↑/↓/→ |
| DMs inbound | X | X | ↑/↓/→ |
| Warm conversations activas | X | X | ↑/↓/→ |
| Comentaristas recurrentes | X | X | ↑/↓/→ |
| Calls agendadas | X | X | ↑/↓/→ |

## Actualización de Memoria
[Si hay algo confirmado que actualizar — o "Sin actualizaciones esta semana"]
```

Guardar en: `outputs/linkedin/YYYY-MM-DD_retro-semanal.md`
