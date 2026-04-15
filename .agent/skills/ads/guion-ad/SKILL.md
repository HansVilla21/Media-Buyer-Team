# SKILL: Guion de Ad para Meta Ads
Versión: 1.0
Agente propietario: MEDIA BUYER
Agentes que pueden invocarla: COMANDANTE, MEDIA BUYER, CREADOR
Última actualización: 2026-03-09
Base de conocimiento: research de 12 búsquedas Perplexity + análisis de llamadas + team meeting 09/03

---

## ¿Qué hace este skill?

Produce guiones de video para Meta Ads (Facebook/Instagram) de Momentum AI Academy. Un guion por sub-avatar, un ángulo por guion, listo para que Hans lo grabe.

**Diferencia crítica con contenido orgánico:** Los ads pueden tener hooks más directos y disruptivos. No tienen que ser anti-gurú al 100% — sí deben ser honestos y sin promesas imposibles, pero pueden usar urgencia real y apelar al dolor de forma más directa que el orgánico.

---

## Inputs necesarios

| Input | Obligatorio | Descripción |
|-------|-------------|-------------|
| Sub-avatar objetivo | ✅ | Sub-avatar 1, 2 o 3 (ver `memory/avatar.md`) |
| Ángulo del ad | ✅ | Ver la lista de ángulos confirmados abajo |
| Etapa del funnel | ✅ | TOFU / MOFU / BOFU |
| Research de la competencia | ❌ | Si existe en `outputs/research/`, usarlo |
| CTA deseado | ❌ | Palabra clave para el DM (ej: PROCESOS, AGENTE, REAL) |

---

## Los 5 Ángulos Confirmados (investigados con Perplexity marzo 2026)

### ÁNGULO 1 — "El Acelerador Refinado" (identidad técnica)
**Para:** Sub-avatar 1 (Profesional Técnico)
**Hook:** Nombrar explícitamente el perfil en los primeros 2 segundos
**Fórmula:** "Si trabajás con [Excel/Jira/ERP/procesos], esto te interesa..." → qué hace Hans → caso real con número → CTA
**CTA recomendado:** PROCESOS
**Por qué funciona:** El Sub-avatar 1 se identifica inmediatamente. El algoritmo de Meta aprende el perfil del que hace clic.

### ÁNGULO 2 — "Los Agentes de IA" (término trending sin monetizar)
**Para:** Sub-avatar 1 + 2
**Hook:** "Agentes de IA" en las primeras palabras — mayor potencial en LATAM sin explotar
**Fórmula:** "¿Sabés qué es un agente de IA?" → diferencia con automatización simple → cómo se monetiza → nadie en LATAM lo enseña en español → CTA
**CTA recomendado:** AGENTE
**Por qué funciona:** "Agentes de IA" está creciendo viralmente. Ningún competidor LATAM lo monetiza en español con n8n.

### ÁNGULO 3 — "El Anti-Ruido" (frustración con cursos anteriores)
**Para:** Sub-avatar 2 (ha tomado cursos que no funcionaron)
**Hook:** "¿Ya tomaste un curso de IA y no generaste nada?" → validar la frustración → por qué fallan → qué es diferente acá → CTA
**CTA recomendado:** REAL
**Por qué funciona:** El avatar 2 tiene historial de cursos sin resultados. El anti-hype es diferenciador.

### ÁNGULO 4 — "El Tiempo Real" (urgencia de oportunidad, no de miedo)
**Para:** Sub-avatar 1 (ya ve la IA llegando a su empresa)
**Hook:** "La automatización ya está en tu empresa. La pregunta es si estás del lado correcto."
**Fórmula:** Urgencia de oportunidad (no de miedo/quedar obsoleto) → qué pasa con quienes aprenden → cómo monetizarlo → CTA
**CTA recomendado:** EMPRESA
**Por qué funciona:** Urgencia real sin apocalipsis laboral. Resuena en 28-42, no en 45+.

### ÁNGULO 5 — "El Número" (financiamiento como argumento central)
**Para:** Sub-avatar 2 (tiene capacidad pero siente que $997 es mucho)
**Hook:** "$100 al mes para aprender a cobrar $1,500 por proyecto"
**Fórmula:** El número de financiamiento primero → qué se aprende → cuánto se puede cobrar → ROI directo → garantía 90 días → CTA
**CTA recomendado:** MES
**Por qué funciona:** La objeción #1 es el precio. Mostrar el financiamiento como argumento principal, no como nota al pie.

---

## Estructura Base del Guion (para todos los ángulos)

