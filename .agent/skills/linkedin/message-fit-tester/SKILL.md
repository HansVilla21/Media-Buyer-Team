---
name: linkedin-message-fit-tester
version: v1
description: Framework de A/B testing de angulos de contenido LinkedIn — testea 3 angulos por tema durante 3 semanas para descubrir que messaging resuena con el avatar, basado en datos reales no intuicion.
---

# LinkedIn Message-Fit Tester

## Cuando usar este skill

- Cuando Hans no sabe que tipo de contenido le funciona mejor (fase de descubrimiento)
- Cuando quiere probar un tema nuevo y no sabe desde que angulo abordarlo
- Cuando un pilar de contenido no esta generando engagement esperado
- Cada 4-6 semanas como ciclo de optimizacion continua
- Cuando cambia el avatar o la oferta y hay que recalibrar el messaging

## Cuando NO usar este skill

- Si ya hay datos claros de que funciona (usar `winning-content.md`)
- Para crear un post individual (usar `linkedin/post-writer`)
- Para analizar metricas generales (usar `linkedin/retro-analyst`)
- Si Hans tiene menos de 3 posts publicados (necesita baseline primero)

## Inputs necesarios

- **Tema a testear**: sobre que quiere probar angulos (ej: "automatizacion de reportes", "por que n8n es mejor que Zapier", "como monetizar IA sin programar")
- **Historial de contenido**: `memory/winning-content.md` + posts recientes
- **Avatar**: `memory/avatar.md` (para saber que angulos podrian resonar)
- **Metricas baseline**: engagement rate promedio de los ultimos 10 posts

## Workflow

1. **Definir el tema** a testear
2. **Generar 3 angulos distintos** del mismo tema (ver framework de angulos abajo)
3. **Crear 3 posts** — uno por angulo, mismo formato para control (idealmente texto largo)
4. **Publicar 1 por semana** durante 3 semanas
5. **Trackear metricas especificas** de cada post (ver metricas del test)
6. **Comparar resultados** al final del ciclo
7. **Declarar ganador** y documentar en `memory/winning-content.md`
8. **Iterar**: doblar el angulo ganador, descartar los que no funcionaron

## Instrucciones

### Framework de Angulos

Para cualquier tema, generar 3 angulos usando estos lentes:

| Angulo | Que hace | Ejemplo con tema "automatizacion de reportes" |
|--------|---------|----------------------------------------------|
| **Educativo directo** | Ensena paso a paso como hacerlo | "Asi automatice un reporte semanal con n8n en 45 minutos" |
| **Dolor/Problema** | Empieza desde el dolor del avatar | "Pierdes 5 horas semanales en reportes manuales que una IA hace en 3 minutos" |
| **POV/Contrario** | Toma postura contra una creencia comun | "Los reportes automaticos NO son el futuro. Los reportes que se generan SOLOS si." |

**Angulos alternativos** (si los 3 anteriores no aplican):

| Angulo | Que hace | Ejemplo |
|--------|---------|---------|
| **Story/Caso real** | Cuenta una historia con resultado | "Un contador me dijo: 'pierdo 3 dias al mes en esto'. Le automatice todo en una tarde." |
| **Comparacion** | Compara herramientas o enfoques | "Excel vs n8n para reportes: por que tu jefe deberia preocuparse" |
| **Trend** | Conecta con algo que esta pasando ahora | "GPT-4o puede leer tus hojas de calculo. Esto cambia todo para equipos financieros." |

### Reglas del Test

1. **Control de variables:** Los 3 posts deben tener el MISMO formato (ej: todos texto largo, o todos carrusel). Si mezclas formato, no sabes si el resultado fue por el angulo o por el formato.
2. **Mismo dia/hora:** Publicar los 3 el mismo dia de la semana y a la misma hora (ej: los 3 un martes a las 9am). Esto controla el efecto del timing.
3. **Minimo 3 semanas:** Un solo post no es dato. Necesitas al menos 3 datapoints para detectar patron.
4. **No promocionar uno mas que otro:** Aplicar el mismo metodo 5-5-5 y golden hour a los 3 posts.
5. **Registrar variables externas:** Si un dia hubo un evento (ej: noticia de IA viral) que pudo afectar las metricas, anotarlo.

