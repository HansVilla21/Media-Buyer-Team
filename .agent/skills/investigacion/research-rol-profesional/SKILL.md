---
name: research-rol-profesional
version: v1
description: Investiga exhaustivamente qué hace un rol profesional específico (media buyer, copywriter, estratega, etc.) usando Perplexity sonar-pro. Produce reporte estructurado con funciones, workflow, métricas, herramientas y gaps para diseño de sistemas de agentes.
---

# Research de Rol Profesional

## Cuándo usar este skill

- Se necesita entender en profundidad qué hace un profesional específico para replicar su función con agentes de IA
- Se va a rediseñar o crear un agente nuevo y se necesita una base factual sobre el rol real
- Hans pide investigar cómo funciona un tipo de experto o profesional de marketing/negocios
- Se quiere identificar qué decisiones, herramientas y procesos debe tener un agente para ser útil

## Cuándo NO usar este skill

- La pregunta es sobre tendencias de mercado o noticias de IA (usar research-tendencias en su lugar)
- El rol ya está documentado en `memory/` o en un reporte previo en `outputs/research/`
- Se busca información sobre una persona específica, no un rol genérico

## Inputs necesarios

- **Nombre del rol:** El puesto o función a investigar (ej: "media buyer", "copywriter de respuesta directa", "growth hacker")
- **Contexto del negocio:** Tipo de negocio donde aplica (ej: infoproductos, SaaS, e-commerce, LATAM)
- **Profundidad requerida:** Básica (overview) / Completa (exhaustiva, para diseño de agentes)
- **Uso del reporte:** ¿Para qué se va a usar? (diseño de agente, briefear a colaborador, entender el mercado)

## Workflow

1. Leer `memory/learnings.md` para verificar que este rol no fue investigado antes
2. Definir 6-8 queries de Perplexity cubriendo estos ángulos obligatorios:
   - Funciones y responsabilidades generales del rol
   - Rutina y workflow diario
   - Herramientas y stack tecnológico
   - Métricas y KPIs que monitorea
   - Decisiones que toma (estratégicas, tácticas, creativas)
   - Cómo trabaja con otros roles del equipo
   - Especificidades para el tipo de negocio del cliente
   - Diferencias con roles similares (para delimitar el scope)
3. Ejecutar búsquedas en paralelo (máximo 3 simultáneas para no sobrecargar)
4. Identificar qué queries dieron resultados pobres y relanzar con queries más específicas
5. Triangular información: si un dato importante aparece en solo 1 fuente, buscar confirmación
6. Redactar reporte completo en formato estándar (ver sección de Output)
7. Guardar en `outputs/research/YYYY-MM-DD_[rol]-profundo.md`
8. Identificar gaps: qué preguntas quedaron sin respuesta y por qué
9. Mapear implicaciones para el sistema de agentes de Hans
10. Actualizar `memory/learnings.md` con hallazgos clave

## Instrucciones

### Construcción de queries para este tipo de research

Los queries más efectivos para investigar un rol profesional combinan:
- El nombre del rol + plataforma específica + acción específica (no genérica)
- El año actual para forzar información reciente
- El contexto del negocio (infoproductos, LATAM, etc.)

**Ejemplos de queries efectivos:**
- "media buyer Meta Ads funciones diarias workflow optimizacion 2025 2026"
- "media buyer para infoproductos cursos online academias digitales funnel TOFU MOFU BOFU"
- "media buyer vs performance marketer vs growth marketer diferencias roles responsabilidades"
- "media buyer herramientas stack tecnologico analytics atribucion CRM 2025 2026"

**Queries que NO funcionan bien (demasiado genéricos):**
- "qué es un media buyer" (respuestas muy superficiales)
- "media buyer skills" sin contexto específico

### Ángulos obligatorios a cubrir en el research

Para cualquier rol profesional que se investigue para diseño de agentes, siempre incluir:

