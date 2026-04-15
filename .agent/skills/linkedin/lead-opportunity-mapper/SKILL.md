---
name: linkedin-lead-opportunity-mapper
version: v1
description: Convierte señales de engagement en LinkedIn en oportunidades comerciales clasificadas — define scoring, distingue niveles de interés y prepara la información para que Hans o el equipo tomen acción.
---

# LinkedIn Lead Opportunity Mapper

## Cuándo usar este skill

- Después de una retro semanal que detectó interacciones relevantes
- Cuando Hans nota DMs, comentarios repetidos o profile views de personas interesantes
- Cuando el signal-researcher detecta señales de compra
- Mensualmente para consolidar el pipeline de oportunidades LinkedIn

## Cuándo NO usar este skill

- Para publicar contenido (usar post-writer o comment-engine)
- Para análisis de métricas generales (usar retro-analyst)
- Para outreach automatizado (NO existe esa infraestructura aún — solo preparar la información)
- Para leads de Meta Ads (usar skills del MEDIA BUYER)

## Inputs necesarios

- **Señales de engagement**: comentarios, DMs, profile views, conexiones nuevas
- **Contexto del lead**: cargo, empresa, industria (visible en LinkedIn)
- **Avatar target**: `memory/avatar.md` (para scoring)
- **Oferta**: `memory/offer.md` (para determinar fit)

## Workflow

1. **Recopilar señales** de engagement de la semana/mes
2. **Clasificar cada señal** según el framework de scoring
3. **Puntuar cada lead** potencial
4. **Categorizar** en los 4 niveles
5. **Generar fichas** de oportunidad para los leads calificados
6. **Sugerir próxima acción** para cada nivel
7. **Guardar** reporte en `outputs/linkedin/YYYY-MM-DD_lead-map.md`

## Instrucciones

### Framework de Scoring

Cada señal de interacción tiene un peso. Se suman para dar un score total.

| Señal | Puntos | Notas |
|-------|--------|-------|
| Like/reacción en 1 post | +1 | Mínima señal de interés |
| Like/reacción en 3+ posts | +3 | Patrón de seguimiento |
| Comentario genérico | +2 | "Buen post", "Interesante" |
| Comentario sustancioso | +5 | Agrega perspectiva, hace pregunta, comparte experiencia |
| Comentario con pregunta sobre automatización | +8 | Señal de dolor activo |
| Compartir post de Hans | +6 | Advocacy — valida ante su red |
| Enviar DM | +10 | Señal fuerte de interés personal |
| DM con pregunta sobre academia/servicios | +15 | Señal de compra directa |
| Profile view (repetido) | +3 | Curiosidad sobre Hans |
| Conexión nueva + mensaje personalizado | +7 | Intención de relación |
| Mención de Hans en su propio post | +10 | Advocacy pública |

### Los 4 Niveles de Lead

| Nivel | Score | Descripción | Próxima acción |
|-------|-------|-------------|----------------|
| **Simple Viewer** | 1-5 | Interacción pasiva, no hay señal clara de interés | Nada — seguir publicando contenido |
| **Engaged Peer** | 6-12 | Interacción recurrente, potencial de relación profesional | Comentar en SUS posts, construir relación |
| **Warm Lead** | 13-20 | Señales claras de interés en el tema de automatización | Responder con valor, ofrecer recurso gratuito, invitar a conversación |
| **Strong Buying Signal** | 21+ | Pregunta directa sobre servicios/academia, DM activo, dolor explícito | Hans contacta directamente con DM personalizado |

### Ficha de Oportunidad

Para cada lead con score > 12 (Warm Lead o superior):

```
## Lead: [Nombre]
Score: X puntos
Nivel: [Warm Lead / Strong Buying Signal]

### Perfil
- Cargo: [cargo actual]
- Empresa: [nombre y tamaño]
- Industria: [sector]
- Ubicación: [país/ciudad]
- Sub-avatar match: [1/2/3 o "no match"]

### Señales Detectadas
1. [Señal 1 — fecha, tipo, detalle]
2. [Señal 2 — fecha, tipo, detalle]
3. [Señal 3 — si aplica]

### Fit con Oferta
- ¿Encaja en Sub-avatar 1 o 2? [sí/no + por qué]
- ¿Tiene capacidad de pago estimada? [sí/probable/no claro]
- ¿Dolor visible? [cuál, basado en sus posts o comentarios]

### Próxima Acción Sugerida
[Acción específica que Hans debería tomar — ej: "Comentar en su último post sobre X", "Enviar DM personalizado mencionando Y", "Invitar a webinar/recurso gratuito"]
```

### Reglas del Lead Mapper

1. **NO automatizar outreach.** No hay infraestructura para esto. Solo preparar información y sugerir acciones que Hans ejecuta manualmente.

2. **NO ser agresivo.** LinkedIn penaliza el spam de DMs y la venta directa. Las acciones sugeridas deben ser naturales: comentar, compartir recurso, hacer pregunta genuina.

3. **Priorizar Sub-avatar 1.** Profesional técnico con background de ingeniería/análisis/contabilidad en empresa mediana/grande. Estos tienen mayor tasa de cierre documentada (ver avatar.md).

4. **Distinguir entre lead y peer.** No todo engaged peer es un lead potencial. Un creador de contenido que comenta mucho puede ser un peer valioso pero no un comprador. Eso tiene valor diferente.

5. **Documentar el dolor visible.** Si en sus comentarios o posts la persona menciona problemas que la academia resuelve (procesos manuales, reportes en Excel, falta de automatización), registrarlo como pain validado.

6. **Score se acumula en el tiempo.** Una persona que interactúa poco pero consistentemente (1 like/semana durante 2 meses) puede tener más potencial que una que comentó una vez y desapareció.

7. **Actualizar mensualmente.** Los leads se enfrían. Si alguien fue warm lead hace 2 meses y dejó de interactuar, bajar su score.

### Pipeline Simple

```
Simple Viewer → [contenido consistente] → Engaged Peer → [engagement recíproco] → Warm Lead → [valor + relación] → Strong Buying Signal → [Hans conecta]
```

El sistema de contenido + comentarios (post-writer + comment-engine) es lo que mueve personas a través del pipeline. El lead mapper solo OBSERVA y CLASIFICA — no interviene en el proceso de engagement.

## Output (formato exacto)

```markdown
# Mapa de Oportunidades LinkedIn
Período: [fecha inicio] — [fecha fin]

## Resumen
- Leads totales detectados: X
- Strong Buying Signals: X
- Warm Leads: X
- Engaged Peers: X

## Strong Buying Signals (prioridad inmediata)
[Fichas completas de cada uno]

## Warm Leads (construir relación)
[Fichas completas de cada uno]

## Engaged Peers Notables
[Lista breve con nombre, cargo, tipo de interacción]

## Acciones Prioritarias para Hans
1. [Acción más urgente con lead más caliente]
2. [Segunda acción]
3. [Tercera acción]

## Notas para el Pipeline
[Observaciones sobre tendencias — ¿de qué industria vienen más leads? ¿qué tipo de contenido genera más señales?]
```

Guardar en: `outputs/linkedin/YYYY-MM-DD_lead-map.md`