```markdown
# Ad Script: [Ángulo]
Versión: v1
Fecha: YYYY-MM-DD
Duración estimada: 45-60 segundos
Ángulo: [El Acelerador / Los Agentes de IA / El Anti-Ruido / El Tiempo Real / El Número]
Etapa del funnel: [TOFU / MOFU / BOFU]
Sub-avatar: [Sub-avatar 1 / 2 / 3]
CTA palabra clave: [PROCESOS / AGENTE / REAL / EMPRESA / MES]

---

## HOOK (0–3 seg) ← Crítico. Con o sin sonido debe parar el scroll.
**Hablado:** [Frase exacta de apertura]
**En pantalla (overlay):** [Texto superpuesto — máx. 5-7 palabras]
**Visual:** [Hans en cámara / pantalla de n8n / B-roll]

## CREDIBILIDAD RÁPIDA (3–8 seg)
[Quién es Hans y por qué confiarle — 1 línea, sin sonar arrogante]

## CUERPO (8–40 seg)
[El argumento principal — beneficios, no características]
[Demo real o caso real con número concreto]
[Avatar infundido: lenguaje exacto del sub-avatar]

## OFERTA / GARANTÍA (40–50 seg) — Solo en MOFU/BOFU
[Qué ofrece, precio o financiamiento, garantía 90 días]

## CTA (últimos 8-10 seg)
[Acción exacta: "Comentá [PALABRA] por DM y te mando más info"]

---

## Copy del ad (texto del post en Meta)
**Headline:**
**Descripción primaria:**
**CTA button:** Más información

## Notas de producción
[Cómo grabarlo, formato, si es con o sin pantalla]
```

---

## Proceso de Producción

**Paso 1 — Leer contexto:**
- `memory/avatar.md` — sub-avatares y dolores documentados
- `memory/offer.md` — precio ($997 / $100 × 12), garantía 90 días
- `memory/brand-voice.md` — posicionamiento anti-gurú
- `memory/winning-content.md` — qué ha funcionado en ads anteriores

**Paso 2 — Seleccionar ángulo:**
- Confirmar con Hans o con el MEDIA BUYER cuál de los 5 ángulos se va a producir
- Un script = un ángulo = un sub-avatar. No mezclar.

**Paso 3 — Escribir 3 variantes de hook:**
- Nunca proponer solo 1 hook. Siempre dar 3 opciones.
- Hans elige cuál graba.

**Paso 4 — Completar el guion:**
- Usar estructura base de arriba
- Primera persona presente: "Estoy trabajando con...", "Acabo de cerrar..."
- Herramientas siempre nombradas: n8n, Claude, Make (nunca "herramientas de IA" genérico)
- Timelines honestos: si un resultado tomó 3 meses, decir 3 meses

**Paso 5 — Checklist antes de entregar:**
- [ ] Hook nombra explícitamente el perfil del sub-avatar o el dolor real
- [ ] Herramientas específicas nombradas (n8n, Claude, etc.)
- [ ] Resultado con número real (no inventado)
- [ ] CTA es una sola acción con palabra clave
- [ ] Sin promesas de ingresos sin contexto
- [ ] Sin urgencia falsa
- [ ] El guion suena a Hans, no a un anuncio corporativo

---

## Output

Guardar en: `outputs/ads/scripts/YYYY-MM-DD_v[n]_[angulo].md`

Cuando Hans confirme que el ad funcionó bien (CPR < objetivo, conversiones calificadas), registrar en:
- `memory/winning-content.md` — el hook, ángulo y resultado
- `memory/learnings.md` — el patrón que se puede replicar

---

## Hooks Confirmados que Funcionan en el Nicho

_(Se actualizan cuando Hans valida con resultados reales)_

- "Si trabajás con Excel, Jira o procesos en tu empresa, esto te interesa..." (Sub-av. 1)
- "¿Sabés qué es un agente de IA? Nadie en LATAM te está enseñando a monetizar esto..." (Sub-av. 1 y 2)
- "$100 al mes para aprender a cobrar $1,500 por proyecto" (Sub-av. 2 — financiamiento)
- "La automatización ya está en tu empresa. La pregunta es si estás de este lado..." (Sub-av. 1)

## Hooks Prohibidos (posicionamiento anti-gurú)

- "La verdad que nadie te dice sobre la IA"
- "Gana $5,000 al mes con ChatGPT"
- "El secreto que los expertos te ocultan"
- "Esto lo cambia todo"
- "En solo 30 días..." (sin datos reales que lo respalden)
