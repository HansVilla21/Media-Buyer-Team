# MEMORY.md — INVESTIGADOR (Momentum AI Academy)

## Entorno Técnico
- Node.js v22 disponible. Usar Node para llamadas a Perplexity (curl + bash falla en Windows con JSON complejo).
- Perplexity API key en `.env` del proyecto. Modelo siempre: sonar-pro.
- Ruta del proyecto: `C:/Users/hvill/Documents/Cloude Code/Media Buyer Team`

## Patrón de Llamada a Perplexity (Node.js)
Usar módulo `https` nativo con `JSON.stringify()` para el payload. Ver `memory/learnings.md` entrada 2026-03-09 para el snippet de código funcional.

## Filtros de Relevancia para la Audiencia de Hans
El avatar es Andrés/Carolina, 28-35 años LATAM, sin background técnico, quiere ganar dinero con IA.

Filtrar SIEMPRE por: "¿un profesional LATAM sin experiencia técnica puede entender esto en 10 segundos y ver por qué le importa a su bolsillo?"

Descartar activamente:
- Controversias político-militares (Pentágono, regulación de defensa)
- Benchmarks técnicos sin traducción a impacto práctico
- Noticias de competidores entre empresas de IA sin ángulo de oportunidad para el usuario
- Procesos de empresas Fortune 500 con equipos de 20+ personas (no aplica a Hans)

## Datos Base de Claude a Marzo 2026 (verificados)
- Claude Pro: $17-20 USD/mes (vs $200 ChatGPT Pro)
- Usuarios activos web: 18.9M/mes
- Crecimiento usuarios gratuitos enero-marzo 2026: +60%
- Integración con Microsoft 365: anunciada 9 marzo 2026
- Claude Marketplace (sin comisiones): lanzado 6 marzo 2026
- Valoración Anthropic: $380,000 millones USD
- Ingresos anualizados: $14,000 millones (14x interanual)

Usar como referencia hasta que haya datos más recientes. Aclarar fecha si han pasado +30 días.

## Datos de Media Buyer Profesional (investigados 2026-03-09)
Reporte completo en: `outputs/research/2026-03-09_media-buyer-profundo.md`

Benchmarks clave (pendiente confirmación con datos reales de Hans):
- ROAS objetivo infoproductos: 3-5x (rentable), >4x ideal
- CTR video educativo Meta: 2-3% bueno, <1% señal de problema
- Frecuencia máxima antes de rotar creative: 3-4
- Duración mínima A/B test: 4-6 semanas
- Creative = 70% del resultado en Meta (vs 30% targeting/bid)
- CPL en paid social sube +21% interanual (2024-2025)

Cambio más importante 2025-2026: el avatar se "infunde" en el creative, no en el targeting manual. Broad targeting + Advantage+ dejan que la IA de Meta encuentre al comprador leyendo el creative.

## Datos de Optimización Meta Ads (investigados 2026-03-09)
Reporte completo en: `outputs/research/2026-03-09_optimizacion-trabajo-remoto.md`

Benchmarks confirmados 2025-2026 (pendiente validación con datos reales de Hans):
- CTR saludable Instagram Meta Ads: >1.5% (CTR de 0.353% = 4x por debajo del mínimo)
- Frecuencia donde empieza fatiga real: 3.5-4.0 (no a 2.0-2.5)
- Reels: 30.81% reach rate vs 13.14% del Feed; captura >50% tiempo de usuarios en Instagram
- Broad targeting gana sobre intereses para profesionales técnicos: 60-70% de los casos, 28% menor CPA
- Below Average quality + Above Average conversion = problema de creative (hook no detiene scroll del avatar correcto), NO problema de embudo
- Mejorar quality ranking de Below Average a Average+ reduce costos 20-40% sin cambiar bid
- CBO para escala de ad sets probados; ABO para testing de creativos nuevos
- 50 conversiones/semana necesarias para que Meta salga de la fase de aprendizaje

