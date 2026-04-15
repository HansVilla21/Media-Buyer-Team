# Análisis AD SET 2 — Datos Reales desde Fecha de Creación
**Fecha de análisis:** 2026-03-18
**Período real de los datos:** 2026-03-13 al 2026-03-17 (5 días activo)
**Nota sobre la API:** Meta muestra date_start "2026-02-16" por la ventana de atribución de 7 días — los datos de gasto y conversiones corresponden únicamente al período desde el 13 de marzo. Confirmado porque al pedir any range desde 2026-03-13 en adelante la API devuelve el mismo total.
**Cuenta:** act_1051600449964359
**Moneda:** CRC (Colones costarricenses)
**Analista:** MEDIA BUYER — Momentum AI Academy

---

## CORRECCIÓN IMPORTANTE AL ANÁLISIS ANTERIOR

El análisis del 2026-03-18 anterior tenía un error en la asignación de nombres a IDs de ads:

| Ad | ID real | Lo que decía antes | Dato correcto |
|----|---------|--------------------|---------------|
| AD 4 — La Curva No Para "EMPRESA" | 120240192925420786 | Mayor gasto, 13 conv. | ₡2,273 gasto, 1 conv. — casi sin distribución |
| AD 5 — Intentaste Solo "METODO" | 120240192972250786 | 0 conversiones | ₡32,952 gasto, 13 conv. — el más distribuido |

Los datos del AD 4 y AD 5 estaban intercambiados en el análisis anterior. Esto afecta las conclusiones sobre qué ángulo funciona.

---

## 1. FECHA REAL DE CREACIÓN DEL AD SET 2

- **Creado:** 2026-03-13 a las 18:46 (hora Costa Rica)
- **Primer día con datos:** 2026-03-13
- **Días activo a la fecha del análisis:** 5 días completos (13, 14, 15, 16, 17 de marzo)
- **Hans indicó "desde esta semana (semana del 16 de marzo)"** — en realidad lleva activo desde el 13. La semana del 16 ya es su segunda mitad de primera semana.

---

## 2. DATOS REALES — NIVEL AD SET (13–17 de marzo, 5 días)

| Métrica | Valor | Contexto |
|---------|-------|---------|
| Gasto total | ₡64,752 CRC | ~₡12,950/día promedio (presupuesto: ₡15,000/día) |
| Impresiones | 25,418 | — |
| Alcance | 13,146 personas únicas | — |
| Frecuencia | 1.93 | Saludable, sin fatiga |
| CTR (todos los clics) | 0.86% | Bajo vs. benchmark >1.5% |
| CPM | ₡2,547 CRC | 2.2x mayor que el CPM del ad ganador histórico (₡1,181) |
| CPC | ₡297 CRC | — |
| Conversaciones iniciadas (7d) | 25 | Métrica de conversión del objetivo |
| Total messaging connections | 31 | Incluyendo reconexiones |
| Primeras respuestas | 23 | Personas que respondieron al DM |
| CPR (costo por conversación iniciada) | ₡2,590 CRC | 5.2x más caro que el mejor histórico de Hans (₡497) |
| Video views | 4,513 | — |

### Gasto por día:
| Día | Gasto | Conversaciones |
|-----|-------|----------------|
| 13 mar | ₡3,944 | 1 (primer día, presupuesto incompleto) |
| 14 mar | ₡13,860 | 6 |
| 15 mar | ₡13,834 | 7 |
| 16 mar | ₡18,658 | 6 |
| 17 mar | ₡14,456 | 5 |
| **Total** | **₡64,752** | **25** |

**Promedio de conversaciones por día (sin contar el día 1 incompleto):** 6 conversaciones/día

---

## 3. DATOS REALES — CADA AD (13–17 de marzo)

### Tabla resumen corregida:

