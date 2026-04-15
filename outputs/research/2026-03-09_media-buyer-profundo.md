# Reporte de Research: ¿Qué es un Media Buyer Profesional? — Guía Exhaustiva
Fecha: 2026-03-09
Pedido por: Hans Villalobos (directo)
Tipo: Research estructural / Rediseño de sistema de agentes
Búsquedas ejecutadas: 8 queries en Perplexity sonar-pro

---

## RESUMEN EJECUTIVO

Un media buyer profesional en 2025-2026 es el responsable de planificar, ejecutar, optimizar y escalar inversión publicitaria pagada para maximizar el retorno de negocio. Su trabajo real va mucho más allá de "poner anuncios": toma decisiones estratégicas sobre qué mensaje mostrar, a quién, en qué momento, con qué presupuesto y cómo iterar para mejorar los resultados continuamente.

En el contexto de un infoproducto como Momentum AI Academy, el media buyer es el eje entre la oferta, el avatar, el contenido creativo y las plataformas de ads — traduciendo el entendimiento del mercado en campañas que generan leads y ventas de forma predecible y escalable.

---

## 1. DEFINICIÓN Y ROL CENTRAL

### ¿Qué hace un media buyer?

El media buyer es el profesional responsable de:
- Planificar la estrategia de medios pagados (qué canales, qué formatos, qué presupuesto)
- Ejecutar las campañas en plataformas como Meta Ads, TikTok Ads, Google Ads
- Optimizar en tiempo real para maximizar ROAS (retorno sobre inversión publicitaria)
- Reducir el CAC (costo de adquisición de cliente)
- Escalar lo que funciona y cortar lo que no

### Diferencia con otros roles de marketing

| Aspecto | Media Buyer | Performance Marketer | Growth Marketer |
|---------|-------------|---------------------|-----------------|
| Objetivo primario | Eficiencia de compra de medios | Conversiones y ROI directo | Crecimiento sistémico y sostenible |
| Métrica clave | CPM, impresiones, CTR | ROAS, CPA, CAC | CAC, LTV, payback period |
| Horizonte temporal | Corto plazo | Mediano plazo | Largo plazo |
| Herramientas | Plataformas de ads, DSPs | Analytics, CRMs, landing pages | SQL, product tools, A/B frameworks |
| Decisiones | Puja, targeting, placement | Creative, copy, landing page | Canales, experimentos, estrategia |

**Nota crítica para el diseño del sistema:** En equipos pequeños como el de Hans, estos tres roles se fusionan en una sola función. El sistema de agentes debe cubrir el espectro completo: desde la compra táctica de medios hasta las decisiones estratégicas de crecimiento.

---

## 2. RUTINA DIARIA DEL MEDIA BUYER (Workflow Completo)

### Mañana — Revisión y Decisiones (8-10 AM aprox.)

**Tareas:**
- Entrar a Meta Ads Manager y revisar métricas overnight: CTR, CPC, ROAS, tasa de conversión
- Identificar campañas con bajo rendimiento (CPA alto, CTR bajo, frecuencia elevada)
- Ajustar presupuestos diarios según pacing del día anterior
- Escalar campañas con ROAS positivo estable (si ROAS >1.5x y lleva 3+ días, aumentar 20-30%)
- Pausar campañas con pérdidas sostenidas (ROAS <0.8x por 48+ horas)
- Revisar segmentación de audiencias: breakdown demográfico, placements (Reels vs. Stories vs. Feed)

**Decisiones típicas de la mañana:**
- ¿Incremento presupuesto a esta campaña o espero más datos?
- ¿Esta caída de ROAS es temporal (ruido estadístico) o señal de fatiga real?
- ¿Cuánto del presupuesto diario asigno a prospección vs. retargeting?

### Mediodía — Optimización y Ejecución (10 AM - 2 PM)

