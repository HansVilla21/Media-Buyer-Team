# Skill: Creative Brief para Ads

**Versión:** 1.0
**Creada:** 2026-03-09
**Usada por:** MEDIA BUYER (genera el brief), CREADOR (lo recibe y ejecuta)

---

## Para qué sirve esta skill

Un brief de creatividades es el documento que el MEDIA BUYER le pasa al CREADOR para producir un ad específico. Sin un brief claro, el CREADOR escribe contenido genérico. Con un brief, el CREADOR produce un creative con hipótesis testeable.

**Regla:** Cada brief = una hipótesis. Un brief no puede testear dos cosas a la vez.

---

## Cuándo usar esta skill

- Cuando el MEDIA BUYER necesita nuevos creativos para testear
- Cuando hay fatiga de creative (frecuencia > 3-4)
- Cuando los resultados de un creative agotado deben reemplazarse
- Cuando hay un nuevo ángulo de oferta que probar
- Cuando el INVESTIGADOR trajo insights de competidores que inspiran un nuevo hook

---

## Template del Brief

```markdown
# Brief de Creatividades: [Nombre del ángulo]
Fecha: YYYY-MM-DD
Creado por: MEDIA BUYER
Para: CREADOR
Prioridad: [Alta / Media]

---

## La hipótesis que estamos testeando
"Creemos que un hook de [tipo] va a resonar más con [sub-avatar] porque [razón basada en datos o insights]."

## Etapa del funnel
[ ] TOFU — Audiencia fría (no conoce a Hans)
[ ] MOFU — Audiencia tibia (vio contenido, no compró)
[ ] BOFU — Audiencia caliente (estuvo en la página de ventas)

## Sub-avatar específico
[Uno de los tres: Empleado Corporativo Atrapado / Emprendedor Digital Estancado / Freelancer Sin Techo]

Describe en 1-2 oraciones quién es exactamente esta persona en este momento de su vida:
[...]

## Hook (0-3 segundos) — SAGRADO, no cambiar sin avisar
[La frase exacta con la que debe abrir el video]
[Alternativa si el CREADOR quiere proponer variante: agregarla como "Hook variante" al final]

## Formato del ad
[ ] Video Reel vertical (9:16)
[ ] Carrusel
[ ] Imagen estática
Duración: [15s / 30s / 45s / 60s]

## Puntos clave del mensaje (en orden)
1. [Primer punto que debe comunicar]
2. [Segundo punto]
3. [Tercero si aplica]

*Nota: beneficios, no características. "Puedes ganar $1,500 extra" no "aprenderás n8n".*

## Elementos del avatar que DEBEN aparecer en el copy
- Dolor: "[la frase exacta que usaría el avatar para describir su problema]"
- Deseo: "[lo que quiere lograr en términos concretos]"
- Objeción a resolver: "[la excusa principal que tiene para no actuar]"

## CTA específico
[La acción exacta que debe hacer la persona al final: "Escribe ACADEMIA por DM" / "Haz clic para ver cómo" / etc.]

## Qué NO incluir en este ad
- [Elemento a evitar, ej: no mencionar precio]
- [Elemento a evitar, ej: no hablar de ChatGPT en este ad]

## KPI objetivo (¿cómo sabremos si funcionó?)
- KPI árbitro: [CTR / CPA / Conversiones]
- Umbral de éxito: [ej: CTR > 2% / CPA < $8 USD]

## Referencias de inspiración (opcional)
- [URL de un ad de competidor, descripción de un hook que viste, etc.]

---

## Notas adicionales del MEDIA BUYER
[Contexto extra, advertencias, o información relevante para el CREADOR]
```

---

## Proceso completo MEDIA BUYER → CREADOR

1. MEDIA BUYER identifica qué hipótesis quiere testear (basado en análisis de campañas o research de competidores)
2. MEDIA BUYER completa el brief con todos los campos
3. MEDIA BUYER guarda el brief en `outputs/ads/briefs/`
4. CREADOR lee el brief completo antes de escribir
5. CREADOR produce el script siguiendo el brief (hook es sagrado)
6. CREADOR guarda el script en `outputs/ads/scripts/`
7. MEDIA BUYER revisa el script antes de que Hans lo grabe
8. Hans graba → MEDIA BUYER lanza en Meta → registra resultados

---

## Tipos de hooks por etapa del funnel

### TOFU (frío) — hooks de interrupción y curiosidad
- Resultado numérico: "Gané $1,500 en 3 horas con esto"
- Dato disruptivo: "El 70% de los contadores van a perder su trabajo en 3 años"
- Pregunta de dolor: "¿Sigues trabajando 8 horas para el mismo sueldo?"
- Identidad: "Esto es para ti si tienes un trabajo fijo y sientes que el mercado te va a reemplazar"

### MOFU (tibio) — hooks de mecanismo y prueba
- Proceso: "Te muestro exactamente cómo mi alumno Carlos hizo $2,000 en su primer mes"
- Diferenciador: "Por qué nuestros alumnos no necesitan saber programar"
- Demostración: "En vivo: construyo una automatización que reemplaza 3 horas de trabajo"

### BOFU (caliente) — hooks de urgencia y decisión
- Urgencia real: "Quedan 5 lugares para el próximo cohort — cierra el [fecha]"
- Garantía prominente: "90 días para ver resultados o te devuelvo el dinero. Así de simple."
- Prueba social final: "127 alumnos ya generan ingresos extra con IA. El próximo puedes ser tú."