### Metricas del Test

Para cada post del test, trackear:

| Metrica | Por que importa |
|---------|----------------|
| **Comentarios sustanciosos** | La senal mas fuerte de que el angulo resonó — indica que el avatar PIENSA sobre lo que dijiste |
| **Profile views generados** | Indica que el contenido genero curiosidad sobre Hans como persona |
| **Saves/Bookmarks** | Indica que el contenido tiene valor de referencia (lo quieren guardar para despues) |
| **Engagement rate** | Metrica general, util como comparacion pero no definitiva |
| **Tipo de persona que comento** | Es el avatar target o son randos? Un post con 5 comentarios del avatar > 20 de personas random |

**Metrica de vanidad (NO usar como criterio de decision):** Likes/Reactions, Impresiones brutas.

### Declarar Ganador

Al final del ciclo de 3 semanas:

| Resultado | Decision |
|-----------|---------|
| Un angulo tiene 2x+ comentarios sustanciosos que los otros | **Ganador claro.** Doblar este angulo las proximas 2-3 semanas. |
| Los 3 angulos tienen performance similar | **No hay diferenciador.** El tema es bueno pero el angulo no importa tanto. Probar formatos diferentes. |
| Ningun angulo genera engagement | **El tema no resuena.** Descartarlo y probar un tema diferente. |
| Un angulo genera engagement de no-avatar | **Engagement equivocado.** El angulo atrae gente pero no la correcta. Descartar y probar uno mas niched. |

### Documentacion del Test

Registrar todo en `outputs/linkedin/YYYY-MM-DD_angle-test.md` usando el template:

```
CICLO DE TEST #X
Tema: [tema]
Periodo: [semana 1] a [semana 3]

ANGULO A: [nombre del angulo]
- Post: [link o referencia]
- Comentarios sustanciosos: X
- Profile views post-publicacion: X
- Saves: X
- Engagement rate: X%
- Tipo de audiencia: [avatar/no-avatar/mixto]

ANGULO B: [nombre del angulo]
[mismas metricas]

ANGULO C: [nombre del angulo]
[mismas metricas]

GANADOR: [A/B/C/Ninguno]
RAZON: [por que]
ACCION: [doblar/iterar/descartar/probar nuevo tema]
```

### Ciclo Continuo

El message-fit testing no es un evento unico. Es un ciclo:

1. **Testear** 3 angulos (3 semanas)
2. **Declarar ganador** y documentar
3. **Doblar** el angulo ganador durante 2-3 semanas
4. **Iniciar nuevo test** con un tema o angulo diferente

Despues de 2-3 ciclos (6-9 semanas), Hans tendra datos REALES de que messaging funciona con SU audiencia especifica. Esto elimina la creacion de contenido por intuicion.

## Output (formato exacto)

```markdown
# Message-Fit Test — Ciclo #X
Tema: [tema]
Periodo: [fecha inicio] — [fecha fin]
Estado: En curso / Completado

## Los 3 Angulos

### Angulo A: [nombre]
**Hook sugerido:** "[primera linea del post]"
**Tipo:** [educativo / dolor / POV / story / comparacion / trend]
**Post completo:** [referencia al post creado con post-writer]

### Angulo B: [nombre]
[misma estructura]

### Angulo C: [nombre]
[misma estructura]

## Calendario de Publicacion
| Semana | Fecha | Angulo | Dia/Hora | Formato |
|--------|-------|--------|----------|---------|
| 1 | YYYY-MM-DD | A | [dia hora] | [formato] |
| 2 | YYYY-MM-DD | B | [dia hora] | [formato] |
| 3 | YYYY-MM-DD | C | [dia hora] | [formato] |

## Resultados (llenar despues de cada publicacion)
[Usar template de documentacion del test]

## Decision Final
**Ganador:** [pendiente / A / B / C / ninguno]
**Accion:** [pendiente / doblar / iterar / descartar / nuevo tema]
**Documentar en:** memory/winning-content.md (si hay ganador claro)
```

Guardar en: `outputs/linkedin/YYYY-MM-DD_angle-test.md`
