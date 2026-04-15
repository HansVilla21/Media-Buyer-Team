# Aprendizajes Acumulados del Sistema

_Este archivo lo escriben los agentes. Registra patrones, preferencias de Hans y lecciones del sistema._
_Fecha de creación: 2026-03-09_

---

## Preferencias Confirmadas de Hans

### Formato y estilo de outputs
- Idioma: español siempre, sin excepción
- Formato: el agente decide según el contexto (no hay formato fijo impuesto)
- Autonomía: ejecutar directamente en creación de contenido; sugerir y esperar en cambios de estrategia

### Herramientas confirmadas
- Edición de video: CapCut
- Automatizaciones: n8n (principal), Make (secundario)
- Research: Perplexity API
- CRM: Airtable / Google Sheets
- Comunicación: Slack, Discord (para notificaciones)

### Contenido
- Canal principal: Instagram (Reels + Stories)
- Frecuencia objetivo: 7 posts/semana
- Prioridad inmediata: guiones de reels + investigación para contenido actualizado
- Plataforma de edición: CapCut

### Ads
- Ha usado Meta Ads
- Tiene un ad ganador actual (video) que genera leads
- Prioridad: crear más ads ganadores, no solo analizar el existente

---

## Aprendizajes del Sistema

---
2026-03-09 — COMANDANTE + INVESTIGADOR + CREADOR
**Aprendizaje:** Para reels de noticias de IA, el ángulo que más conecta con el avatar de Hans NO es técnico (benchmarks, parámetros) sino de impacto laboral y oportunidad económica: "esto ya está pasando en empresas grandes, ¿estás del lado correcto?"
**Contexto:** Primer reel de noticias sobre Claude Anthropic. Se investigaron 9 hallazgos y se eligieron los 3 más accionables y comprensibles para no-técnicos.
**Acción futura:** En reels de noticias de IA, siempre filtrar los hallazgos por el criterio: "¿un profesional LATAM de 28-35 años sin background técnico puede entender esto en 10 segundos?" Si no, es ruido para la audiencia de Hans.
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** La noticia del Pentágono bloqueando Anthropic (marzo 2026) existe pero es ruido para la audiencia de Hans — es controversia de defensa militar, no de productividad o monetización. Filtrarla activamente en futuros reels de novedades de IA.
**Contexto:** Apareció en búsqueda de Claude + negocios LATAM 2026.
**Acción futura:** En research de noticias de IA, agregar filtro activo: "¿es relevante para alguien que quiere ganar dinero con IA en LATAM?" Si no, no incluir en el reporte para el CREADOR.
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** Perplexity sonar-pro no devuelve casos LATAM específicos de uso de Claude en negocios pequeños — no existen documentados en medios hispanohablantes a marzo 2026. Esto es una oportunidad de posicionamiento para Hans: ser de los primeros en mostrar casos de uso concretos en LATAM con Claude.
**Contexto:** Búsqueda explícita de "Claude casos de uso negocios LATAM 2026 n8n Make WhatsApp" — Perplexity confirmó ausencia de datos específicos.
**Acción futura:** No inventar casos LATAM sin fuente. En cambio, usar el ángulo: "nadie en LATAM lo está mostrando todavía — aquí te enseño yo."
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** Datos verificados de Claude a marzo 2026 que sirven como munición de contenido para Hans: (1) Claude superó a ChatGPT en descargas el 1 de marzo 2026, (2) Claude Pro cuesta $17-20/mes vs $200/mes de ChatGPT, (3) 18.9M usuarios activos mensuales en web, (4) crecimiento 60% usuarios gratuitos desde enero 2026, (5) integración con Microsoft 365 anunciada el 9 de marzo 2026, (6) Claude Marketplace lanzado el 6 de marzo 2026 sin comisiones. Todos estos datos tienen fuentes verificables en español.
**Contexto:** Research de 3 búsquedas Perplexity sonar-pro para reporte de novedades Claude para principiantes.
**Acción futura:** Usar estos datos como referencia base para reels de noticias de IA hasta que haya datos más recientes. No presentarlos como "de hoy" si han pasado más de 30 días.
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje (técnico):** La API de Perplexity falla con curl en bash de Windows cuando el JSON contiene comillas anidadas. La solución que funciona es llamar a Perplexity desde Node.js usando el módulo `https` nativo con JSON.stringify() para construir el payload. Node v22 está disponible en el entorno de Hans.
**Contexto:** Primer intento con curl dio error "There was an error parsing the body". Node.js resolvió el problema en el primer intento.
**Acción futura:** Siempre usar Node.js para llamadas a Perplexity en este entorno Windows. Bash + curl falla con JSON complejo.
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** Research exhaustivo sobre el rol de media buyer profesional completado (8 búsquedas Perplexity sonar-pro). Ver `outputs/research/2026-03-09_media-buyer-profundo.md` para el reporte completo. Hallazgos clave para el sistema:
1. El creative es el 70% del resultado en Meta Ads — el targeting manual perdió relevancia con Advantage+ y broad targeting. El avatar ahora se "infunde" en el creative, no en la configuración de audiencias.
2. El funnel TOFU/MOFU/BOFU tiene mecánicas distintas: TOFU=awareness con hooks de dolor, MOFU=retargeting con prueba social, BOFU=urgencia + garantía.
3. El media buyer moderno en 2026 supervisa IA — no ejecuta targeting manual. Sus decisiones son: qué ángulo creativo probar, qué escalar, cuándo pausar, cómo interpretar datos.
4. Gaps críticos identificados en el sistema de Hans: sin lectura de métricas de Meta vía API, sin template de brief de creatividades, sin proceso de análisis de competidores semanal, sin mapa del funnel actual documentado.
5. Benchmarks clave: ROAS objetivo >3-5x para infoproductos, CTR >2% en video educativo, frecuencia máxima 3-4 antes de rotar creative, test A/B mínimo 4-6 semanas.
**Contexto:** Research para rediseño del sistema de agentes. 8 búsquedas Perplexity. Pendiente validación de benchmarks por Hans con datos reales de sus campañas.
**Acción futura:** Cuando Hans comparta datos reales de Meta Ads, contrastar con estos benchmarks y actualizar con los números reales de su cuenta.
---