**Tareas:**
- Lanzar tests A/B de nuevos creativos
- Rotar creativos en campañas con frecuencia alta (>4) para evitar fatiga
- Revisar ad sets específicos: qué audiencias están convirtiendo mejor
- Configurar nuevas variantes de copy y visuales según hallazgos del día
- Coordinar con el equipo creativo: dar feedback sobre qué está funcionando y qué no
- Ajustar pujas: cambiar entre Cost Cap, ROAS Goal o manual según fase de la campaña

**Acciones y lógica de decisión:**

| Situación | Acción | Razón |
|-----------|--------|-------|
| CPA subiendo >20% | Estrechar audiencia o revisar creative | Combatir desperdicio, mejorar relevancia |
| Frecuencia alta (>5) | Duplicar ganadores con targeting amplio | Renovar sin perder fase de aprendizaje |
| Escalando | Aumentar presupuesto 20-50% gradualmente | Evitar reset del algoritmo |
| CTR <0.5% | Cambiar creative o pausar | Señal de anuncio poco relevante |

### Tarde — Análisis y Reporting (2-5 PM)

**Tareas:**
- Análisis profundo de cohortes y atribución: ¿qué canal/creative generó qué conversión?
- Actualizar dashboards en Google Analytics / Looker Studio
- Revisión de benchmarks semanales
- Investigar ad library de competidores para nuevas ideas de creative
- Preparar reporte para el negocio: qué pasó, qué cambió, qué se va a hacer

### Noche — Estrategia y Preparación (5-7 PM)

**Tareas:**
- Construir nuevas campañas para el día siguiente
- Revisar automated rules (pausa automática si CPC supera umbral, escala si ROAS está en objetivo)
- Planificación semanal y mensual: alineación con metas de negocio
- Research de tendencias de creativos en el mercado (qué hooks están funcionando)

**Distribución de tiempo estimada:**
- 40% optimización de campañas activas
- 30% análisis de datos
- 20% configuración de nuevas campañas y tests
- 10% reporting y comunicación

---

## 3. DECISIONES QUE TOMA UN MEDIA BUYER

### Decisiones estratégicas
- Qué plataformas priorizar (Meta, TikTok, YouTube, Google)
- Cuánto presupuesto asignar a cada etapa del funnel (TOFU / MOFU / BOFU)
- Cuándo escalar (y cuánto) vs. cuándo pausar y testear
- Qué ángulo de oferta y posicionamiento usar en los ads
- Cómo distribuir la inversión entre campañas de prospección vs. retargeting

### Decisiones creativas
- Qué hooks y ángulos probar en video
- Qué elementos del avatar infundir en cada creativo (problema, deseo, objeción)
- Qué formato usar según objetivo (Reels para prospección, carruseles para educación, stories para urgencia)
- Cuándo el creative está fatigado y necesita renovarse

### Decisiones analíticas
- Si los datos actuales son estadísticamente significativos para tomar una decisión
- Si una caída en ROAS es temporal o sistemática
- Qué atribuir a qué canal cuando hay múltiples touchpoints
- Qué segmento del avatar convierte mejor (para retroalimentar el targeting)

---

## 4. EL FUNNEL DEL MEDIA BUYER: TOFU / MOFU / BOFU

Para un infoproducto como Momentum AI Academy, el funnel en paid social funciona así:

### TOFU — Top of Funnel (Audiencia Fría)

**Objetivo:** Generar awareness y primeros leads entre personas que no conocen la marca.

**Estrategia en Meta Ads:**
- Videos educativos cortos que muestran un resultado posible: "Cómo gané $1,500 con una automatización de IA en LATAM"
- Hooks que nombran el dolor exacto del avatar: "¿Trabajas 8 horas al día y tu sueldo no crece?"
- Carruseles con tips gratuitos de valor real
- Lead magnets: guías, checklists, mini-capacitaciones gratuitas
- Targeting: broad + Advantage+ (dejar que la IA de Meta encuentre al comprador basándose en el creative)