| Ad | Gasto (₡) | Impresiones | CTR | CPM (₡) | Conversaciones | CPR (₡) |
|----|-----------|-------------|-----|---------|----------------|---------|
| AD 1 — El Tiempo Perdido "PROCESOS" | 26,202 | 10,031 | 0.76% | 2,612 | 11 | 2,382 |
| AD 2 — Los Agentes de IA "AGENTE" | 1,158 | 500 | 0.60% | 2,316 | 1 | 1,158 |
| AD 3 — Lo Básico Ya No Alcanza "REAL" | 2,167 | 644 | 0.78% | 3,365 | 0 | N/A |
| AD 4 — La Curva No Para "EMPRESA" | 2,273 | 796 | 0.50% | 2,856 | 1 | 2,273 |
| AD 5 — Intentaste Solo "METODO" | 32,952 | 13,447 | 0.97% | 2,451 | 13 | 2,535 |
| **TOTAL** | **64,752** | **25,418** | **0.86%** | **2,547** | **25** | **2,590** |

### Distribución del presupuesto por el algoritmo:
- AD 5 recibió el 50.9% del gasto total
- AD 1 recibió el 40.5% del gasto total
- AD 2, 3 y 4 combinados: solo el 8.6% del gasto

### Detalles por ad:

#### AD 1 — El Tiempo Perdido "PROCESOS" (segundo lugar)
- Gasto: ₡26,202 | Alcance: 6,325 | Frecuencia: 1.59
- CTR: 0.76% | CPM: ₡2,612 | CPC: ₡345
- Conversaciones iniciadas: 11 | CPR: ₡2,382
- Primeras respuestas: 11 | Respuestas de profundidad 2: 5 | Profundidad 3: 5
- 4 compartidos, 3 guardados, 21 reacciones
- **Diagnóstico:** Segundo ad del algoritmo. CTR bajo pero consistente. Las 5 respuestas de profundidad 3 indican conversaciones que llegaron al tercer mensaje — señal de interés genuino.

#### AD 2 — Los Agentes de IA "AGENTE" (descartado por el algoritmo)
- Gasto: ₡1,158 | Alcance: 401 | Frecuencia: 1.25
- CTR: 0.60% | CPM: ₡2,316 | CPC: ₡386
- Conversaciones iniciadas: 1 | CPR: ₡1,158 (el más barato del lote — pero con 1 sola conversión)
- **Diagnóstico:** El algoritmo lo marginó desde el primer día. Paradójicamente, su CPM es el segundo más bajo y su CPR con los pocos datos que tiene es ₡1,158 — mejor que el promedio. Podría ser interesante pero Meta no le dio oportunidad.

#### AD 3 — Lo Básico Ya No Alcanza "REAL" (peor CPM, 0 conversiones)
- Gasto: ₡2,167 | Alcance: 392 | Frecuencia: 1.64
- CTR: 0.78% | CPM: ₡3,365 | CPC: ₡433
- Conversaciones iniciadas: 0
- **Diagnóstico:** CPM más alto del grupo, 0 conversiones. El algoritmo lo penalizó por señales de baja calidad desde el inicio. Candidato claro a pausa.

#### AD 4 — La Curva No Para "EMPRESA" (prácticamente sin distribución)
- Gasto: ₡2,273 | Alcance: 546 | Frecuencia: 1.46
- CTR: 0.50% | CPM: ₡2,856 | CPC: ₡568
- Conversaciones iniciadas: 1 | CPR: ₡2,273
- Nota: 1 bloqueo registrado (usuario bloqueó el mensaje)
- **Diagnóstico:** El CTR más bajo del grupo (0.50%) y CPM segundo más alto. El algoritmo no le asignó presupuesto porque las primeras impresiones no mostraron señales de engagement. El ángulo "empresa adoptando IA" puede ser correcto pero el hook o la ejecución no arranca.

#### AD 5 — Intentaste Solo "METODO" (el favorito del algoritmo)
- Gasto: ₡32,952 | Alcance: 7,853 | Frecuencia: 1.71
- CTR: 0.97% | CPM: ₡2,451 | CPC: ₡253
- Conversaciones iniciadas: 13 | CPR: ₡2,535
- 9 compartidos, 9 guardados, 53 reacciones, 6 comentarios
- Respuestas profundidad 2: 2 | Profundidad 3: 1
- **Diagnóstico:** El algoritmo lo escogió como favorito absoluto. Tiene el CTR más alto (0.97%), el CPC más bajo (₡253) y los mejores indicadores de engagement orgánico (53 reacciones, 9 compartidos). Sin embargo, el CPR de ₡2,535 sigue siendo 5x más alto que el mejor histórico. Y las conversaciones de profundidad 2 y 3 son bajas en proporción — las conversaciones se inician pero no se profundizan tanto como en el AD 1.