---

## Skills Creadas por el Sistema

| Skill | Fecha | Creada por | Motivo |
|-------|-------|------------|--------|
| creador-de-skills | 2026-03-09 | Setup inicial | Base del sistema de skills, adaptada de proyecto Antigravity |
| research-rol-profesional | 2026-03-09 | INVESTIGADOR | Metodología para investigar roles profesionales en profundidad con Perplexity (para diseño de agentes) |

---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** Campaña "Trabajo Remoto" analizada en profundidad. La situación Below Average calidad + Above Average conversión indica que el creative actual convierte bien a los que hacen clic, pero el CTR 0.353% (benchmark saludable: >1.5%) revela que el hook no detiene el scroll del avatar correcto (profesional técnico 28-42). El problema no es técnico (targeting, presupuesto) sino creativo (mensaje equivocado para el avatar equivocado). El rango 55-64 tiene el mejor CTR (2.44%) mientras que el 28-42 no está respondiendo — el creative resuena con perfiles más mayores.
**Contexto:** 12 búsquedas Perplexity sonar-pro para optimización de campaña activa Meta Ads. Reporte completo en `outputs/research/2026-03-09_optimizacion-trabajo-remoto.md`.
**Acción futura:** Para nuevos ads de Hans, el hook en los primeros 2-3 segundos DEBE nombrar explícitamente el perfil (ingeniero, contador, analista) y usar ángulo de aceleración, no de miedo. No usar "quédate atrás con la IA" — eso resuena en 45+ años, no en 28-42.
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** Benchmarks de Meta Ads 2025-2026 confirmados para el contexto de Hans:
- CTR saludable Meta Ads Instagram: >1.5% (menos de 1% es señal de problema)
- Frecuencia donde empieza fatiga real: 3.5-4.0 (no a 2.46 como está el ad actual)
- Below Average quality → Above Average conversion = problema de creative no de embudo (el ad convierte a los que llegan, pero no hace clic suficiente)
- Mejora de quality ranking de Below Average a Average+ reduce costos 20-40% sin cambiar el bid
- Reels: 30.81% de reach rate vs. 13.14% del Feed; captura >50% del tiempo de usuarios en Instagram en 2025
- Broad targeting gana sobre intereses para profesionales técnicos en 60-70% de los casos; 28% menor CPA, 18% mayor ROAS
- CBO para escala; ABO para pruebas de creative nuevo
- La fase de aprendizaje de Meta necesita 50 conversiones/semana para optimizarse
**Contexto:** Research de 12 búsquedas sonar-pro el 2026-03-09. Pendiente validación con datos reales de Hans de su cuenta.
**Acción futura:** Usar estos benchmarks como referencia para análisis de campañas futuras. Cuando Hans comparta datos de sus campañas, comparar contra estos números.
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** Research de 12 búsquedas Perplexity sonar-pro sobre ángulos para ad scripts de IA. Reporte completo en `outputs/research/2026-03-09_research-angulos-ads-ia.md`. Hallazgos clave:
1. "Automatizaciones con IA" es la combinación ganadora para el cuerpo del ad. "IA" sola para el hook de atención (mayor volumen de interés). "Automatizaciones" sola es demasiado técnica para audiencia fría.
2. "Agentes de IA" es el término con mayor potencial no explotado en LATAM para el nicho de Hans. Está creciendo viralmente, ningún competidor lo posiciona en español con enfoque de monetización y n8n.
3. El ángulo de "negocio de automatización" (retainers, clientes recurrentes) convierte mejor que "freelance" o "ingresos extra" para infoproductos en LATAM en 2026.
4. n8n es claramente el líder entre profesionales técnicos avanzados sobre Make y Zapier — nombrarlo explícitamente en ads es un filtro de calificación del avatar correcto.
5. Competidores identificados: Rodrigo Camacho (HighLevel + YouTube, USA-centric), IDIA.es (España, agentes IA n8n), HostGator Español (tutorial gratuito n8n, sin monetización). Ninguno ataca al Sub-avatar 1 (profesional técnico LATAM) con un proceso de ventas incluido.
6. El término "GTM Engineer" tiene tracción en LinkedIn (3,000+ vacantes, salarios $2,000-5,000/mes LATAM). Es una oportunidad de posicionamiento para el Sub-avatar 1 que está en LinkedIn.
7. El financiamiento a 12 meses (~$100/mes) debe ser argumento central en el Ad 5 (Sub-avatar 2), no pie de página.
**Acción futura:** El CREADOR debe escribir 5 guiones de ad correspondientes a los 5 ángulos identificados: (1) El Acelerador, (2) Los Agentes de IA, (3) El Anti-Ruido, (4) El Tiempo Real, (5) El Número del Financiamiento.
---