**KPIs a monitorear en TOFU:**
- CPM (costo por mil impresiones): debe ser eficiente, señal de buena relevancia
- CTR (tasa de clics): >1.5% en video, >2% ideal
- Costo por lead inicial (CPL)
- Porcentaje de video visto (hook rate): >30% a los 3 segundos

### MOFU — Middle of Funnel (Audiencia Tibia)

**Objetivo:** Nutrir y calificar leads que ya mostraron interés.

**Estrategia en Meta Ads:**
- Retargeting a quienes vieron el video TOFU pero no convirtieron
- Webinars o masterclasses gratuitas
- Secuencias de anuncios con testimonios y casos de éxito reales
- Contenido que resuelve objeciones: "No necesitas saber programar para hacer esto"
- Emails automatizados complementarios (omnichannel)

**KPIs a monitorear en MOFU:**
- Costo por registro (CPR) al webinar o lead magnet
- Tasa de apertura de emails
- CTR de retargeting (debe ser más alto que TOFU)

### BOFU — Bottom of Funnel (Audiencia Caliente)

**Objetivo:** Convertir en venta a quien ya está listo para comprar.

**Estrategia en Meta Ads:**
- Anuncios de oferta directa con urgencia real (plazos, bonos, garantía)
- Landing pages optimizadas con CRO (A/B test de headlines, CTAs, social proof)
- Testimonios de alumnos reales con resultados específicos
- Retargeting a visitantes de la página de ventas que no compraron
- Upsell y cross-sell para alumnos actuales

**KPIs a monitorear en BOFU:**
- ROAS (objetivo mínimo >1.5x break-even, objetivo ideal >3-4x)
- CPA (costo por cliente adquirido)
- Tasa de conversión de la landing page
- LTV proyectado del cliente

---

## 5. MÉTRICAS Y BENCHMARKS QUE MONITOREA EL MEDIA BUYER

### Métricas principales (2025-2026)

| Métrica | Definición | Fórmula | Benchmark Referencial |
|---------|-----------|---------|----------------------|
| **CTR** | Tasa de clics sobre impresiones | (Clics / Impresiones) × 100 | 1-2% (estándar), 2-3% (video educativo) |
| **CPM** | Costo por mil impresiones | (Gasto / Impresiones) × 1,000 | $5-15 USD en prospección |
| **CPC** | Costo por clic | Gasto / Clics | $0.50-2.00 USD |
| **ROAS** | Retorno sobre gasto en ads | Ingresos / Gasto en Ads | 3-5x para ser rentable en infoproductos |
| **CPA** | Costo por adquisición | Gasto / Conversiones | 20-30% del LTV del cliente |
| **CPL** | Costo por lead | Gasto / Leads generados | Variable según nicho y precio del curso |
| **Frecuencia** | Veces promedio que alguien vio el ad | Impresiones / Alcance | <3-4 (sobre eso, fatiga de ad) |

### Nuevas métricas de Meta para 2026

- **Views (nueva métrica unificada):** Reemplaza en parte a impresiones. Unifica views de video y otras interacciones reales. Más relevante para Reels y Stories.
- **Creative Fatigue Score:** Señal automática de cuando un creative está gastado por repetición excesiva. Permite renovar antes de que el CPA se dispare.
- **Similitud de Creativos:** Detecta creativos demasiado similares entre sí que compiten internamente (cannibalization).

### Señales de alarma que activan intervención inmediata

- ROAS cae por debajo del break-even por 48+ horas
- CPA supera 1.5x el costo objetivo
- CTR baja de 0.5% (creative agotado)
- Frecuencia supera 5-7 (audiencia quemada)
- CPM sube >20% vs. promedio (competencia intensa en la subasta)

---

## 6. GESTIÓN Y ESCALADO DE PRESUPUESTOS

### Distribución semanal del presupuesto

| Día | % del presupuesto semanal | Razón |
|-----|--------------------------|-------|
| Lunes-Miércoles | 40% | Mayor tráfico post-fin de semana, alta intención |
| Jueves-Viernes | 35% | Pico de compras online |
| Sábado-Domingo | 25% | Menor conversión; enfoque en retargeting |

