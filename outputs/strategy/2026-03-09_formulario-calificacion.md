# Formulario de Calificación — Preguntas para Agendamiento
Fecha: 2026-03-09
Basado en: Team Meeting 09/03 + Análisis de llamadas del closer
Para implementar en: el link de agendamiento que manda Brayan

---

## OBJETIVO

Filtrar leads ANTES de la llamada para que:
1. Solo lleguen a llamada personas que califican (tienen perfil + capital)
2. Los closers reciban leads más calientes y con contexto
3. Los no-calificados reciban un recurso gratuito en lugar de quedar en el vacío

---

## PREGUNTAS PROPUESTAS (ordenadas por importancia)

### Pregunta 1 — Filtro de perfil (la más importante)
**"¿A qué te dedicas actualmente?"**
- [ ] Trabajo en empresa (empleado/a)
- [ ] Tengo negocio propio
- [ ] Soy freelancer o consultor
- [ ] Estoy buscando empleo
- [ ] Estudiante

*Si responde "Estoy buscando empleo" → trigger del mensaje automático de no-calificado*

### Pregunta 2 — Área de trabajo (segmentación)
**"¿En qué área trabajas o te especializas?"**
- [ ] Ingeniería (industrial, sistemas, software, etc.)
- [ ] Contabilidad / Finanzas
- [ ] Logística / Operaciones / Supply Chain
- [ ] Salud (médico, enfermería, administración de clínicas)
- [ ] Ventas / Marketing
- [ ] Administración / Recursos Humanos
- [ ] Servicio al cliente / Turismo / Hotelería
- [ ] Otro: ___________

*Nota para closers: los perfiles de ingeniería, contabilidad y logística son los que más rápido cierran*

### Pregunta 3 — Ingresos (filtro de capacidad de pago)
**"¿Cuál es tu rango de ingresos mensuales aproximado?"**
- [ ] Menos de $500 USD/mes
- [ ] $500–$1,000 USD/mes
- [ ] $1,000–$2,000 USD/mes
- [ ] $2,000–$4,000 USD/mes
- [ ] Más de $4,000 USD/mes

*Si responde "Menos de $500 USD/mes" → trigger del mensaje de no-calificado*

### Pregunta 4 — Herramientas / experiencia (filtro de fit con el programa)
**"¿Has trabajado con alguna de estas herramientas o procesos?"**
- [ ] Excel avanzado (fórmulas, tablas dinámicas)
- [ ] Sistemas de gestión (ERP, CRM, Jira, Trello u otros)
- [ ] Automatizaciones básicas (Zapier, Make, similares)
- [ ] Programación (Python, JavaScript u otro)
- [ ] Ninguna de las anteriores

*Si responde "Ninguna" → no descalifica sola, pero combinada con otros factores sí*

### Pregunta 5 — Objetivo (intención de compra)
**"¿Qué quieres lograr con esto principalmente?"**
- [ ] Generar ingresos extra sin dejar mi trabajo actual
- [ ] Cambiar de carrera o empezar algo independiente
- [ ] Automatizar procesos en mi trabajo o negocio actual
- [ ] Aprender la habilidad para mejorar mi valor profesional
- [ ] Solo explorar / ver de qué trata

*Si responde "Solo explorar" → enviar a nurturing, no a llamada*

### Pregunta 6 — Disposición de inversión (cierre anticipado)
**"¿Estás en posición de invertir en tu desarrollo profesional en este momento?"**
- [ ] Sí, estoy listo/a para empezar
- [ ] Sí, pero necesito conocer los detalles y las opciones de pago
- [ ] En 1-3 meses probablemente sí
- [ ] No por ahora

*Si responde "No por ahora" → mensaje de no-calificado con recursos + nurturing*
*Si responde "Sí, estoy listo" → priorizar esa llamada*

### Pregunta 7 — Texto libre (oro para los closers)
**"¿Qué es lo que más te interesa aprender o resolver?"** (campo de texto libre)

*Esto le da contexto al closer para personalizar la llamada desde la apertura*

---

## LÓGICA DE CALIFICACIÓN

### ✅ LEAD CALIFICADO (procede a llamada)
- Tiene trabajo activo (no buscando empleo)
- Ingresos > $500/mes
- Al menos 1 herramienta/proceso en su background
- Disposición de inversión: sí o en 1-3 meses
- Objetivo concreto (no "solo explorar")

### ⚠️ LEAD TIBIO (nurturing, no llamada urgente)
- Tiene trabajo pero ingresos bajos ($500-$1,000)
- Sin background técnico pero con objetivo claro
- Disposición de inversión en 1-3 meses
- → Acción: mandar a ver más contenido de Hans + video de la página + reagendar en 4-6 semanas

### ❌ LEAD NO CALIFICADO (mensaje automático)
- Sin trabajo / buscando empleo
- Ingresos < $500/mes
- Sin disposición de inversión
- Solo quería información / explorar
- → Acción: mensaje automático de no-calificado (ver abajo)

---

## MENSAJE AUTOMÁTICO PARA LEADS NO CALIFICADOS

**Propuesta (en nombre de Hans):**

"Hola [nombre], muchas gracias por tu interés en Momentum AI Academy 🙌

Revisando tu perfil, creemos que en este momento quizás no es el mejor timing para entrar al programa — y preferimos ser honestos contigo antes de hacerte perder tiempo.

Pero eso puede cambiar. Aquí te dejamos recursos gratuitos para que sigas aprendiendo sobre automatización con IA mientras tanto:

📺 [Link canal YouTube de Hans]
🌐 [Link página web / video VSL]

Cuando tu situación cambie y quieras avanzar, las puertas están abiertas. ¡Mucho éxito!"

---

## POLÍTICA DE VIDEO PRE-LLAMADA

**Regla definida por Hans en la reunión:**
- Brayan debe confirmar que el lead VIO el video de la página web antes de la llamada
- Si no lo ha visto → reagendar, no celebrar la llamada
- Texto sugerido de Brayan: "Antes de tu llamada, es importante que veas este video de 7 minutos: [link]. Te va a dar mucha claridad de qué es exactamente lo que hacemos. Cuando lo hayas visto, confirma aquí y ya estás listo/a para la llamada 👍"

---

## NOTAS DE IMPLEMENTACIÓN

1. Brayan deja de agendar manualmente → manda el link del formulario
2. El formulario puede implementarse en Typeform, Google Forms o el sistema que ya usen
3. Las respuestas llegan antes de la llamada → closer lee el contexto → personaliza apertura
4. Los leads no calificados van al mensaje automático, no quedan en el vacío
5. Revisar el formulario y ajustar después de 2-3 semanas con data real