Insight crítico campaña "Trabajo Remoto": CTR mejor en 55-64 (2.44%) que en 28-42 (avatar objetivo). El hook actual resuena con profiles mayores. Ángulo de aceleración (no miedo) para el profesional técnico 28-42.

## Gap de Datos: LATAM
No existen casos documentados en medios hispanohablantes de empresas pequeñas/freelancers LATAM usando Claude con n8n/Make/WhatsApp (confirmado marzo 2026). Esto es una oportunidad de posicionamiento para Hans.

No existen benchmarks específicos de Costa Rica en Perplexity. Usar LATAM general (referencia: Brazil CPM ~$2.63) como proxy.

## Skills de Investigación Disponibles
- `.agent/skills/investigacion/research-rol-profesional/SKILL.md` — Para investigar roles profesionales en profundidad con Perplexity (8 queries, formato estándar). Creada 2026-03-09.

## Queries que Funcionan Bien para Research de Meta Ads
- Combinar: [elemento específico] + [plataforma] + [año 2025 2026] — siempre incluir ambos años
- Para situaciones paradójicas o inusuales: hacer búsquedas adicionales específicas sobre la paradoja
- 10-12 búsquedas para análisis de campaña completo produce diagnóstico confiable

## Queries que Funcionan Bien para Research de Roles
Combinar: [rol] + [plataforma específica] + [acción específica] + [año]
Evitar queries genéricos sin contexto de plataforma o industria.

## Terminología de IA: Potencia por Contexto (investigado 2026-03-09)
Reporte completo en: `outputs/research/2026-03-09_research-angulos-ads-ia.md`

- "IA" sola: mayor volumen de atención (usar en hooks de 0-2 segundos)
- "Automatizaciones con IA": combinación ganadora para el cuerpo del ad — especifica + filtra
- "Automatizaciones" sola: término técnico frío, no funciona en audiencia fría TOFU
- "Agentes de IA": MAYOR OPORTUNIDAD no explotada — tendencia viral LATAM 2025-2026, ningún competidor lo posiciona en español con monetización + n8n
- n8n nombrado explícitamente en ad = filtro de calificación del Sub-avatar 1 correcto

## Competidores Identificados en el Nicho de Hans (marzo 2026)
- Rodrigo Camacho: YouTube gratuito, HighLevel no n8n, USA-centric, $10K/mes como promesa
- IDIA.es: España, agentes IA n8n, sin presencia LATAM vía paid
- HostGator Español: tutorial gratuito n8n 1 hora, sin proceso de ventas ni mentoría
- Ninguno ataca al Sub-avatar 1 (profesional técnico LATAM) con proceso de ventas incluido

## Ángulos de Ads Identificados para Hans (pendiente validación A/B real)
5 ángulos para testear, en orden de prioridad:
1. "El Acelerador" — Sub-avatar 1, convierte la habilidad técnica existente en ingreso
2. "Los Agentes de IA" — diferenciación + tendencia emergente, posiciona a Hans adelante
3. "El Anti-Ruido" — filtra falso avatar, distingue de cursos ChatGPT genéricos
4. "El Tiempo Real" — urgencia sin miedo, ángulo de aceleración (no "te reemplazarán")
5. "El Número del Financiamiento" — Sub-avatar 2, elimina objeción de precio desde el hook

## Queries que Funcionan Bien para Research de Ángulos de Ads
- Buscar el ángulo específico + tipo de infoproducto + mercado + año: produce resultados concretos
- Para competidores: buscar por nombre de herramienta (n8n, HighLevel) + instructor + español
- Para términos de mercado: buscar tanto "IA" como "automatización" por separado para triangular
- Búsqueda de hooks virales en reels en español: Perplexity retorna cursos de España, NO LATAM — usar inferencia cruzada de búsquedas de copywriting y Meta Ads en su lugar