### Fases de presupuesto

**Fase de Testing:**
- $50-200 USD/día por campaña
- Duración: 3-7 días mínimo, hasta 50 conversiones por ad set
- Objetivo: identificar creativos y audiencias ganadoras
- Usar CBO (Campaign Budget Optimization) para que Meta distribuya

**Fase de Escalado:**
- Aumentar solo 20-30% diario para no resetear la fase de aprendizaje
- Máximo 50% de incremento en 3 días consecutivos
- Regla de escalado: "Si ROAS >1.5x por 3 días consecutivos, escala 25%"
- Automated Rules en Meta: configurar aumento automático cuando se cumplan condiciones

**Cuándo escalar (umbrales):**
- ROAS >1.5x (o tu break-even específico)
- CPA menor que el objetivo
- CTR >1.5-2%
- Frecuencia <3-4
- Más de 50 conversiones/día por ad set (señal fuerte para el algoritmo)

**Cuándo pausar:**
- ROAS <0.8x por 48+ horas
- CPA >1.5x el objetivo por 3 días
- CTR <0.5%
- Frecuencia >5-7
- CPM sube >20% vs. promedio sin mejora en conversiones

### CBO vs. ABO

- **CBO (Campaign Budget Optimization):** Meta distribuye el presupuesto automáticamente entre ad sets. Mejor para escalar. Recomendado en >80% de casos.
- **ABO (Ad Set Budget Optimization):** Control manual por ad set. Mejor para tests aislados donde se quiere controlar exactamente cuánto gasta cada hipótesis.

---

## 7. CREATIVE TESTING: METODOLOGÍA COMPLETA

El creative es el factor número uno en el éxito de un ad en Meta en 2025-2026. El 70% del resultado de una campaña depende del creative.

### Estructura ganadora de un video ad para Meta (2025)

**Hook (0-2 segundos):** La fase más crítica. Determina si el usuario sigue viendo o hace scroll.
- Pregunta que nombra el dolor: "¿Trabajas para un sueldo fijo y no puedes crecer?"
- Beneficio inmediato: "Gané $1,500 en 2 semanas sin programar"
- Demo rápida: mostrar el resultado antes de explicar el proceso
- Regla: el hook debe funcionar incluso sin sonido (subtítulos siempre)

**Cuerpo (3-15 segundos):** Beneficios, no características. Prueba social.
- Mencionar la solución en lenguaje del avatar, no técnico
- UGC (User Generated Content): más auténtico, más efectivo que producción corporativa
- Incluir prueba social: número de alumnos, testimonios, resultados reales

**Cierre (15-30 segundos):** CTA claro y específico.
- Un solo llamado a la acción
- Reducir fricción: "Escríbeme por DM" o "Haz clic para ver cómo"
- Crear urgencia si es real (no falsa escasez)

**Formato ganador 2025:**
- Reel vertical corto (15-30 segundos para prospección)
- Auténtico y filmado con celular (supera a producción profesional fría)
- Subtítulos siempre (70%+ de usuarios ve sin sonido)
- Rotar creative cada vez que la frecuencia supera 3-4

### Metodología de testing a alta velocidad

**Semana 1 — Preparación:**
- Definir 1 hipótesis clara: "¿Un hook UGC convierte mejor que un hook con datos?"
- Preparar 2-4 assets por variante (videos, copies)
- Elegir 1 KPI único como árbitro (CPA o Conversiones)

**Semanas 2-6 — Test A/B:**
- Split 50/50 dentro de la misma campaña (no en campañas separadas — reduce ruido)
- No cambiar nada más durante el test: aislar la variable
- Dejar correr mínimo 4-6 semanas para datos estadísticamente significativos

**Semana 6+ — Análisis y escala:**
- Elegir ganador por el KPI definido
- Documentar: qué ángulo funcionó y por qué (hipótesis sobre el avatar)
- Iterar: nueva hipótesis basada en el aprendizaje anterior