---
2026-03-09 — INVESTIGADOR
**Aprendizaje:** Research exhaustivo de LinkedIn en marzo 2026 completado (15 búsquedas Perplexity sonar-pro). Reporte completo en `outputs/research/2026-03-09_research-linkedin-experto.md`. Hallazgos clave para el sistema:

1. El algoritmo de LinkedIn usa dos LLMs desde mid-2025: Causal LLM (recuperación) y 360Brew (ranking). Ya no es un sistema de señales simples — es razonamiento semántico. El perfil del creador es tratado como un "documento" que define a qué audiencias llega el contenido.

2. Formato rey sin discusión: carrusel/PDF con 21.77% de engagement mediano. Video: 7.35%. Imágenes: 6.52%. Links externos: 3.81% (penalizados). Texto puro: 3.18%. Los links externos deben ir en el PRIMER COMENTARIO, nunca en el cuerpo del post.

3. Frecuencia óptima para perfiles personales: 2-3 posts/semana. LinkedIn amplifica solo UN post por cuenta cada 24 horas — publicar más seguido canibaliza el propio alcance.

4. La "golden hour" es real y crítica: los primeros 60-120 minutos determinan si el post se amplifica. Discusiones de ida y vuelta generan 5.2x más amplificación. Responder comentarios aumenta engagement 30%; 83% de los perfiles mejoran cuando lo hacen.