---

## 4. DIAGNÓSTICO HONESTO

### ¿Cuánto tiempo lleva activo realmente?
5 días. El 13 de marzo fue el primer día, y fue un día incompleto (el ad set se creó a las 18:46). Los días reales completos son 4 (14, 15, 16, 17 de marzo).

### ¿Está en fase de aprendizaje?
Sí, definitivamente. Meta requiere 50 conversiones por semana por ad set para salir de la fase de aprendizaje. En 5 días el AD SET 2 tiene 25 conversiones en total. Al ritmo actual de ~6 conversiones/día, la semana 1 cerraría con ~42 conversiones — cerca pero sin alcanzar el umbral. No ha salido de aprendizaje.

### ¿Las métricas de esta semana qué indican?
Tres patrones claros:

**1. El algoritmo ya tomó su decisión interna:** Con solo 5 días y ₡64,752 gastados, Meta concentró el 91.4% del presupuesto en 2 de los 5 ads. Los otros 3 recibieron gasto simbólico. Esto es normal en un ad set con múltiples creativos — el algoritmo hace su propia selección rápida.

**2. El CTR es el problema principal:** Ningún ad supera el 1%. El umbral para considerar un ad saludable en video educativo LATAM es >1.5%. El mejor CTR es 0.97% (AD 5). El gap es real, no es ruido estadístico — está presente en todos los ads del lote.

**3. El CPR está 5x más caro que el historial de Hans:** ₡2,535–₡2,590 CRC vs. ₡497 CRC del ad ganador anterior. Con 5 días de datos y en fase de aprendizaje, parte de esa brecha es normal. Pero la magnitud del gap (5x) sugiere que el problema no es solo la curva de aprendizaje — los hooks de estos ads no están parando el scroll tan bien como el ad ganador anterior.

### ¿Es demasiado pronto para concluir algo?
Para los 3 ads con gasto mínimo (AD 2, 3 y 4): sí, 5 días con casi ningún gasto no es suficiente para un veredicto justo. El algoritmo los descartó antes de darles datos suficientes.

Para los 2 ads con distribución real (AD 1 y AD 5): hay suficiente señal para diagnóstico preliminar. No para una decisión definitiva, pero sí para confirmar la dirección.

Para el CPR general del ad set: el dato de ₡2,590 CRC es real, pero con la campaña aún en fase de aprendizaje es esperable que mejore. El umbral de preocupación real sería si en 2 semanas completas el CPR no baja de ₡1,500 CRC.

### ¿Hay señales claras ya?
Sí, dos:

**Señal positiva:** El AD 5 "Intentaste Solo" con ángulo de método/solución tiene el mejor CTR, mejor CPC, y los mejores indicadores de engagement orgánico. Es el ángulo que el algoritmo está validando con el gasto.

**Señal negativa:** El AD 4 "La Curva No Para" con ángulo de adopción empresarial de IA — que el análisis anterior identificó incorrectamente como el líder — tiene en realidad el CTR más bajo (0.50%), CPM segundo más alto, y casi ninguna distribución. El ángulo "las empresas ya adoptan IA" no está resonando en estas ejecuciones específicas.

---

## 5. RECOMENDACIONES CON LOS DATOS CORRECTOS

### PRIORIDAD 1 — Dejar correr AD 1 y AD 5 sin tocarlos hasta completar 2 semanas
Son los únicos con datos suficientes. El AD 5 tiene el mejor CTR y el algoritmo lo prefirió. El AD 1 tiene profundidad de conversación mejor. Ambos necesitan más tiempo para salir de aprendizaje.

**No escalar presupuesto todavía** — cambiar el presupuesto reinicia la fase de aprendizaje.

### PRIORIDAD 2 — Pausar AD 3 (confirmación de Hans requerida)
- ₡2,167 gastados, 0 conversaciones, CPM más alto del lote (₡3,365)
- El algoritmo lo descartó en las primeras 24 horas
- No tiene datos suficientes para defenderlo y el CPM revela que el algoritmo lo ve como mala calidad