## Datos de LinkedIn 2026 (investigados 2026-03-09)
Reporte completo en: `outputs/research/2026-03-09_research-linkedin-experto.md`

Benchmarks confirmados (15 búsquedas sonar-pro):
- Engagement rate LinkedIn 2025: 6.2% general (la más alta de todas las redes)
- Carrusel: 21.77% engagement mediano (formato rey, 3x sobre video)
- Video nativo: 7.35% | Imágenes: 6.52% | Links: 3.81% | Texto: 3.18%
- Frecuencia óptima perfiles personales: 2-3 posts/semana (LinkedIn amplifica 1 post/24h)
- Hashtags: 3-5 óptimo. Contradicción de fuentes — usar para categorización, no como motor principal
- Golden hour: primeros 60-120 minutos son críticos. Discusiones de ida y vuelta: 5.2x amplificación
- Responder comentarios: +30% engagement, 83% de perfiles mejoran al hacerlo
- LinkedIn Ads CPM: $33-65 USD (vs. $6-15 de Meta). Pipeline ROI: 2.44x por $1 invertido
- Lead Gen Forms: 13% tasa de completado (vs. 2-5% landing page externa)
- LATAM LinkedIn: 80M+ usuarios. México, Brasil, Argentina, Colombia lideran

Algoritmo 2026 (LLMs): Causal LLM (recuperación) + 360Brew (ranking). Ventana estricta de 30 días.
El perfil del creador es tratado como "documento" — define a qué clusters llega el contenido.
Links externos penalizados. Poner links SIEMPRE en el primer comentario, nunca en el cuerpo del post.
Creator Mode: activar antes de empezar cualquier estrategia. Cambia Connect por Follow.

Recomendación para Hans: LinkedIn orgánico primero. LinkedIn Ads solo con 3K+ seguidores + prueba social.
Sub-avatar 1 (profesional técnico) está activo en LinkedIn. Es el canal más relevante para él.
El nicho de automatización con IA en español NO está saturado en LinkedIn — oportunidad de posicionamiento.

## Claude Code — Datos Clave (investigado 2026-03-24)

Reporte completo en: `outputs/research/webinar-claude-code-research.md`

- Claude Code = herramienta CLI de Anthropic que actúa como agente autónomo en la terminal del usuario
- Diferencia con Claude web: Claude web responde. Claude Code hace cosas reales en el computador.
- Requiere Claude Pro ($20/mes), Node.js instalado. Setup en menos de 5 minutos.
- Movimiento "vibe coding" = crear apps y automatizaciones con solo lenguaje natural, sin programar. Claude Code es la herramienta líder. Y Combinator lo usa activamente.
- Productividad documentada: Thoughtworks reportó +200% de output por ingeniero con Claude Code.
- Casos de uso para avatar de Hans: scrapers de prospectos, automatización de reportes Excel, flujos de ventas WhatsApp/email, herramientas internas de empresa.
- Hook viral de Hacker News: "Tengo 60 años. Claude Code mató mi pasión por programar" — generó debate masivo en 2025-2026.
- Ángulo correcto para el avatar de Hans: "sin programar" / "sin saber código". No posicionar para developers.
- Coherencia de marca: Claude Code es de Anthropic, la misma empresa cuyo modelo Claude usa Hans. "Enseño el ecosistema correcto."

## Estrategia Webinar en Tiempo Corto (48-72h) — Confirmada en Research

- Con 5K-20K seguidores orgánicos: expectativa realista 200-500 registros en 48h
- Formato: 3-5 Reels/día + Stories con countdown + CTA por link en bio o DM con palabra clave
- Tasa de re-engagement esperada con mensaje personalizado en WhatsApp/DM: 20-30%
- CTA por DM con palabra clave sigue funcionando en Instagram (confirmado en múltiples búsquedas)

## Regla de Escritura en Memoria
Solo agregar datos confirmados por Hans o verificados por fuentes. No especular.
