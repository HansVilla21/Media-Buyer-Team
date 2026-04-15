# Reporte de Research: Optimización Campaña "Trabajo Remoto" — Meta Ads
Fecha: 2026-03-09
Pedido por: COMANDANTE / Hans Villalobos
Tipo: Ads — Optimización de Campaña Activa

---

## CONTEXTO DE LA CAMPAÑA

- Campaña activa en Costa Rica / LATAM
- Objetivo: `onsite_conversion.messaging_conversation_started_7d` (DM en Instagram)
- Presupuesto: ₡15,600/día
- Resultado actual: 840 conversaciones iniciadas

**Métricas al momento del análisis:**
| Métrica | Valor | Estado |
|---------|-------|--------|
| CPR (Costo por resultado) | ₡496.94 | ALERTA: +30.92% vs semana anterior |
| CPM | ₡1,181 | |
| CTR | 0.353% | MUY BAJO (benchmark: >1.5%) |
| Frecuencia | 2.46 | En zona de advertencia |
| Calidad del anuncio | BELOW AVERAGE | Problema activo |
| Interacción | BELOW AVERAGE | Problema activo |
| Conversión | ABOVE AVERAGE | Punto fuerte |

**Distribución por edad (CTR):**
| Rango | CTR | Nota |
|-------|-----|------|
| 18-24 | 0.59% | Peor segmento |
| 45-54 | 1.56% | Buen segmento |
| 55-64 | 2.44% | Mejor CTR pero fuera del avatar |
| 28-42 | (no especificado) | Avatar que realmente compra |

---

## DIAGNÓSTICO DEL PROBLEMA PRINCIPAL

### ¿Qué está pasando exactamente?

El ad tiene una situación paradójica pero con explicación clara: **calidad BELOW AVERAGE con conversión ABOVE AVERAGE**. Esto significa:

1. **El ad convierte bien a los que llegan** — los que hacen clic y abren el DM son personas con alta intención de compra. El proceso después del clic funciona.

2. **Pero el ad no hace clic suficiente** — el CTR de 0.353% está en un rango de 3 a 5 veces por debajo del benchmark mínimo (1.5%). La mayoría de la audiencia ve el ad y no reacciona.

3. **Meta lo penaliza por relevancia** — Meta evalúa el ad contra competidores que muestran al mismo público. Si el público ve el ad y no interactúa (no hace clic, no da "me gusta", no comenta, no comparte), Meta reduce la calidad del ranking. Esto sube el CPM y el CPR.

4. **El público que hace clic no es el avatar correcto** — los datos de edad muestran que los rangos 45-64 tienen mejor CTR, pero el avatar que cierra (profesional técnico, 28-42 años) probablemente no está respondiendo al hook actual del creative. El mensaje actual probablemente resuena más con perfiles mayores o más genéricos.

5. **Frecuencia 2.46 está al límite** — no es crisis todavía (la crisis empieza en 3.5-4.0), pero combinado con el CTR bajo y el CPR subiendo 30%, indica que la audiencia que ya vio el ad no está respondiendo mejor en el segundo o tercer impacto.

### Conclusión del diagnóstico:

**El problema no es el embudo post-clic (conversión ABOVE AVERAGE confirma que funciona). El problema es el creative y la audiencia a la que está llegando.** El ad actual no habla con el lenguaje ni el ángulo correcto para hacer que el avatar correcto (profesional técnico 28-42) detenga el scroll.

---

## 1. RECOMENDACIONES DE TARGETING Y SEGMENTACIÓN

### Edad: excluir o reducir peso de 18-24

- El CTR de 0.353% en promedio, con 18-24 años en 0.59%, confirma que este segmento está bajando el promedio general.
- **Acción:** Excluir el segmento 18-24 del ad set actual o crear una exclusión de audiencia.
- El benchmark global para campañas de mensajes en Instagram indica que el segmento 25-44 es el más valioso comercialmente (>51% de la base de Facebook/Instagram con mayor capacidad de compra).

### Intereses vs. Broad para llegar al profesional técnico

Los datos de Perplexity (búsqueda 9) muestran resultados muy claros para 2025-2026:

**Para profesionales técnicos (ingenieros, contadores, trabajadores técnicos):**
- Broad targeting con Advantage+ gana en 60-70% de los casos
- Broad targeting entrega 28% menor CPA y 18% mayor ROAS vs. targeting por intereses
- Meta infiere perfil profesional a través de señales de comportamiento (dispositivo, patrones de uso, tipo de apps, conexión a LinkedIn)