### PRIORIDAD 3 — Evaluar AD 4 antes de pausar
Antes de pausar el AD 4, vale la pena entender por qué el ángulo de adopción empresarial de IA no arrancó. El CTR de 0.50% sugiere que el hook específico no para el scroll, aunque el concepto puede ser válido. La recomendación es pausarlo, pero reformular el hook para un test futuro.

### PRIORIDAD 4 — AD 2 en limbo: hay un dato interesante
Con solo ₡1,158 gastados y 1 conversación, el CPR implícito es ₡1,158 — el más bajo del lote. Esto puede ser ruido estadístico de 1 solo dato, pero vale la pena darle una oportunidad antes de pausar. Sugerencia: si se pausa AD 3 y AD 4, una fracción del presupuesto que liberan podría fluir a AD 2 naturalmente por el algoritmo.

### PRIORIDAD 5 — Crear nueva variante del hook del AD 5
El ángulo "método vs. intentar solo" está recibiendo señal positiva. El siguiente paso es crear un AD 5 variante con un hook de apertura más agresivo — los primeros 3 segundos más directos — para ver si el CTR puede cruzar el 1.5%.

### PRIORIDAD 6 — Evaluar expansión geo en 2 semanas
Con solo Costa Rica y 13,146 personas alcanzadas en 5 días, la audiencia disponible es limitada. No cambiar ahora para no interferir con la fase de aprendizaje, pero planificar la expansión para la segunda quincena de marzo.

---

## 6. TABLA DE ACCIONES CORREGIDA

| Ad | Acción | Timing | Razón |
|----|--------|--------|-------|
| AD 5 — Intentaste Solo "METODO" | MANTENER | Ahora | Favorito del algoritmo, CTR 0.97%, 13 conv. |
| AD 1 — El Tiempo Perdido "PROCESOS" | MANTENER | Ahora | Segundo en conv., buena profundidad de DM |
| AD 2 — Los Agentes de IA "AGENTE" | EVALUAR 5 días más | En 5 días | CPR implícito el más bajo, pero 1 sola conversión |
| AD 4 — La Curva No Para "EMPRESA" | PAUSAR (confirmar con Hans) | Esta semana | CTR más bajo (0.50%), casi sin distribución, 1 conv. |
| AD 3 — Lo Básico Ya No Alcanza "REAL" | PAUSAR (confirmar con Hans) | Esta semana | CPM más alto, 0 conversiones, algoritmo lo descartó |

---

## 7. CORRECCIÓN DE LA MEMORIA DEL AGENTE

El análisis anterior guardó en MEMORY.md que "AD 4 La Curva No Para = mejor CTR, mejor CPC". Esto era incorrecto. Los datos reales muestran:

- **AD 5 "Intentaste Solo"** = mejor CTR (0.97%), mejor CPC (₡253), favorito del algoritmo
- **AD 4 "La Curva No Para"** = peor CTR (0.50%), segundo mayor CPM, sin distribución significativa

El patrón de ángulo a replicar es el de AD 5: solución al problema de aprender solo / método estructurado, no el ángulo de adopción empresarial de IA.

---

## 8. ESTADO VS. HISTORIAL DE HANS

| Métrica | Actual (AD SET 2, 5 días) | Mejor histórico |
|---------|--------------------------|----------------|
| CPM | ₡2,547 CRC | ₡1,181 CRC (ad trabajo remoto) |
| CTR | 0.86–0.97% | No documentado con precisión |
| CPR | ₡2,590 CRC | ₡497 CRC (ad trabajo remoto) |
| Frecuencia | 1.93 | Sin fatiga |
| Días activo | 5 días | El histórico tenía 30+ días |

**Nota crítica:** Comparar 5 días de un ad set en fase de aprendizaje contra 30+ días de un ad ganador maduro no es una comparación justa. El CPR de ₡2,590 no es alarma todavía — es punto de partida. La alarma real sería si en 2 semanas no baja de ₡1,500 CRC.

---

*Análisis corregido por MEDIA BUYER — Momentum AI Academy*
*Fuente: Meta Graph API v19.0, AD SET 2 creado 2026-03-13, datos hasta 2026-03-17*
*Nota: El análisis del 2026-03-18 anterior contenía los datos del AD 4 y AD 5 invertidos — este documento los corrige.*
