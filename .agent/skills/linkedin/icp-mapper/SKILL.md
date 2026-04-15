---
name: linkedin-icp-mapper
version: v1
description: Framework para definir, mantener y priorizar listas de cuentas target en LinkedIn por tier — alimenta el metodo 5-5-5, la estrategia de comentarios y el warm outreach.
---

# LinkedIn ICP Mapper

## Cuando usar este skill

- Al iniciar la estrategia de LinkedIn (setup unico)
- Mensualmente para actualizar y refrescar las listas
- Cuando Hans siente que comenta en cuentas que no le generan retorno
- Cuando el metodo 5-5-5 se siente ineficiente (comentar por comentar)
- Cuando el Sub-avatar 1 cambia o se refina

## Cuando NO usar este skill

- Para definir el avatar general (eso vive en `memory/avatar.md`)
- Para crear contenido (usar `linkedin/post-writer`)
- Para enviar mensajes (usar `linkedin/warm-outreach`)
- Para buscar tendencias de mercado (usar `linkedin/signal-researcher`)

## Inputs necesarios

- **Avatar actual**: `memory/avatar.md` (especialmente Sub-avatar 1)
- **Estrategia LinkedIn**: `docs/linkedin-strategy.md`
- **Nicho de Hans**: automatizacion IA, n8n, Claude, educacion tecnica LATAM
- **Cuentas que Hans ya sigue o interactua** (opcional pero util)

## Workflow

1. **Leer contexto**: avatar.md + linkedin-strategy.md
2. **Definir criterios por tier** (ver abajo)
3. **Investigar y poblar** cada tier con cuentas reales
4. **Validar** que cada cuenta cumple los criterios
5. **Documentar** en `docs/linkedin-icp-tiers.md`
6. **Revisar mensualmente** — agregar, quitar, mover entre tiers

## Instrucciones

### Los 3 Tiers de Cuentas Target

#### Tier 1 — Influencers del Nicho (5-15 cuentas)
**Que son:** Creadores con 10K+ seguidores que publican sobre IA, automatizacion, no-code, o transformacion digital en LATAM o en espanol.
**Por que importan:** Comentar en sus posts te expone a SU audiencia (que es tu avatar). Un comentario bueno en una cuenta de 50K seguidores puede generar mas profile views que tu propio post.
**Criterios:**
- 10K+ seguidores en LinkedIn
- Publica al menos 2x/semana
- Su audiencia overlaps con el Sub-avatar 1 de Hans
- Contenido en espanol o bilingue

**Como identificar:** Buscar en LinkedIn por keywords: "automatizacion IA", "inteligencia artificial LATAM", "n8n", "no-code", "transformacion digital". Filtrar por creadores con alto engagement.

**Accion con Tier 1:** Comentar 5x/semana en sus posts (parte del metodo 5-5-5). Comentarios de 2-3 oraciones con valor agregado, nunca "Buen post!".

#### Tier 2 — Peers / Cuentas del Mismo Nivel (15-25 cuentas)
**Que son:** Creadores con 1K-10K seguidores que estan construyendo audiencia en nichos cercanos (IA, tech, educacion online, emprendimiento digital LATAM).
**Por que importan:** Potencial de colaboracion, cross-promotion, y comunidad. Los peers se amplifican mutuamente.
**Criterios:**
- 1K-10K seguidores
- Publican al menos 1x/semana
- Nicho complementario (no competencia directa)
- Engagement real (no vanity followers)

**Accion con Tier 2:** Comentar 5x/semana (parte del metodo 5-5-5). Conectar si no estan conectados. Considerar para LinkedIn Lives o colaboraciones futuras.

#### Tier 3 — Avatar Target Directo (50-100+ cuentas)
**Que son:** Profesionales tecnicos en LATAM que SON el Sub-avatar 1: ingenieros, analistas, contadores, project managers con 6+ anos de experiencia, trabajando en empresas.
**Por que importan:** Son los potenciales alumnos/clientes. Comentar en SUS posts (si publican) o interactuar con sus comentarios en posts de Tier 1 crea visibilidad directa.
**Criterios:**
- Perfil tecnico: ingeniero, analista, contador, PM, data
- 6+ anos de experiencia profesional
- Trabaja en empresa mediana-grande en LATAM
- Activo en LinkedIn (publica o comenta al menos 1x/mes)

**Como construir esta lista:**
1. Revisar quienes comentan en posts de cuentas Tier 1 del nicho
2. Revisar profile views de Hans — quienes lo visitan
3. Revisar quienes comentan en posts de Hans
4. Buscar en LinkedIn por cargo + industria + region
5. Agregar personas que envian conexion a Hans

**Accion con Tier 3:** Comentar 5x/semana (parte del metodo 5-5-5). Cuando muestren senal de interes (ver `linkedin/signal-detector`), pasar a warm outreach.

### Reglas de Mantenimiento

1. **Revisar las listas cada 2-4 semanas** — quitar cuentas inactivas, agregar nuevas
2. **Mover entre tiers** si una cuenta crece o decrece
3. **No acumular cuentas muertas** — si alguien no publica en 30 dias, sacarlo de la lista activa
4. **Priorizar calidad sobre cantidad** — 10 cuentas Tier 1 activas > 50 cuentas random
5. **Documentar por que** una cuenta esta en cada tier — facilita la revision mensual

### Como Alimenta al Metodo 5-5-5

El metodo 5-5-5 (antes de cada post) se vuelve mas efectivo con las listas:

| 5 comentarios en... | Fuente |
|---------------------|--------|
| Cuentas Tier 1 | Lista definida — siempre hay posts nuevos de estas cuentas |
| Cuentas Tier 2 (peers) | Lista definida — apoya y recibe apoyo |
| Cuentas Tier 3 (avatar) | Lista definida — engagement directo con potenciales leads |

Sin las listas, el metodo 5-5-5 se convierte en "comentar en lo que aparece en el feed" — ineficiente y sin direccion.

### Criterios de Exclusion (NO agregar a las listas)

- Cuentas que solo venden (coaches de "hazte rico", MLM, crypto hype)
- Cuentas con engagement claramente falso (miles de likes, cero comentarios reales)
- Cuentas que no publican en espanol (a menos que su audiencia sea LATAM)
- Cuentas de la competencia directa (otros que ensenen exactamente lo mismo)

## Output (formato exacto)

El output de este skill es el documento `docs/linkedin-icp-tiers.md`:

```markdown
# LinkedIn ICP Tiers — Hans Villalobos
Ultima actualizacion: YYYY-MM-DD

## Tier 1 — Influencers del Nicho (10K+)
| # | Nombre | URL LinkedIn | Seguidores | Nicho | Frecuencia | Notas |
|---|--------|-------------|-----------|-------|-----------|-------|
| 1 | [nombre] | [url] | ~XK | [nicho] | X/sem | [nota] |

## Tier 2 — Peers (1K-10K)
| # | Nombre | URL LinkedIn | Seguidores | Nicho | Frecuencia | Notas |
|---|--------|-------------|-----------|-------|-----------|-------|
| 1 | [nombre] | [url] | ~XK | [nicho] | X/sem | [nota] |

## Tier 3 — Avatar Target Directo
| # | Nombre | URL LinkedIn | Cargo | Empresa | Experiencia | Senal |
|---|--------|-------------|-------|---------|------------|-------|
| 1 | [nombre] | [url] | [cargo] | [empresa] | X anos | [como lo encontramos] |

## Proxima Revision: YYYY-MM-DD
```

Guardar en: `docs/linkedin-icp-tiers.md`