5. Hashtags: contradicción de fuentes. LinkedIn Engineering (nueva arquitectura semántica) dice "zero impact". Hootsuite/Buffer/Sprout Social dicen "+20-50% alcance con 3-5 hashtags". Posición conservadora: usar 3-5 para categorización, no depender de ellos.

6. LinkedIn tiene 80M+ usuarios en LATAM. El nicho de automatización con IA en español NO está saturado en LinkedIn — oportunidad de posicionamiento para Hans como referente LATAM de n8n + monetización.

7. LinkedIn Ads tienen CPM $33-65 USD (vs. $6-15 de Meta) pero producen leads de mayor calidad para el Sub-avatar 1. ROI de pipeline documentado: 2.44x. Recomendación: orgánico LinkedIn primero, Ads solo cuando haya 3K+ seguidores y prueba social sólida.

8. Creator Mode debe activarse inmediatamente — cambia el botón de "Conectar" a "Seguir", desbloquea analytics, Live, Newsletter y hashtags de perfil.

9. El algoritmo tiene ventana de 30 días: posts con más de 30 días no pueden ser recuperados por FishDB. El contenido evergreen solo tiene valor dentro de esa ventana.

10. Método 5-5-5 de comentarios diarios confirmado como mejor práctica: 5 comentarios en cuentas de nivel superior + 5 en pares + 5 en audiencia objetivo. Hacerlo ANTES de publicar el propio contenido.
**Acción futura:** El agente experto en LinkedIn debe usar este reporte como base de conocimiento. Cuando Hans active LinkedIn como canal, el CREADOR debe adaptar los formatos de contenido (especialmente carruseles técnicos) al avatar profesional técnico.
---

---
2026-03-10 — INVESTIGADOR
**Aprendizaje:** Validación de mercado de los 5 ángulos de ads completada. Reporte completo en `outputs/research/2026-03-10_validacion-mercado-5-ads.md`. Hallazgos clave:

1. **Veredictos por ad:** Ad 1 (El Tiempo Perdido) y Ad 4 (El Tiempo Real) = LANZAR sin ajuste. Ad 5 (El Número), Ad 3 (El Anti-Ruido) y Ad 2 (Los Agentes de IA) = LANZAR CON AJUSTE (ver reporte para detalles específicos).

2. **"Agentes de IA" no es reconocido en LATAM en audiencia fría.** Confirmado por dos búsquedas independientes + datos del formulario de mercado (0/30 encuestados conocen n8n o términos técnicos). El Ad 2 necesita definir el término en los primeros 5 segundos O reservarse para retargeting/MOFU donde hay contexto previo.

3. **Adopción IA en empresas LATAM confirmada con datos:** 47% de empresas LATAM ya implementan IA en 2025, proyección 70% para 2026. México: 83% ROI positivo con IA. Colombia: 89% planea invertir en IA para 2026. Costa Rica: líder en LATAM en adopción (Índice ILIA 2025). Estos datos respaldan directamente el hook del Ad 4 y son útiles para el cuerpo de todos los ads.

4. **Precio $997 USD es competitivo en el segmento correcto.** El mercado LATAM tiene distribución polarizada: cursos DIY ($15-250 USD sin mentoría) vs programas con mentoría y garantía ($897-2,000 USD). Hans está en el segmento premium justificado por mentoría + garantía + proceso de ventas. El riesgo es que el espectador compare con Udemy sin entender la diferencia.