1. **Rutina y workflow:** ¿Qué hace hora a hora? ¿Cuánto tiempo dedica a qué?
2. **Decisiones:** ¿Qué tipo de decisiones toma? ¿Con qué frecuencia? ¿Basadas en qué información?
3. **Herramientas:** Stack tecnológico completo. Gratuitas vs. de pago. Críticas vs. complementarias.
4. **Métricas:** KPIs que monitorea. Señales de alerta. Benchmarks de referencia.
5. **Interacción con el equipo:** ¿A quién le pide qué? ¿Qué entrega a quién?
6. **Especificidades del negocio:** El mismo rol cambia mucho según industria. Forzar el contexto correcto.
7. **Tendencias 2025-2026:** Cómo está evolucionando el rol con IA y automatización.
8. **Diferencias con roles similares:** Para delimitar exactamente qué cubre este agente y qué no.

### Manejo de resultados pobres en Perplexity

Si un query devuelve "no hay resultados específicos" o información muy genérica:
- Reformular con términos más específicos (agregar plataforma, nicho, año)
- Dividir el query en 2 más específicos
- Cambiar el idioma: algunos términos técnicos tienen mejor cobertura en inglés
- Documentar en el reporte qué información no se encontró y por qué (transparencia sobre los gaps)

### Filtro de relevancia para el contexto de Hans

Antes de incluir información en el reporte, preguntar:
- ¿Es relevante para un negocio de infoproductos en LATAM con presupuesto de ads pequeño a mediano?
- ¿Es aplicable a Instagram + Meta Ads como canales principales?
- ¿El agente que se va a construir puede hacer esto realísticamente?

Descartar activamente:
- Información para empresas Fortune 500 con equipos grandes de 20+ personas
- Procesos que requieren software de $5,000+/mes
- Funciones que son claramente territorio de otro agente del sistema

### Sección de implicaciones para el sistema de agentes

Esta es la sección más valiosa del reporte para Hans. Siempre incluir:
- Qué funciones del rol puede replicar el sistema de agentes actual
- Qué gaps existen (técnicos o de información) que limitan al sistema
- Qué agente del equipo debe encargarse de cada función identificada
- Qué datos o inputs necesita el sistema para funcionar correctamente

## Output (formato exacto)

```markdown
# Reporte de Research: ¿Qué es un [ROL]? — Guía Exhaustiva
Fecha: YYYY-MM-DD
Pedido por: [quién lo solicitó]
Tipo: Research estructural / [propósito]
Búsquedas ejecutadas: N queries en Perplexity sonar-pro

---

## RESUMEN EJECUTIVO
[3-5 oraciones con los hallazgos más importantes. Lo que alguien que no tiene tiempo leería.]

---

## 1. DEFINICIÓN Y ROL CENTRAL
### ¿Qué hace un [rol]?
[Lista de responsabilidades principales]

### Diferencia con roles similares
[Tabla comparativa]

---

## 2. RUTINA DIARIA Y WORKFLOW
[Organizado por bloques de tiempo. Incluir lógica de decisiones.]

---

## 3. DECISIONES QUE TOMA
[Estratégicas / Tácticas / Creativas / Analíticas — separadas]

---

## 4. MÉTRICAS Y KPIs
[Tabla: métrica, definición, fórmula, benchmark referencial]
[Señales de alerta]

---

## 5. HERRAMIENTAS Y STACK TECNOLÓGICO
[Por categoría: ads, analytics, automatización, comunicación]

---

## 6. CÓMO TRABAJA CON OTROS ROLES
[Quién le da inputs, a quién le da outputs, cómo es el flujo]

---

## 7. ESPECIFICIDADES PARA [TIPO DE NEGOCIO]
[Todo lo que cambia cuando el contexto es infoproductos / LATAM / etc.]

---

## 8. TENDENCIAS 2025-2026
[Cómo está cambiando el rol con IA y automatización]

---

## 9. IMPLICACIONES PARA EL SISTEMA DE AGENTES DE HANS
[Mapa de funciones → agentes responsables]
[Gaps identificados en el sistema actual]

---

## Datos y Estadísticas Útiles
[Bullets con datos concretos y fuente]

---

## Fuentes
[URLs o nombres de publicaciones]

---

## Notas para el Agente que Usará Este Reporte
[Advertencias, contexto adicional, limitaciones de los datos]
```