**Velocidad de iteración recomendada:**
- Lanzar mínimo 4-8 creativos nuevos por mes
- Cuando hay escala, aumentar a 10-20 creativos/mes
- Nunca depender de un solo creativo ganador: el ad fatigue siempre llega

---

## 8. CÓMO EL MEDIA BUYER USA EL AVATAR Y LA OFERTA

### El avatar no es para el targeting manual — es para el creative

Este es el cambio más importante en Meta Ads 2025-2026 post-Andrómeda (actualización del algoritmo):

El targeting manual (por intereses, comportamientos, lookalikes) ya no es la forma principal de llegar al avatar. Meta usa sus modelos de IA (Vision-Language Models) para "leer" el creative y encontrar al público correcto automáticamente.

**Consecuencia práctica:**
- El media buyer infunde el buyer persona DENTRO del creative
- El anuncio "habla" específicamente a un sub-avatar: sus dolores, su lenguaje, sus deseos
- Meta lee esas señales semánticas y visuales y expande el reach a personas similares
- El creative se convierte en el targeting real

### Cómo se infunde el avatar en el creative

**En los visuales:**
- Personas que se parezcan al avatar (edad, contexto, situación)
- Escenarios que reconozca: home office, celular, trabajando solo
- Paleta emocional alineada: no lujo aspiracional vacío, sino resultado alcanzable

**En el copy:**
- Usar el lenguaje exacto del avatar: "sin programar", "desde casa", "en LATAM"
- Mencionar el dolor específico: "sueldo que no crece", "no tengo tiempo"
- Mostrar el resultado antes del proceso (fórmula: resultado → proceso → prueba → CTA)

**En la estructura del mensaje:**
- Hablar de UN sub-avatar a la vez: un ad para "el empleado corporativo atrapado", otro para "el emprendedor digital estancado"
- No tratar de capturar a todos con un solo mensaje genérico

### Cómo usa la oferta

- Cada etapa del funnel enfatiza un aspecto diferente de la oferta
- TOFU: el resultado prometido y la oportunidad de mercado
- MOFU: el mecanismo único y la prueba de que funciona
- BOFU: la garantía, los bonos, la urgencia de actuar ahora
- La oferta de $2,000-$5,000 USD extra al mes se menciona en BOFU, no en TOFU (muy directo para audiencia fría)

---

## 9. ANÁLISIS DE COMPETIDORES (Ad Intelligence)

### Herramientas principales

**Facebook Ad Library (gratuita — siempre el punto de partida):**
- Acceso: facebook.com/ads/library
- Buscar por nombre de página del competidor
- Filtrar por: tipo de medio (video/imagen/carrusel), estado (activo/inactivo), fecha
- Ordenar por impresiones (de mayor a menor) para encontrar los ads con más inversión
- Analizar: hook de apertura, copy, CTA, landing page destino

**Qué analizar de cada ad de competidor:**
- Hook (primeros 2 segundos): ¿qué problema o deseo nombra?
- Estructura del mensaje: ¿cómo van de problema a solución?
- CTA: ¿a dónde mandan? ¿webinar, DM, landing directa?
- Cuánto tiempo lleva activo: si lleva semanas o meses, es probablemente rentable
- Qué elementos de social proof usan

**Herramientas de pago para análisis avanzado:**
- **GetHookd ($19+/mes):** Detecta ads que se están escalando activamente, transcribe videos de competidores, genera variantes de scripts basadas en los hooks detectados. Biblioteca de 65M+ ads.
- **BigSpy (tier gratuito):** Tendencias de creativos en múltiples plataformas.

### Proceso de análisis de competidores (frecuencia: semanal)