5. **Garantía de 90 días con resultado (primer cliente) SÍ diferencia.** La garantía de 7 días de devolución es estándar de plataforma — no diferencia. Una garantía de RESULTADO es menos común y reduce la barrera de entrada activamente. Comunicarla con condiciones claras para no atraer leads que solo buscan el reembolso.

6. **Competidores directos NO están en paid Meta Ads.** Agustín Medina, Migue Baena, Flujo Perfecto IA, HostGator operan en YouTube orgánico y Skool. Platzi opera en Meta Ads pero no en automatización IA con n8n. Hay una ventana de primer movedor en paid para Hans.

7. **Claims de ingreso sin prueba = escepticismo activo en LATAM.** Para que "$1,500 por proyecto" sea creíble: necesita (a) caso específico de alumno, (b) tipo de cliente y proyecto concreto, o (c) rango con condición. Nunca solo el número solo.

8. **Formato 45-54 segundos tiene respaldo para productos $500-$1,500.** Condición: los primeros 3 segundos deben parar el scroll visualmente + captions en todas las tomas (80% de Reels se ve sin sonido).

9. **CTA de DM keyword no está quemado.** Sigue siendo la mecánica estándar y soportada por Instagram. El riesgo es si el mismo público ya lo ha visto muchas veces — diferenciación está en la especificidad de la palabra clave ("AUTOMATIZAR" > "INFO").

10. **Anti-gurú genérico está saturándose.** "Yo no soy el típico gurú" ya todos lo dicen. La especificidad (herramienta concreta, tipo de cliente, resultado medible) hace más trabajo que el posicionamiento explícito de autenticidad.

**Acción futura:** El CREADOR debe incorporar los ajustes específicos identificados por ad antes de que Hans grabe. El orden de producción recomendado: Ad 1 → Ad 4 → Ad 5 (con ajuste) → Ad 3 (con calificador) → Ad 2 (con definición o para retargeting).
---

---
2026-03-24 — INVESTIGADOR
**Aprendizaje:** Research completo para webinar de Claude Code (25-26 marzo 2026). Hallazgos clave para el sistema:

1. **Claude Code es la herramienta más trending en IA ahora mismo (marzo 2026).** El movimiento "vibe coding" (crear apps y automatizaciones con solo lenguaje natural, sin programar) es viral. Claude Code es la herramienta central. Y Combinator reporta startups lanzando MVPs en un fin de semana.

2. **El hook de "sin programar" es el correcto para el avatar de Hans con Claude Code.** Su audiencia no son developers. Son profesionales técnicos que quieren resultados sin aprender a programar. Claude Code + n8n + Make = el stack completo para eso.

3. **Casos de uso concretos confirmados para el avatar:** Scrapers de prospectos (clínicas, restaurantes), automatización de reportes Excel, flujos de ventas completos con WhatsApp/email, herramientas internas de empresa — todo sin escribir código.

4. **Estadística útil para contenido:** Thoughtworks documentó +200% de output de código por ingeniero con Claude Code. Dato poderoso para justificar la relevancia de la herramienta.

5. **Estrategia webinar en 48-72h:** Con audiencia orgánica de 5K-20K seguidores y la estrategia correcta (3-5 Reels/día + Stories con countdown + CTA por DM/link) se pueden obtener 200-500 registros. El CTA por DM con palabra clave ("escríbeme CLAUDE") sigue siendo efectivo.

6. **Re-engagement de leads fríos:** Tasa esperada 20-30% con secuencia personalizada. El mejor ángulo para reactivar con el webinar gratuito: "valor gratuito irresistible, sin presión de venta." Mensaje en WhatsApp/DM que funciona: anunciar el evento como novedad de IA de interés, no como oferta de venta.

7. **Coherencia de marca para Hans:** Claude Code es de Anthropic, la misma empresa cuyo modelo (Claude) usa en todas sus automatizaciones. Ángulo poderoso: "enseño el ecosistema correcto, no IA genérica."
**Reporte completo:** `outputs/research/webinar-claude-code-research.md`
---

