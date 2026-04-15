# MEMORY — Media Buyer Ads (Momentum AI Academy)

## Benchmarks Reales de Hans (prioridad sobre benchmarks de mercado)

- CPR ganador de referencia: ₡496.94 CRC (ad "trabajo remoto", mar 2026)
- CPM competitivo: ₡1,181 CRC (vs. ₡4,575–₡5,671 en ads débiles del mismo período)
- Umbral de pausa por CPR: ₡750 CRC (50% sobre el mejor CPR activo)
- Período analizado: 7 feb – 8 mar 2026

Ver detalle completo: `outputs/ads/analysis/2026-03-09_analisis-3-ads.md`

## Patrones Confirmados de Ads

### Hook de identidad > hook de oportunidad histórica
El hook "cambiar su trabajo de 9 a 5 a trabajo remoto" (deseo ya formado) produjo CPM 3-5x menor que "te perdiste Bitcoin en 2012" (referencia histórica). En LATAM de Hans, los hooks que activan un deseo ya nombrado superan a los que apuntan a FOMO de oportunidad pasada.

### Exclusión de alternativas como mecanismo de credibilidad
La frase "no estoy hablando de cripto, trading o empezar un negocio desde cero" es uno de los elementos más eficientes del ad ganador. Filtra el escepticismo y diferencia sin necesidad de probarlo. Incluir en todos los futuros scripts.

### La voz de Hans es "usted", no "tú"
El ad ganador usa "usted". Los dos ads débiles usan "tú". Consistente con brand-voice.md. Siempre escribir scripts con "usted" para el mercado de Hans.

### No repetir la misma prueba social en ads simultáneos
Los tres ads usaban casi la misma línea: "dejé el 9 a 5, generé $2,000 en un mes". Con audiencias solapadas, produce fatiga de mensaje. Diferenciar prueba social por ad.

## Señales de Fatiga de Ad en Meta (patrón detectado)

Combinación que indica ad en declive por audiencia receptiva agotada:
- Calidad: Debajo del promedio
- Engagement: Debajo del promedio
- Conversión: Por encima del promedio
- CPR subiendo >15% en el período

Acción correcta: no escalar, preparar reemplazo. Pausar cuando CPR supere 50% del valor inicial.

## Dato de Segmento de Edad (insight crítico)

En "trabajo remoto": 45-54 años CTR 1.56%, 55-64 años CTR 2.44%, vs. 18-24 años CTR 0.59%.
Hipótesis: el mensaje genérico de "trabajo remoto" atrae a un segmento de mayor edad que el avatar técnico confirmado (28-42 años). La solución es nichar por contenido del guión, no por targeting de audiencia.

## Campaña Activa — Datos Reales Mar 2026 (AD SET 2, corregido 2026-03-18)

- AD SET 2 creado: 2026-03-13 (no el 16 — lleva 5 días activo)
- CPR actual: ₡2,590 CRC — 5.2x más caro que el ganador histórico (₡497). Con 5 días en aprendizaje, no es alarma aún.
- CPM actual: ₡2,547 CRC
- CTR promedio: 0.86% (rango: 0.50%–0.97%)
- Ad favorito del algoritmo: AD 5 "Intentaste Solo METODO" (CTR 0.97%, CPC ₡253, 13 conv., 51% del gasto)
- Ad segundo lugar: AD 1 "El Tiempo Perdido PROCESOS" (CTR 0.76%, 11 conv., 40% del gasto)
- Ads con gasto mínimo y candidatos a pausa: AD 3 (0 conv., CPM más alto) y AD 4 (CTR 0.50%, 1 conv.)
- Geo: solo Costa Rica — audiencia limitada
- Objetivo: OUTCOME_ENGAGEMENT / Conversaciones DM
- Estado: en fase de aprendizaje (~6 conv/día vs. 50/semana requeridas para salir)

CORRECCIÓN IMPORTANTE: El análisis anterior del 2026-03-18 tenía invertidos los datos del AD 4 y AD 5. El ad ganador real es el AD 5 "Intentaste Solo", NO el AD 4 "La Curva No Para".

Ver análisis corregido: `outputs/ads/analysis/2026-03-18_analisis-adset2-corregido.md`

## Patrón Confirmado: El Algoritmo Selecciona Solo 2 de 5 Ads (mar 2026)

Con 5 ads activos en un ad set, Meta concentró >91% del presupuesto en 2 ads (AD 1 y AD 5). Los otros 3 recibieron gasto simbólico. Con ₡15,000/día, no lanzar más de 3 ads simultáneos en el mismo ad set.

## Ángulo de Método/Solución Personal = Mejor CTR en Prueba Mar 2026 (CORREGIDO)

El ad "Intentaste Solo" con ángulo "tratar de aprenderlo solo sin método estructurado es el error" obtuvo el mejor CTR (0.97%) y mejor CPC (₡253) entre los 5 ads. El ángulo de adopción empresarial de IA (AD 4 "La Curva No Para") tuvo en realidad el peor CTR (0.50%) y casi ninguna distribución del algoritmo.

## Archivos Clave de Referencia

- `outputs/ads/analysis/2026-03-09_analisis-3-ads.md` — análisis completo de 3 ads (AD SET 1 histórico)
- `outputs/ads/analysis/2026-03-18_analisis-adset2-corregido.md` — análisis AD SET 2 corregido (5 días reales)
- `outputs/ads/analysis/2026-03-18_analisis-campana-activa.md` — análisis anterior INCORRECTO (datos AD 4/AD 5 invertidos)
- `memory/avatar.md` — sub-avatares confirmados (Profesional Técnico es prioridad)
- `memory/offer.md` — oferta, precios, garantía
- `memory/brand-voice.md` — voz de Hans, estructura narrativa