1. Ir a Facebook Ad Library
2. Buscar 3-5 competidores directos en el nicho de educación IA/automatización
3. Identificar sus ads más antiguos activos (los más viejos = los más rentables)
4. Documentar: tipo de hook, ángulo de oferta, formato de video, CTA
5. Identificar patrones: ¿qué ángulo usan la mayoría? ¿dónde hay un gap?
6. Usar los insights para informar la siguiente tanda de creativos propios (inspiración, no copia)

---

## 10. CÓMO TRABAJA EL MEDIA BUYER CON EL EQUIPO CREATIVO

### El brief de creatividades

El media buyer provee al equipo creativo (o al creador de contenido) un brief estructurado con:
- El ángulo específico del ad (qué problema o deseo aborda)
- El sub-avatar al que va dirigido
- El hook de apertura (exactamente qué decir en los primeros 2 segundos)
- El formato (Reel, carrusel, imagen estática)
- Los puntos clave del mensaje (beneficios, no características)
- El CTA específico
- Referencias o ejemplos de ads de inspiración
- KPI objetivo (para qué etapa del funnel es)

### Ciclo de feedback e iteración

1. Media buyer analiza rendimiento de creativos actuales
2. Identifica: ¿qué hooks tienen mejor CTR? ¿Qué angles tienen mejor CPA?
3. Briefea al creador con hipótesis específica: "necesito probar un hook con resultado numérico en los primeros 2 segundos"
4. Creador produce el contenido
5. Media buyer lanza en test A/B
6. En 2-4 semanas, analiza resultados
7. Documenta aprendizaje y briefea la siguiente iteración

### Velocidad de producción creativa recomendada

- **Fase inicial (testing):** 4-8 creativos nuevos/mes
- **Fase de escala:** 10-20 creativos/mes
- **Señal de alerta:** Si un mismo creative lleva más de 4-6 semanas sin ser reemplazado y la frecuencia sube, el media buyer debe activar producción de nuevos

---

## 11. STACK TECNOLÓGICO DEL MEDIA BUYER

### Plataformas de ads (obligatorio)
- **Meta Ads Manager:** Central de operaciones para Facebook e Instagram Ads
- **Meta Business Suite:** Gestión integrada de cuenta y páginas
- **Meta Pixel + Conversion API:** Tracking de conversiones (CAPI es clave post-iOS14)
- **Meta Experiments:** Para A/B tests controlados dentro de Meta

### Analytics y atribución
- **Google Analytics 4:** Tracking de comportamiento en landing pages y sitio web
- **Looker Studio (antes Data Studio):** Dashboards visuales, reportes exportables, gratuito
- **Triple Whale / Northbeam:** Atribución avanzada para e-commerce/infoproductos con múltiples touchpoints (más relevante cuando la inversión mensual supera los $5,000-10,000 USD)
- **Improvado:** Analytics AI que permite consultas en lenguaje natural sobre datos de campañas; reduce tiempo de reporting ~30%

### Automatización e IA
- **Meta Automated Rules:** Escalar o pausar campañas automáticamente cuando se cumplen condiciones
- **Advantage+ (Meta):** Optimización automática de placements, creativos y audiencias
- **CBO (Campaign Budget Optimization):** Meta distribuye presupuesto entre ad sets automáticamente
- **Copy.ai / Jasper:** Generación de variantes de copy a escala para tests

### Análisis de competidores
- **Facebook Ad Library:** Gratuito, punto de partida obligatorio
- **GetHookd ($19+/mes):** Detección de ads escalando, transcripción de videos de competidores
- **BigSpy:** Tendencias de creativos (tier gratuito disponible)

### CRM y seguimiento de leads
- **Airtable / Google Sheets:** Tracking de leads, pipeline de ventas
- **ManyChat:** Automatización de DMs en Instagram para captura de leads
- **Email marketing:** Integrado con el funnel de MOFU (ActiveCampaign, Klaviyo, Mailchimp)

### Herramientas de contenido y producción
- **CapCut:** Edición de video (en el caso de Hans)
- **Canva:** Diseño de estáticos para ads
- **Gemini Imagen / DALL-E:** Referencias visuales y variantes de creativos con IA

