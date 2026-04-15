---
name: linkedin-signal-detector
version: v1
description: Rutina semanal para detectar senales de interes en LinkedIn (profile views, comentarios recurrentes, shares) y convertirlas en acciones concretas de engagement o warm outreach.
---

# LinkedIn Signal Detector

## Cuando usar este skill

- Cada semana como rutina (idealmente lunes o viernes, 15 minutos)
- Cuando Hans quiere identificar quien esta mostrando interes real en su perfil/contenido
- Antes de ejecutar warm outreach (este skill alimenta el skill `linkedin/warm-outreach`)
- Cuando profile views suben o bajan significativamente
- Cuando un post genera engagement inusual y quieres saber QUIEN interactuo

## Cuando NO usar este skill

- Para crear contenido (usar `linkedin/post-writer`)
- Para investigar tendencias de mercado (usar `linkedin/signal-researcher`)
- Para enviar mensajes masivos (NO hacemos eso)
- Para analizar metricas de performance de posts (usar `linkedin/retro-analyst`)

## Inputs necesarios

- **Profile views de la semana** (LinkedIn Analytics > Analitica > Quien vio tu perfil)
- **Lista de personas que comentaron** en los posts de la semana
- **Nuevas conexiones recibidas** de la semana
- **DMs recibidos** (si hubo)
- **Posts compartidos/guardados** por otros (si visible)
- **Contexto**: `memory/avatar.md` (para saber si las senales vienen del avatar target)

## Workflow

1. **Recopilar datos**: Hans comparte las senales de la semana (profile views, comentarios, conexiones nuevas)
2. **Clasificar cada senal** segun el sistema de scoring (ver abajo)
3. **Filtrar por avatar match**: solo las senales que vienen del Sub-avatar 1 o 2 son accionables
4. **Asignar accion** a cada senal calificada
5. **Producir lista de acciones** ordenada por prioridad
6. **Actualizar tracking** (ver template `templates/linkedin-weekly-signals.md`)
7. **Guardar** en `outputs/linkedin/YYYY-MM-DD_signal-detection.md`

## Instrucciones

### Tipos de Senales y Que Significan

| Senal | Que indica | Fuerza | Accion recomendada |
|-------|-----------|--------|-------------------|
| **Visita al perfil** (1 vez) | Curiosidad basica | Baja | Revisar si es avatar target. Si si, visitar su perfil de vuelta. |
| **Visita al perfil** (2+ veces) | Interes activo | Alta | Enviar conexion con nota personalizada o DM si ya conectados |
| **Comentario en post** (sustancioso) | Engagement real | Alta | Responder con profundidad + visitar su perfil + considerar DM |
| **Comentario en post** (generico "Buen post") | Engagement superficial | Baja | Responder brevemente, no priorizar |
| **Comentarios en 2+ posts** | Seguidor comprometido | Muy Alta | DM personalizado agradeciendolo + pregunta genuina |
| **Share/Repost de contenido** | Advocacy activo | Muy Alta | Agradecer publicamente + DM + considerar para red de aliados |
| **Nueva conexion + visita perfil** | Interes deliberado | Alta | Revisar perfil, enviar mensaje de bienvenida personalizado |
| **DM espontaneo** | Interes directo | Maxima | Responder en <24h + iniciar conversacion genuina |
| **Save/Bookmark** (si visible) | Valor percibido alto | Media | No accionable directamente pero indica que el contenido tiene utilidad practica |

### Sistema de Scoring de Senales

Cada senal se puntua de 1 a 5:

| Score | Criterio | Ejemplo |
|-------|---------|---------|
| **5** | Senal directa de interes comercial | DM preguntando por servicios, "como me inscribo" |
| **4** | Engagement repetido del avatar target | Comenta en 3+ posts, visita perfil 2+ veces |
| **3** | Engagement significativo unico | Comentario sustancioso, share, conexion con nota |
| **2** | Senal debil pero del avatar correcto | Vista de perfil unica, like, conexion sin nota |
| **1** | Senal de persona fuera del avatar | Engagement de bots, recruiters, vendedores |

**Regla:** Solo las senales con score 3+ generan acciones proactivas.

### Filtro de Avatar Match

Antes de actuar sobre una senal, verificar:
- Es profesional tecnico, ingeniero, analista, contador? (Sub-avatar 1)
- Tiene 6+ anos de experiencia?
- Esta en LATAM?
- Trabaja en empresa (no freelancer ni desempleado)?

Si cumple 3 de 4 criterios = Avatar Match.
Si cumple 2 = Avatar Parcial (actuar con menor prioridad).
Si cumple 0-1 = No Avatar (no invertir tiempo proactivo).

### Acciones por Prioridad

**Prioridad 1 (hacer hoy):**
- Responder DMs espontaneos
- Responder comentarios sustanciosos de personas con score 4-5
- Enviar DM a personas que comentaron en 2+ posts

**Prioridad 2 (hacer esta semana):**
- Enviar conexion personalizada a visitantes del perfil con avatar match
- Responder comentarios de score 3
- Visitar perfiles de personas que visitaron el tuyo

**Prioridad 3 (opcional):**
- Agradecer shares/reposts
- Revisar nuevas conexiones y enviar mensaje de bienvenida

### Lo Que NO Hacer

1. **No enviar mensajes masivos** — todo debe ser personalizado y manual
2. **No contactar a personas que no mostraron senal** — eso es cold outreach
3. **No vender en el primer mensaje** — la senal indica interes, no disposicion de compra
4. **No enviar mas de 10-15 DMs/semana** — calidad > cantidad
5. **No ignorar senales de personas fuera del avatar** — responder con cortesia, pero no invertir tiempo proactivo

### Patrones a Detectar Semana a Semana

Despues de 3+ semanas de tracking, buscar:
- Que tipo de contenido genera mas profile views?
- De que industria vienen las senales mas fuertes?
- Que cargos aparecen mas en profile views?
- Hay personas que aparecen repetidamente? (potenciales leads calientes)
- Las senales aumentan o disminuyen? (indicador de salud del contenido)

## Output (formato exacto)

```markdown
# Signal Detection — Semana del YYYY-MM-DD

## Resumen de Senales
- Profile views: X (vs X semana anterior)
- Comentarios totales: X (sustanciosos: X)
- Nuevas conexiones: X (avatar match: X)
- DMs recibidos: X
- Shares/Reposts: X

## Senales de Alta Prioridad (Score 4-5)
### [Nombre de la persona]
- **Senal:** [que hizo]
- **Perfil:** [cargo, empresa, anos experiencia]
- **Avatar Match:** Si/Parcial/No
- **Score:** X/5
- **Accion:** [que hacer]

[repetir para cada senal alta]

## Senales de Media Prioridad (Score 3)
| Persona | Senal | Avatar Match | Accion |
|---------|-------|-------------|--------|
| [nombre] | [que hizo] | Si/No | [accion] |

## Acciones de Esta Semana
### Hacer Hoy
1. [accion + persona]

### Hacer Esta Semana
1. [accion + persona]

## Patrones Detectados
[Si hay 3+ semanas de datos, notar tendencias]

## Metricas de Tracking
| Semana | Profile Views | Comentarios Sust. | Conexiones Avatar | DMs Inbound |
|--------|-------------|-------------------|-------------------|-------------|
| Actual | X | X | X | X |
| Anterior | X | X | X | X |
```

Guardar en: `outputs/linkedin/YYYY-MM-DD_signal-detection.md`