---
2026-03-25 — INVESTIGADOR
**Aprendizaje:** Research profundo de Claude Code para clase introductoria (8 búsquedas sonar-pro). Datos técnicos confirmados útiles para el sistema:

1. **Instalación correcta en 2026:** El método `npx claude-code` o `npm install -g @anthropic-ai/claude-code` está DEPRECADO desde v2.1.15. El método correcto es el instalador nativo: `curl -fsSL https://claude.ai/install.sh | bash` (Mac/Linux) o `irm https://claude.ai/install.ps1 | iex` (Windows PowerShell). No requiere instalar Node.js por separado.

2. **Requisito de suscripción:** Claude Code solo funciona con Claude Pro ($20/mes), Max, Teams o Enterprise. El plan gratuito no lo incluye. Dato importante para mencionar en cualquier clase o contenido sobre Claude Code.

3. **Comparativa de herramientas confirmada (2026):** Claude Code = tareas autónomas complejas (CLI). Cursor = edición diaria en IDE con IA. GitHub Copilot = sugerencias inline para principiantes que aprenden a programar. Windsurf = codebases grandes en equipo. Para el avatar de Hans (no programador que quiere automatizar), Claude Code es la herramienta correcta porque ejecuta tareas completas con instrucciones en lenguaje natural.

4. **84% de desarrolladores ya usa IA como estándar de trabajo** (Stack Overflow 2026). Dato útil para contextualizar la relevancia de Claude Code en clases y contenido.

5. **Claude Code genera $1,000 millones en ingresos anualizados** como producto. Dato de credibilidad para mencionar en la clase (la herramienta no es un experimento, es un negocio establecido).

6. **El complemento oficial de Claude para Excel** existe y se instala desde Microsoft AppSource. Relevante para el avatar que trabaja con Excel — no necesita Claude Code para automatizar Excel, puede usar el complemento directamente desde Excel.

7. **Advertencia de tutoriales desactualizados:** En YouTube hay muchos tutoriales de 2025 que usan el método `npx claude-code`. Son obsoletos. El instalador nativo de 2026 es más simple y no requiere Node.js previo.

**Reporte completo:** `outputs/webinar-claude-code/research-claude-code-clase1.md`
---

---
2026-03-30 — INVESTIGADOR
**Aprendizaje:** Análisis profundo de Neurogrowth/Ron Duarte completado (14 búsquedas Perplexity sonar-pro). Reporte completo en `outputs/research/2026-03-30_neurogrowth-linkedin-flywheel-profundo.md`. Hallazgos clave:

1. **Neurogrowth no tiene validación externa verificable.** Cero menciones en G2, Clutch, Trustpilot, medios de terceros o blogs. Sus case studies son 100% autoproducidos. Para Hans, lograr 3-5 testimonios verificables externos supera ese estándar de credibilidad.

2. **El LinkedIn Flywheel y todos sus frameworks son rebrandings de conceptos públicos.** Message-Market Fit Protocol, Allbound Growth Protocol y LinkedIn Flywheel son nombres de marca sobre prácticas estándar de la industria. La barrera de entrada al conocimiento es cero.

3. **El modelo de Neurogrowth fue diseñado para B2B enterprise, NO para educators.** Los datos 2025-2026 son consistentes: outbound masivo automatizado funciona para agencias vendiendo a empresas con tickets $5K-20K+. Para educators vendiendo programas de formación, content-led growth + outreach selectivo tiene 40% menor CAC. Copiar este modelo para vender la academia es un error estratégico.

4. **Precios de mercado reales del servicio:** El promedio de la industria es $5,200/mes (Clutch, 150+ agencias). Tier básico: $2,000-4,000/mes. Esto crea un ángulo de ad poderoso para Hans: "En lugar de pagar $3,000/mes a una agencia para conseguir clientes, aprende el método y aplícalo tú mismo por $997 una sola vez."

