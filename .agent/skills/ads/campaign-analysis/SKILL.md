# Skill: Análisis de Campañas con Reglas de Decisión

**Versión:** 1.0
**Creada:** 2026-03-09
**Usada por:** MEDIA BUYER

---

## Para qué sirve esta skill

Cuando Hans comparte métricas de Meta Ads, el MEDIA BUYER no solo las analiza — toma decisiones concretas basadas en reglas predefinidas. Esta skill elimina la ambigüedad: para cada situación hay una acción clara.

---

## Cómo recibir y procesar métricas

Hans puede compartir métricas de diferentes formas:
- Copy/paste desde Meta Ads Manager
- Captura de pantalla
- Lista manual de números

En todos los casos, extrae los valores de:
`CTR | CPM | CPC | CPL | ROAS | Frecuencia | Gasto total | Conversiones | CPA`

Si faltan métricas críticas, pregunta antes de analizar.

---

## Tabla de Decisiones (aplicar en orden)

### 1. ¿Cuánto tiempo lleva corriendo el ad?

| Situación | Acción |
|-----------|--------|
| < 3 días | **ESPERAR.** La IA de Meta necesita tiempo para optimizar. No tocar nada. |
| < 50 conversiones acumuladas | **ESPERAR.** Meta no tiene suficientes datos para estabilizar. |
| 3+ días y 50+ conversiones | **PROCEDER AL ANÁLISIS.** |

### 2. ¿Cómo está el ROAS?

| ROAS | Acción |
|------|--------|
| > 3x por 3+ días | **ESCALAR:** aumentar presupuesto 25-30%. No más en un solo día. |
| 1.5x – 3x por 3+ días | **MANTENER:** el ad es rentable. Monitorear si sube. |
| 1x – 1.5x | **OBSERVAR:** cerca del break-even. Revisar CTR y CPA antes de decidir. |
| < 1x por 48+ horas | **PAUSAR:** pérdida confirmada. Detener y briefear nuevo creative. |

### 3. ¿Cómo está el CTR?

| CTR | Señal | Acción |
|-----|-------|--------|
| > 2% | Hook funcionando | Mantener o escalar |
| 1.5% – 2% | Aceptable | Monitorear |
| 1% – 1.5% | Hook débil | Iterar creative en el próximo ciclo |
| < 1% | Hook muerto | Brief nuevo creative con urgencia |
| < 0.5% | Emergencia | Pausar el ad y briefear inmediatamente |

### 4. ¿Cómo está la Frecuencia?

| Frecuencia | Señal | Acción |
|------------|-------|--------|
| < 3 | Sano | Continuar |
| 3 – 4 | Fatiga temprana | Preparar nuevo creative aunque el ROAS sea bueno |
| 4 – 5 | Fatiga media | Brief urgente de nuevo creative, no escalar |
| > 5 | Audiencia quemada | Renovar creative O ampliar audiencia (Advantage+) |
| > 7 | Crítico | Pausar ad o duplicar campaña con targeting más amplio |

### 5. ¿Cómo está el CPM?

| CPM | Señal | Acción |
|-----|-------|--------|
| < $8 | Eficiente | Buena relevancia del creative |
| $8 – $15 | Normal | Dentro del benchmark |
| > $15 | Alto | Revisar si el creative es relevante o hay saturación del nicho |
| Subió > 20% vs. promedio | Alerta | Competencia aumentó en la subasta o creative está perdiendo relevancia |

### 6. ¿Cómo está el CPA?

| CPA vs. objetivo | Acción |
|-----------------|--------|
| < objetivo | Escalar si ROAS también es bueno |
| 1x – 1.5x objetivo | Observar 48 horas más |
| > 1.5x objetivo por 3 días | Pausar o iterar creative |

---

## Formato del Reporte de Análisis

```markdown
# Análisis de Campaña: [Nombre o período]
Fecha: YYYY-MM-DD
Datos aportados por: Hans
Período analizado: [fechas]

---

## Métricas recibidas

| Métrica | Valor actual | Benchmark | Estado |
|---------|-------------|-----------|--------|
| CTR | X% | 1.5-2% | 🟢/🟡/🔴 |
| CPM | $X | <$15 | 🟢/🟡/🔴 |
| CPC | $X | <$2 | 🟢/🟡/🔴 |
| ROAS | Xx | >1.5x | 🟢/🟡/🔴 |
| Frecuencia | X | <4 | 🟢/🟡/🔴 |
| CPA | $X | <objetivo | 🟢/🟡/🔴 |

## Diagnóstico (qué está pasando realmente)
[2-3 oraciones directas sobre la situación]

## Decisiones recomendadas

### Acción inmediata (hacer hoy)
- [Acción 1 con justificación]

### Acción esta semana
- [Acción 2]

### Acción en el próximo ciclo (7-14 días)
- [Acción 3]

## Lo que NO tocar
[Qué está funcionando y no debe modificarse]

## Próximo hito de revisión
[Cuándo volver a revisar y qué métrica va a arbitrar la decisión]
```

---

## Reglas de oro para el análisis

1. **Nunca tomes decisiones con menos de 3 días de datos.** La IA de Meta necesita tiempo.
2. **Nunca cambies más de una variable a la vez.** Si cambias el creative, no cambies también el presupuesto.
3. **Escala gradualmente.** Nunca más del 30% de presupuesto en un solo día.
4. **El CTR alto + ROAS bajo** = el creative atrae pero la oferta o la landing no convierte. Problema de MOFU/BOFU.
5. **El CTR bajo + buena frecuencia** = el creative está fatigado, no la oferta.
6. **El CPM subiendo + CTR bajando** = el creative está perdiendo relevancia para el algoritmo.
