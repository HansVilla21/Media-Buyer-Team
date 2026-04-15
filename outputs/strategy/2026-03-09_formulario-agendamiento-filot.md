# Formulario de Agendamiento — Filot / Calendly
Fecha: 2026-03-09
Para: Link de agendamiento de Brayan (reemplaza el agendamiento manual)
Objetivo: Filtrar leads no calificados ANTES de la llamada + darle contexto al closer
Inspiración: Formato Rebeca Alvarado Tax Lawyer adaptado a Momentum AI Academy

---

## CONTEXTO DEL PROBLEMA

**Proceso actual (manual / con problemas):**
- Brayan recibe el DM → pregunta cuándo pueden hablar → agenda manualmente
- Resultado: llegan a llamada leads sin perfil técnico, sin capacidad de pago, o "solo curiosos"
- Closers pierden tiempo, se desmotivan, tasas de cierre bajas

**Proceso nuevo (con Filot):**
- Brayan recibe el DM → manda el link de Filot → lead llena el formulario
- El formulario filtra automáticamente → solo pasan a llamada los calificados
- Los no calificados reciben un mensaje automático con recursos gratuitos
- El closer entra a la llamada con el perfil del lead ya leído

---

## PREGUNTAS DEL FORMULARIO
(en el orden exacto que deben aparecer en Filot)

---

### BLOQUE 1 — Datos básicos (automático en Filot/Calendly)
- Nombre completo
- Email
- Número de WhatsApp (con indicativo de país)

---

### PREGUNTA 1 — Ocupación actual
**"¿Cuál es su ocupación actual?"**
*(Campo de texto libre — una línea)*

> Por qué texto libre: permite al closer leer exactamente cómo se describe el lead. "Ingeniero industrial en Intel" da mucho más contexto que marcar "Ingeniería".

---

### PREGUNTA 2 — Área de trabajo *(la más importante para filtrar)*
**"¿En qué área trabaja o se especializa?"**
*(Selección única)*

- Ingeniería (industrial, sistemas, software, electrónica, etc.)
- Contabilidad / Finanzas / Auditoría
- Logística / Operaciones / Supply Chain
- Tecnología / TI / Soporte técnico
- Administración / Recursos Humanos
- Ventas / Marketing
- Salud (médico, enfermería, administración de clínicas)
- Educación
- Servicio al cliente / Hotelería / Turismo
- Sin empleo actualmente
- Otro: ___________

**Lógica interna:**
- Ingeniería, Contabilidad, Logística, Tecnología → ✅ Calificado (perfil técnico confirmado)
- Administración, Ventas, Salud, Educación → ⚠️ Tibio (revisar con el resto de respuestas)
- Servicio al cliente, Hotelería, Turismo → ⚠️ Revisar capacidad de pago
- Sin empleo actualmente → ❌ No calificado (trigger de mensaje automático)

---

### PREGUNTA 3 — Herramientas que usa *(segundo filtro técnico)*
**"¿Con cuáles de estas herramientas trabaja actualmente?"**
*(Selección múltiple — puede marcar varias)*

- Excel avanzado (tablas dinámicas, fórmulas complejas)
- Sistemas de gestión (ERP, CRM, SAP, Jira, Trello u otros)
- Bases de datos (SQL, Access u otros)
- Automatizaciones básicas (Zapier, Make, Power Automate)
- Programación (Python, JavaScript, otro lenguaje)
- Ninguna de las anteriores

**Lógica interna:**
- 2 o más herramientas marcadas → ✅ Perfil técnico confirmado
- 1 herramienta marcada → ⚠️ Evaluar con otras respuestas
- "Ninguna" marcada → ⚠️ No descalifica solo, pero combinado con área no técnica → ❌

> Nota para el closer: esta pregunta es oro. Si alguien marca "SAP + Python + automatizaciones" ya llegó caliente. Si marca solo "ninguna", la llamada necesita más educación.

---

### PREGUNTA 4 — Qué busca lograr *(intención de compra)*
**"¿Qué quiere lograr principalmente?"**
*(Selección única)*

- Generar ingresos extra sin dejar mi trabajo actual
- Crear un negocio propio de automatizaciones con IA
- Automatizar procesos en mi trabajo o empresa actual
- Mejorar mi valor profesional y conseguir mejores oportunidades
- Aprender sobre IA y automatización (explorar el tema)

**Lógica interna:**
- Las 4 primeras opciones → ✅ Intención de compra clara
- "Aprender / explorar el tema" → ⚠️ Nurturing, no llamada urgente

---

### PREGUNTA 5 — Ingresos mensuales *(capacidad de pago)*
**"¿Cuál es su rango de ingresos mensuales aproximado?"**
*(Selección única)*

- Menos de $500 USD/mes (o menos de ₡250,000)
- Entre $500 y $1,000 USD/mes
- Entre $1,000 y $2,500 USD/mes
- Entre $2,500 y $5,000 USD/mes
- Más de $5,000 USD/mes
- Prefiero no indicarlo

**Lógica interna:**
- Menos de $500/mes → ❌ No calificado (sin capacidad de inversión)
- $500-$1,000/mes → ⚠️ Tibio — el financiamiento de $100/mes puede funcionar, pero ajustado
- $1,000/mes+ → ✅ Calificado

> Para el closer: si dice $500-$1,000, abrir con el argumento de financiamiento desde el inicio. Si dice $2,500+, abrir con el ROI directo del primer proyecto.

---

### PREGUNTA 6 — Disponibilidad de inversión *(cierre anticipado)*
**"¿Está en posición de invertir en su desarrollo profesional en este momento?"**
*(Selección única)*