---

## 12. EL MEDIA BUYER PARA INFOPRODUCTOS: ESPECIFICIDADES

### Por qué los infoproductos son un caso especial

- Márgenes muy altos (no hay costo de inventario, envío o producción física)
- Ciclos de compra cortos en algunos casos (decisiones emocionales bajo urgencia)
- La prueba social y los resultados de alumnos son el activo más valioso
- La confianza y autoridad del creador son parte del producto
- El funnel es más largo que en e-commerce: la educación requiere nurturing

### Ajustes específicos para academias digitales

**En TOFU:**
- El contenido orgánico (reels, stories) alimenta el paid: los mejores orgánicos se convierten en ads
- El hook debe resolver la ecuación: "¿vale la pena mi atención?" en 2 segundos
- Ángulos más efectivos: resultado numérico + identidad del avatar ("esto es para ti si...")

**En MOFU:**
- El webinar o masterclass gratuita es el mecanismo de nurturing más efectivo para ticket medio-alto
- El retargeting debe mostrar prueba social diferente: si en TOFU mostraste resultados, en MOFU muestra el proceso

**En BOFU:**
- La garantía es fundamental para reducir el riesgo percibido (la garantía de 90 días de Momentum AI Academy es un activo de BOFU)
- Los testimonios de alumnos con resultados específicos y cuantificables convierten mejor que testimonios emocionales
- La urgencia debe ser real (cohortes, fechas de inicio, número de lugares)

### Evolución del rol hacia 2026

- Meta automatiza cada vez más la ejecución táctica (pujas, distribución, audiencias)
- El media buyer migra hacia la supervisión estratégica: definir inputs (quién es el avatar, qué dice la oferta, qué quiere el negocio) y supervisar los outputs de la IA
- Las decisiones humanas que quedan: qué ángulo creativo probar, cómo interpretar los datos, cuándo intervenir en una campaña, cómo ajustar la oferta
- Para 2026, Meta promete generar campañas completas (imágenes, copy, distribución) a partir de una URL y un presupuesto — elevando el ROAS promedio un 22% vs. gestión manual en sus primeras pruebas

---

## 13. IMPLICACIONES PARA EL SISTEMA DE AGENTES DE HANS

### Lo que el sistema de agentes debe replicar (mapeado por función)

**Funciones de análisis diario (MEDIA BUYER agent):**
- Leer métricas de Meta Ads (via API) y generar resumen con señales de alerta
- Identificar campañas que deben escalarse, pausarse o necesitan nuevo creative
- Comparar rendimiento actual vs. benchmarks y vs. período anterior

**Funciones de creative strategy (CREADOR + MEDIA BUYER en coordinación):**
- Generar briefs de creatividades con hipótesis específicas de testing
- Producir hooks y estructuras de video basadas en el avatar
- Documentar qué ángulos y hooks han funcionado mejor (memoria de winning creatives)

**Funciones de research (INVESTIGADOR):**
- Monitorear ad library de competidores semanalmente
- Detectar tendencias de hooks y formatos en el nicho
- Traer datos externos que inspiren nuevos ángulos de creative

**Funciones de estrategia (ESTRATEGA):**
- Revisar mensualmente: ¿está el funnel completo cubierto (TOFU/MOFU/BOFU)?
- ¿El avatar sigue siendo válido o hay señales de que cambió?
- ¿La oferta está bien posicionada para las campañas actuales?
- ¿Hay oportunidades de escalado en nuevos canales o formatos?

**Funciones de orquestación (COMANDANTE):**
- Recibir las métricas del MEDIA BUYER y decidir qué agente activa
- Si ROAS cayó → activa INVESTIGADOR para analizar qué cambió + CREADOR para nuevos hooks
- Si hay nuevo budget → activa ESTRATEGA para plan de escalado
- Si hay nuevo lanzamiento → coordina CREADOR + MEDIA BUYER para funnel completo

### Gaps identificados en el sistema actual