**Sin embargo, para el caso específico de Hans (mercado pequeño: Costa Rica):**
- El targeting broad en un mercado de 5 millones de personas puede ser demasiado amplio y entregar mucho público irrelevante
- Recomendación: **Híbrido** — broad base (sin intereses) + exclusión de estudiantes y menores de 25 + carga del customer list de leads/clientes actuales como semilla para que Advantage+ construya lookalike

**Intereses que tienen sentido si se quiere probar targeting manual:**
- "Automatización de procesos" / "Software empresarial" / "Emprendimiento" / "Finanzas personales"
- "n8n" (si existe como interés), "Make", "Zapier", "herramientas de productividad"
- "Trabajar desde casa" / "Ingresos extra" / "Freelance"
- Empleadores: multinacionales, zonas francas (si aplica en Meta para CR)

**Nota crítica:** En un mercado pequeño como Costa Rica, los intereses muy específicos (como "ingeniería industrial") pueden crear audiencias de menos de 50,000 personas, lo que limita la capacidad de aprendizaje del algoritmo. Si el ad set necesita 50 conversiones por semana para salir de la fase de aprendizaje, un público demasiado pequeño puede mantenerlo en aprendizaje indefinidamente.

---

## 2. RECOMENDACIONES DE PLACEMENT

### Reels es el placement dominante en 2025-2026

Los datos son contundentes (búsqueda 7):
- Reels logra **30.81% de reach rate** vs. 13.14% del Feed con fotos
- Reels capturó más del 50% del volumen de ads en Instagram en 2025 (crecimiento 35% interanual)
- Formato vertical 9:16 entrega 7% más CTR y menor costo que otros formatos
- Los usuarios pasan el 50%+ del tiempo en Instagram en Reels

### Recomendación de placement para esta campaña:

1. **Placement manual: solo Instagram Reels + Instagram Stories** (desactivar Facebook, Audience Network, Messenger, Feed de Facebook)
2. Esto concentra el gasto donde está la atención del avatar de 28-42 años
3. El creative actual (si es un video) debe estar optimizado en formato 9:16
4. Si el creative no es 9:16 nativo, el algoritmo lo penaliza en Reels — esto podría explicar parte del "Below Average" en calidad

**Lo que NO hacer:** Dejar Advantage+ Placements encendido si el creative no está nativo en vertical. Meta distribuye presupuesto en placements donde el creative no está optimizado, bajando el quality ranking general.

---

## 3. RECOMENDACIONES DE PRESUPUESTO: CBO vs ABO

### Para este caso específico: mantener ABO (presupuesto por ad set)

Los datos de Perplexity (búsqueda 10) muestran que:
- **CBO** es mejor cuando tienes múltiples ad sets con creativos probados y quieres que el algoritmo optimice automáticamente hacia el ganador
- **ABO** es mejor para pruebas y testing donde necesitas garantizar que cada variación reciba datos suficientes
- La recomendación 2026 es: **CBO primero para escala, ABO para testing de creativos nuevos**

**Dado el estado actual del ad (Below Average, CPR subiendo):**
- Si se va a lanzar un creative nuevo, usar ABO para garantizar que el nuevo ad recibe datos reales antes de que el algoritmo lo abandone
- Si se escala el ad actual (que tiene ABOVE AVERAGE en conversión), CBO puede funcionar para dejar que Meta optimice

### Presupuesto actual (₡15,600/día):

- Si el CPR sigue subiendo, la misma cantidad de presupuesto produce menos conversaciones. En 30 días, +30.92% de CPR significa que el mismo presupuesto da ~23% menos conversaciones.
- No escalar el presupuesto mientras el ad tenga Below Average en calidad — primero arreglar el creative, luego escalar.

---

## 4. ¿DUPLICAR EL AD SET O EDITAR EL ACTUAL?

### Respuesta: Crear un ad set NUEVO con creative nuevo, no editar ni duplicar el actual

**Por qué no editar el actual:**
- Editar el ad set activo (cambiar audiencia, presupuesto significativo o creative) reinicia la fase de aprendizaje automáticamente y borra el historial de optimización acumulado con 840 conversaciones
- Perder ese historial en un ad que tiene ABOVE AVERAGE en conversión sería desperdiciar la única señal positiva que tenemos