- Sí, estoy listo/a para tomar una decisión hoy si el programa es lo que busco
- Sí, pero quiero conocer primero las opciones de pago disponibles
- Posiblemente en 1 a 3 meses
- No por ahora

**Lógica interna:**
- "Listo hoy" → ✅ Priorizar esta llamada — llega caliente
- "Opciones de pago" → ✅ Calificado — abrir con financiamiento $100/mes
- "En 1-3 meses" → ⚠️ Tibio — agendar pero no priorizar
- "No por ahora" → ❌ No calificado — mensaje automático

---

### PREGUNTA 7 — Acuerdo de condiciones *(reducir no-shows)*
**"Para garantizar la mejor experiencia en la llamada, por favor confirme lo siguiente:"**
*(Checkboxes — todos obligatorios)*

- [ ] Voy a tomar la llamada desde un lugar tranquilo y con buena conexión, preferiblemente desde una computadora
- [ ] Entiendo que si no confirmo mi asistencia por WhatsApp el día antes, la llamada puede ser reagendada
- [ ] **Voy a ver el video de presentación antes de la llamada** *(link del VSL aquí)* — esto es obligatorio para aprovechar mejor el tiempo

> Esta última es clave. Si el lead no marca que va a ver el video, Brayan debe confirmar el día antes que lo vio. Si no lo vio → reagendar.

---

### PREGUNTA 8 — Texto libre para el closer *(contexto de oro)*
**"¿Qué le gustaría lograr con esto? ¿Qué cambiaría en su vida si generara $1,500–$2,000 USD extra al mes?"**
*(Campo de texto libre — párrafo)*

> Esta es la pregunta más valiosa para el closer. El avatar principal no quiere automatizar su trabajo — quiere libertad, ingresos extra, independencia, quizás dejar su empleo. El que escribe "quiero tener más tiempo con mi familia y no depender de un jefe" o "quiero pagar mis deudas y ahorrar" llega con motivación emocional real. El closer abre la llamada conectando con ESA respuesta, no con una herramienta técnica.

---

### PREGUNTA 9 — Redes sociales *(opcional pero útil)*
**"¿En qué redes sociales podemos ubicarle?"**
*(Campo de texto libre — una línea)*

Ejemplo: @usuario en Instagram, LinkedIn: nombre completo

> Permite al closer revisar el perfil del lead antes de la llamada y personalizar aún más la apertura.

---

## LÓGICA DE CALIFICACIÓN (resumen para Brayan)

### ✅ LEAD CALIFICADO → procede a llamada
Cumple TODO lo siguiente:
- Tiene trabajo activo (no "sin empleo")
- Área técnica o semi-técnica (ingeniería, contabilidad, logística, TI)
- Ingresos > $500/mes
- Disponibilidad de inversión: "listo hoy" o "quiero conocer opciones de pago"
- Objetivo concreto (no "solo explorar")

**Acción de Brayan:** confirmar la llamada + recordar que deben ver el video antes

---

### ⚠️ LEAD TIBIO → nurturing, no llamada urgente
- Tiene trabajo pero área no técnica o ingresos $500-$1,000
- Disponibilidad "en 1-3 meses"
- Solo quiere explorar

**Acción de Brayan:** mandar recursos gratuitos (YouTube de Hans + VSL) + reagendar en 3-4 semanas

---

### ❌ LEAD NO CALIFICADO → mensaje automático, no llamada
- Sin empleo actualmente
- Ingresos < $500/mes
- "No por ahora" en disponibilidad de inversión

**Acción:** mensaje automático (no consume tiempo de Brayan ni de closers)

---

## MENSAJE AUTOMÁTICO PARA LEADS NO CALIFICADOS

*(En nombre de Hans, enviado automáticamente por Filot o por Brayan con una plantilla)*

---

"Hola [nombre], muchas gracias por su interés en Momentum AI Academy 🙌

Revisamos su perfil y creemos que en este momento quizás no es el mejor timing para entrar al programa — y preferimos ser honestos antes de hacerle perder su tiempo.

Pero eso puede cambiar. Le dejamos estos recursos gratuitos para que siga aprendiendo sobre automatización con IA mientras tanto:

📺 Canal de YouTube: [link]
🎥 Video de presentación: [link VSL]

Cuando su situación cambie y quiera avanzar, aquí estaremos. ¡Mucho éxito!"

---

## MENSAJE DE BRAYAN PARA MANDAR EL LINK

*(Plantilla de WhatsApp para cuando llegue un lead por DM)*

---

"Hola [nombre] 👋 Gracias por escribir.

Para coordinar su llamada con nuestro equipo, le pido que complete este formulario de 2 minutos — así aprovechamos mejor el tiempo juntos:

🔗 [Link de Filot]

Una vez que lo complete, queda agendado automáticamente. Cualquier consulta, aquí estoy 😊"

---

## NOTAS DE IMPLEMENTACIÓN EN FILOT

1. Las preguntas 1-9 van dentro del flujo de agendamiento (antes de que el lead elija fecha/hora)
2. La lógica de calificación puede implementarse con "conditional logic" en Filot si lo soporta, o bien Brayan revisa las respuestas manualmente antes de confirmar la llamada
3. Las respuestas del formulario deben llegar al closer antes de la llamada — verificar que Filot manda un resumen por email o WhatsApp
4. Revisar las preguntas y ajustar después de 2-3 semanas con data real

---

*Generado por: COMANDANTE — Media Buyer Team*
*Basado en: reunión 09/03 + análisis de llamadas + referencia visual de formulario Calendly*
*Archivo: outputs/strategy/2026-03-09_formulario-agendamiento-filot.md*