1. **No hay tracking de ad performance en tiempo real:** El sistema actual no tiene integración con la API de Meta Ads para leer métricas automáticamente. Este es el mayor gap técnico.
2. **No hay memoria de winning creatives estructurada:** El archivo `winning-content.md` existe pero necesita un formato específico para ads (hook, ángulo, resultado, aprendizaje).
3. **No hay proceso de brief a creative definido:** El MEDIA BUYER necesita un template de brief de creatividades que pase al CREADOR.
4. **No hay ciclo de análisis de competidores regular:** Necesita establecerse como proceso semanal automatizable.
5. **No hay definición de funnel actual de Hans:** ¿Qué está corriendo en TOFU? ¿Qué en MOFU? ¿Qué en BOFU? Esa estructura base necesita documentarse.

---

## Datos y Estadísticas Útiles

- Incremento de CPL (costo por lead) interanual en paid social: +21% YoY (2024-2025) — la escasez de atención y la saturación de plataformas encarece la adquisición
- Creative es responsable del ~70% del resultado de una campaña en Meta (vs. 30% targeting/bid)
- Advantage+ con IA: eleva ROAS promedio 22% vs. gestión manual (dato de Meta para campaña automatizada completa)
- Frecuencia de rotación de creative recomendada: cada 3-4 semanas en campañas activas
- A/B test duración mínima: 4-6 semanas para datos estadísticamente significativos
- Benchmarks de CTR para video educativo en Meta: 2-3% (bueno), <1% (señal de problema)
- Benchmarks ROAS para infoproductos/educación digital: 3-5x para ser rentable, >4x objetivo ideal
- Fase de aprendizaje Meta: requiere mínimo 50 conversiones por ad set para estabilizarse

---

## Fuentes

- Perplexity sonar-pro, 8 búsquedas ejecutadas el 2026-03-09
- Meta Blueprint 2025 (meta.com/business/help) — referenciado en resultados de Perplexity
- Agencia LA Libélula + Abeja Comunicación — datos de metodología de testing en español
- WordStream / Hawke Media — benchmarks ROAS 2025 (3-5x promedio en retail/infoproductos)
- GetHookd (gethookd.com) — datos de herramientas de ad intelligence y CPL +21% YoY
- Improvado — dato de reducción de tiempo en reporting ~30% con AI analytics

---

## Notas para el Agente que Usará Este Reporte

1. **Este reporte es la base para rediseñar el sistema de agentes.** El COMANDANTE debe leerlo completo para entender qué hace realmente un media buyer y cómo dividir responsabilidades entre agentes.

2. **El gap más crítico identificado es la falta de lectura de métricas de Meta Ads.** Sin datos reales de campañas, el MEDIA BUYER agent solo puede generar estrategia y creative briefs — no puede optimizar activamente. Cuando Hans integre la API de Meta, este sistema se vuelve 10x más valioso.

3. **La tendencia 2026 de IA en Meta cambia el rol del media buyer:** ya no es la persona que configura audiencias manualmente — es quien decide qué decirle al avatar y supervisa que la IA de Meta haga el trabajo táctico. Esto es exactamente lo que un sistema de agentes puede hacer bien.

4. **Para el contexto específico de Hans (@hansvilla.ai):**
   - El avatar (Andrés/Carolina, 28-35, LATAM) debe vivir en el creative, no en el targeting manual
   - La garantía de 90 días es su mejor activo de BOFU — debe estar en todos los ads de cierre
   - Sus reels orgánicos son el mejor material de prospección para ads — los que más views tienen deberían probarse como ads
   - El contenido UGC (Hans hablando directamente a cámara) supera a producción fría en este nicho

5. **Benchmarks con cautela:** Los benchmarks de CTR, ROAS y CPA varían significativamente por nicho, precio del producto, madurez del mercado y momento de la campaña. Los valores en este reporte son referencias de mercado general — Hans debe establecer sus propios benchmarks basados en historial real de sus campañas.