**Por qué no duplicar:**
- Duplicar sí resetea la fase de aprendizaje y da una "segunda vida" al algoritmo para explorar nuevas rutas de entrega
- PERO el problema principal no es la entrega del algoritmo — es que el creative no conecta con el avatar correcto
- Duplicar el mismo ad con el mismo creative solo va a reproducir el mismo problema en el nuevo ad set

**Lo que sí hacer:**

1. **Mantener el ad set actual tal como está** — no tocarlo, dejarlo correr mientras baja el CPR naturalmente o se estabiliza. Tiene 840 conversaciones de historial y ABOVE AVERAGE en conversión.

2. **Crear un ad set nuevo, independiente, con un creative completamente nuevo** — nuevo hook, nuevo ángulo, dirigido explícitamente al profesional técnico de 28-42 años. Darle un presupuesto de prueba (₡5,000-7,000/día separado).

3. **Si el nuevo creative supera al actual** en CPR y CTR después de 7-14 días con suficiente volumen: pausar el actual y escalar el nuevo.

Este approach protege el historial del ad que funciona en conversión mientras se prueba el nuevo ángulo sin contaminar el ad set original.

---

## 5. EL PROBLEMA REAL DEL CREATIVE Y LOS DATOS DE EDAD

### El desajuste más importante de toda la campaña

Los datos de edad revelan algo crítico: **el creative actual está siendo más efectivo para capturar la atención de personas de 45-64 años que del avatar objetivo de 28-42 años**.

Esto no es un problema de targeting — es un problema de mensaje.

El hook y el ángulo del ad actual probablemente usa un lenguaje o referencias que resuenan más con personas mayores (quizás más conservadoras en el trabajo, más temerosas del desempleo, menos digitales). El avatar de 28-42 años profesional técnico tiene un dolor diferente: no teme quedarse atrás, ya sabe que la automatización existe — quiere el método correcto y la validación de que Hans es quien se lo puede enseñar.

**Implicación para el creative nuevo:**
- No usar el ángulo de miedo a quedar obsoleto (resuena en 45+)
- Usar el ángulo de aceleración: "ya sabes que esto existe, aquí está el método para cobrarlo"
- Mencionar explícitamente el perfil: ingenieros, contadores, personas que ya trabajan con procesos
- Mostrar casos de uso concretos de n8n con contexto empresarial (PDFs, WhatsApp, CRM)

---

## 6. SOBRE EL CTR 0.353%

El benchmark de la industria para campañas de mensajes en Instagram es 1.5% o superior para considerarse saludable. Un CTR de 0.353% está en un rango donde:

- El hook del video no está deteniendo el scroll en los primeros 1-3 segundos
- O el creative no se ve como contenido nativo de Instagram/Reels (parece claramente un ad)
- O el copy superpuesto no tiene suficiente tensión o curiosidad para hacer clic

**Para campañas de mensajes/DMs específicamente:** el CTR mide cuántos hacen clic para abrir el DM. La gente en Instagram es más reacia a abrir un DM con una marca desconocida que a hacer clic en un link. Esto hace que el hook tenga que ser aún más específico y prometerle algo concreto al usuario si abre el DM.

---

## HALLAZGOS PRINCIPALES (Resumen de las 12 búsquedas)

1. **Below Average en calidad + Above Average en conversión = problema de creative, no de embudo.** El ad convierte a los que llegan, pero no convence a suficientes personas para hacer clic. (Búsquedas 1 y Extra 1)

2. **Frecuencia 2.46 está en zona segura pero vigilar.** La fatiga de creative no empieza hasta 3.5-4.0. El problema actual es de relevancia, no de saturación. (Búsqueda 2)

3. **CPR subiendo 30% es una señal de alarma estructural en todo el mercado Meta, no solo en esta campaña.** El CPL en paid social subió 21% interanual en 2025 globalmente. En LATAM el CPM de Brazil es $2.63 — Costa Rica puede estar en un rango similar o más bajo, lo que hace que el CPR de ₡496 sea manejable si el ROAS lo justifica. (Búsqueda 3)

4. **Reels es el placement dominante.** 30.81% de reach rate, 50%+ del tiempo de los usuarios, 7% más CTR con formato 9:16. Si el ad no está en 9:16 nativo, esto explica parte del problema. (Búsqueda 7)