5. **Benchmarks reales de LinkedIn outreach 2025:** Reply rate promedio: 10-11% (Expandi, millones de outreach). Optimizado con personalización real: 15-25%. Tasa de aceptación de conexiones: 27% promedio / 45% con personalización. Cold email de comparación: 3.8-5.1%. LinkedIn es 2x mejor que email en reply rate. Multichannel (LinkedIn + email): 3.5x más respuestas que solo LinkedIn.

6. **Límites seguros de automation en LinkedIn 2026:** Mensajes con Sales Navigator: 250/día. Conexiones: 20-100/día (según antigüedad de cuenta). Las herramientas cloud-based (Expandi, Dripify, Waalaxy) tienen tasas de ban <0.1% para usuarios de pago. El modelo de 60-100 msgs/día de Neurogrowth está dentro de los límites seguros.

7. **Sales Navigator pricing 2026:** Core: $99/mes mensual. Advanced (con Buyer Intent data): $179/mes mensual. El stack completo de Neurogrowth probablemente cuesta al cliente: Sales Navigator + herramienta automation + fee agencia = $2,200-4,250/mes mínimo.

8. **No hay competidores de Neurogrowth en LATAM hispanohablante.** El mercado de LinkedIn outreach B2B as-a-service en español es prácticamente inexistente. Esto explica cómo operan sin marketing visible: no tienen competencia directa en español.
**Acción futura:** El ESTRATEGA debe evaluar si agregar un módulo de "LinkedIn para conseguir clientes" a la academia de Hans crea ventaja diferencial. El ángulo de precio vs agencia ($997 academia vs $3,000+/mes agencia) es un hook potencialmente poderoso para Sub-avatar 1.
---

### Skills LinkedIn nuevos (2026-03-30)
Basado en el reverse engineering del LinkedIn Flywheel de Ron Duarte/Neurogrowth, se crearon 4 skills nuevos y se enriquecieron 2 existentes:

**Skills nuevos:**
- `signal-detector` — rutina semanal de deteccion de senales de interes (profile views, comentarios recurrentes). Alimenta al warm-outreach.
- `icp-mapper` — listas de cuentas target por tier (1-influencers, 2-peers, 3-avatar). Hace el metodo 5-5-5 mas efectivo.
- `warm-outreach` — templates de DM para contactar personas que ya mostraron interes. NUNCA cold. Maximo 10-15 DMs/semana.
- `message-fit-tester` — A/B testing de angulos de contenido: 3 angulos x 3 semanas, trackear cual resuena con el avatar.

**Skills enriquecidos:**
- `profile-optimizer` — agregado framework "perfil como landing page" con tabla de funcion de conversion por seccion.
- `retro-analyst` — agregados KPIs de senales (profile views, conexiones avatar, DMs inbound, warm conversations, comentaristas recurrentes, calls agendadas).

**Docs nuevos:**
- `docs/linkedin-icp-tiers.md` — documento de listas de cuentas target (pendiente de poblar)
- `docs/linkedin-lead-signals.md` — catalogo de senales y que hacer con cada una
- `docs/linkedin-warm-outreach-playbook.md` — playbook de outreach calido vs frio

**Templates nuevos:**
- `templates/linkedin-weekly-signals.md`
- `templates/linkedin-angle-test.md`
- `templates/linkedin-warm-dm.md`

**Decision estrategica clave:** El outbound masivo automatizado (60-100 msgs/dia con spintax) NO aplica a nuestro modelo de marca personal educativa. Nuestro enfoque es: 80% contenido de autoridad + 20% warm outreach manual a personas que mostraron interes. Esto esta validado por datos de mercado 2025-2026 (content-led growth tiene 40% menor CAC que outbound masivo para educators/coaches).

---

## Notas de Operación

- Este archivo es de escritura continua — los agentes agregan, no reemplazan.
- Si un aprendizaje contradice uno anterior, marcar el anterior como `[DEPRECADO]` y agregar el nuevo.
- Hans puede revisar este archivo para entender cómo está evolucionando el sistema.