5. **Broad targeting gana sobre intereses específicos para profesionales técnicos**, pero en mercados pequeños como Costa Rica se recomienda combinar broad con exclusiones y customer list. (Búsqueda 9)

6. **Duplicar ad set ayuda cuando el problema es de entrega, no de creative.** En este caso, el problema es el mensaje — duplicar el mismo creative no resuelve nada. (Búsqueda 8)

7. **CBO primero para escala, ABO para testing de creativos nuevos.** Mantener el ad actual en ABO y crear el nuevo creative también en ABO separado para testing. (Búsqueda 10)

8. **Para campañas de DMs/mensajes en 2026:** consolidar audiencias amplias + 10-20 variaciones de creative + Advantage+ para que el algoritmo encuentre los mejores performers. La calidad post-clic (la experiencia del DM) debe ser parte de la optimización. (Búsqueda 6)

---

## DATOS Y ESTADÍSTICAS ÚTILES

- CTR saludable para Meta Ads Instagram: >1.5% (benchmark general); el 0.353% está 4x por debajo
- Frecuencia donde empieza fatiga seria: 3.5-4.0 (el ad actual está en 2.46 — margen disponible)
- Rotar creative recomendado: cada 14-21 días para cold prospecting; cada 7-14 para retargeting
- Mejora de quality ranking de Below Average a Above Average reduce costos 20-40% sin cambiar el bid
- Broad targeting vs. intereses para profesionales técnicos: broad gana 60-70% de los casos en 2025-2026, entrega 28% menor CPA
- Advantage+ Placements puede distribuir presupuesto ineficientemente si el creative no está optimizado para todos los formatos
- CPM de Instagram en LATAM (referencia): Brazil ~$2.63 (bajo), Mexico en rango medio; Costa Rica probablemente similar
- La fase de aprendizaje de Meta requiere 50 conversiones por semana para optimizarse correctamente

---

## ACCIONES INMEDIATAS (Las 3 más importantes HOY)

### Accion 1: NO tocar el ad set actual

El ad actual tiene historial valioso (840 conversaciones, ABOVE AVERAGE en conversión). No editarlo, no pausarlo, no cambiar su presupuesto. Dejarlo correr mientras se construye el plan alternativo.

Excepción: si el CPR supera el umbral de rentabilidad del negocio (Hans debe definir cuál es ese número en ₡ basado en su LTV de cliente), entonces pausar y redirigir presupuesto al creative nuevo.

### Accion 2: Crear un creative nuevo dirigido al profesional técnico 28-42

El creative nuevo debe tener:
- Hook en los primeros 2-3 segundos que nombre el perfil explícitamente: "Si eres ingeniero, contador o alguien que trabaja con procesos..."
- Ángulo de aceleración (no de miedo): "Ya sabes que la automatización existe en tu empresa. Aquí está cómo cobrar por hacerla."
- Formato 9:16 nativo para Reels
- CTA directo a DM con promesa específica de lo que van a recibir al escribir

Este creative nuevo va en un ad set nuevo, con presupuesto de prueba separado (₡5,000-7,000/día), con placement manual en Instagram Reels + Stories, con exclusión de 18-24 años, y usando ABO.

### Accion 3: Excluir el rango 18-24 del ad set actual (si Meta lo permite sin reiniciar aprendizaje)

Si se puede agregar una exclusión de audiencia por edad sin que Meta considere esto un cambio significativo (que reinicie el aprendizaje), excluir 18-24. Esto debería mejorar el CTR promedio inmediatamente porque ese segmento tiene el CTR más bajo (0.59%) y baja el promedio general.

**Advertencia:** Verificar en el Meta Ads Manager si modificar la audiencia activa reinicia el aprendizaje. Si lo hace, NO hacer esta modificación al ad set actual — aplicarla solo al ad set nuevo.

---

## ÁNGULOS DE ADS SUGERIDOS PARA EL CREATIVE NUEVO

Basado en el research y el perfil del avatar (Profesional Técnico 28-42, ingenieros/contadores/analistas LATAM):

1. **Ángulo "Ya lo ves en tu empresa":** "Los flujos automáticos de WhatsApp, los chatbots que responden solos, los reportes que se generan solos — eso ya está en tu empresa. La pregunta es: ¿tú lo estás construyendo o solo lo estás viendo?" → DM para saber cómo cobrarlo.

2. **Ángulo "Portafolio vendible en 90 días":** "Eres ingeniero / contador / analista. Ya tienes el conocimiento de procesos. Lo que te falta es el stack (n8n + IA) y cómo empaquetarlo como servicio. En 90 días, primer cliente." → DM para ver el método.

3. **Ángulo "Demo en vivo":** Mostrar una automatización real corriendo (un flujo de n8n que procesa PDFs, o un bot de WhatsApp respondiendo). "Esto lo hice en 3 horas. Cobra $1,200 por implementarlo. ¿Tienes procesos así en tu empresa?" → DM para ver cómo empezar.

4. **Ángulo "El costo de no hacerlo":** "En tu empresa ya están evaluando contratar a alguien que sepa n8n y automatización con IA. Ese alguien podría ser tú. Externo, pagando $1,500+ por proyecto." → DM.

---

## ÁNGULOS DE PLACEMENTS Y ESTRUCTURA SUGERIDA

```
ESTRUCTURA RECOMENDADA DE CAMPAÑA (NUEVA):

Campaña: Trabajo Remoto — Profesional Técnico
Objetivo: messaging_conversation_started_7d
Tipo presupuesto: ABO (por ad set)

Ad Set 1: PRUEBA — Creative Nuevo (Profesional Técnico)
- Presupuesto: ₡6,000/día
- Audiencia: CR, 25-44, sin intereses (broad), excluir 18-24
- Exclusiones: Personas que ya iniciaron conversación (si aplica)
- Placement: Instagram Reels + Instagram Stories (manual)
- Ads: 2-3 variaciones del nuevo hook

Ad Set 2: CONTROL — Ad Actual (sin tocar)
- Presupuesto: ₡15,600/día (mantener igual)
- No modificar nada
- Monitorear CPR diariamente

Evaluar después de 7-14 días con al menos 50 conversaciones en Ad Set 1.
Si Ad Set 1 supera en CPR al Ad Set 2: escalar Ad Set 1, pausar Ad Set 2.
```

---

## NOTAS PARA EL AGENTE QUE USE ESTE REPORTE

1. **El mercado es Costa Rica** — pequeño (~5M habitantes, ~2M en Instagram). Los benchmarks globales de CTR y CPM no aplican directamente. El CPR en colones debe compararse contra el LTV del cliente de Hans (precio del programa y tasa de cierre) para saber si es rentable, no contra benchmarks de USD.

2. **La situación Below Average Quality + Above Average Conversion es inusual pero conocida.** Significa que hay un segmento pequeño de alta intención que sí responde, pero la audiencia general no. El creative actual está muy nichado para el avatar incorrecto.

3. **No hay datos específicos de benchmarks de Meta Ads para Costa Rica en las fuentes consultadas.** Los datos usados son globales (EE.UU. y mercados desarrollados) y regionales (LATAM general con referencia a Brazil y México). Ajustar las expectativas de CTR hacia abajo para mercados pequeños con audiencias más homogéneas.

4. **El punto más urgente no es técnico — es creativo.** Ningún ajuste de targeting, placement o presupuesto va a resolver un CTR de 0.353% si el hook del video no para el scroll. La prioridad debe ser el CREADOR: un brief para el nuevo ad con el ángulo específico del profesional técnico 28-42.

5. **Limitar investigación a fuentes de 2025-2026** — el ecosistema de Meta Ads cambió significativamente con el roll-out completo de Advantage+ en mid-2025. Recomendaciones de 2023-2024 pueden estar desactualizadas.

---

## FUENTES

- Meta Business Help Center (referenciado en múltiples resultados de Perplexity)
- Meta Performance Report Q4 2025 (referenciado en Perplexity búsqueda 9)
- Meta Forward 2025 Conference (referenciado en Perplexity búsqueda 9)
- Hootsuite Social Media Trends 2026 Analysis (referenciado en Perplexity búsqueda 2)
- AdEspresso 2026 Report (referenciado en Perplexity búsqueda 9)
- Marketing Dive — HubSpot case study 2025 (referenciado en Perplexity búsqueda 9)
- Búsquedas realizadas: 12 queries en Perplexity sonar-pro el 2026-03-09

---

*Reporte generado por: INVESTIGADOR — Media Buyer Team de Hans Villalobos*
*Guardado en: outputs/research/2026-03-09_optimizacion-trabajo-remoto.md*
