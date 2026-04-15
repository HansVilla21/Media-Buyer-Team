---
name: linkedin-warm-outreach
version: v1
description: Templates y protocolo para enviar DMs personalizados en LinkedIn SOLO a personas que mostraron interes activo. No cold outreach. Maximo 10-15 DMs por semana, todos manuales y humanos.
---

# LinkedIn Warm Outreach

## Cuando usar este skill

- Cuando el `signal-detector` identifica personas con score 3+ de interes
- Cuando alguien comenta en 2+ posts de Hans
- Cuando alguien visita el perfil de Hans 2+ veces
- Cuando alguien envia conexion con nota personalizada
- Cuando Hans quiere iniciar conversacion con alguien que mostro interes
- Para enviar mensajes de bienvenida a nuevas conexiones del avatar target

## Cuando NO usar este skill

- Para contactar personas que NO mostraron ninguna senal de interes (eso es cold outreach)
- Para enviar mensajes masivos o automatizados (NUNCA)
- Para vender directamente en el primer mensaje (NUNCA)
- Para crear contenido de posts (usar `linkedin/post-writer`)
- Para comentar en posts de otros (usar `linkedin/comment-engine`)

## Inputs necesarios

- **Reporte de senales**: output del `linkedin/signal-detector`
- **Perfil de la persona**: cargo, empresa, contenido que publican, que comentaron
- **Contexto del interes**: que senal genero (comentario, profile view, share, etc.)
- **Avatar**: `memory/avatar.md`
- **Voz de marca**: `memory/brand-voice.md`

## Workflow

1. **Recibir senal calificada** del signal-detector (score 3+)
2. **Investigar a la persona** — ver su perfil, que publican, donde trabajan, que comentaron
3. **Seleccionar template** apropiado segun el tipo de senal
4. **Personalizar** el mensaje con detalles reales de la persona (NO generico)
5. **Revisar** que suene a Hans, no a robot ni a vendedor
6. **Enviar** manualmente desde LinkedIn
7. **Registrar** en el tracking semanal

## Instrucciones

### Principios Fundamentales

1. **Solo warm, nunca cold.** Cada persona que contactamos mostro interes primero. Nosotros respondemos, no iniciamos de la nada.
2. **Humano, no template.** Aunque usamos templates como base, cada mensaje debe tener al menos 1 elemento especifico de la persona (su cargo, algo que publico, algo que comento).
3. **Valor primero, venta nunca en primer contacto.** El objetivo del primer DM es iniciar conversacion, no vender la academia.
4. **Maximo 10-15 DMs/semana.** Calidad absoluta. Un DM excelente > 50 DMs genericos.
5. **Tono Hans.** Directo, profesional pero humano, sin formalismo excesivo, sin emojis abundantes.

### Templates por Tipo de Senal

#### Template 1 — Comentarista Recurrente
**Cuando:** Alguien comento en 2+ posts de Hans
**Objetivo:** Agradecer + abrir conversacion genuina

```
Hola [nombre],

He notado que comentas seguido en mis posts y queria agradecerte — tus aportes suman.

Vi que trabajas en [empresa/industria]. Me da curiosidad: ya estan usando alguna automatizacion con IA ahi, o es algo que estan explorando?

[Hans]
```

**Variante si la persona comento algo especifico:**
```
Hola [nombre],

Tu comentario en mi post sobre [tema] me hizo pensar. Cuando dijiste "[frase textual de su comentario]" — es exactamente lo que veo en muchas empresas de [industria].

Estas usando alguna herramienta para resolver eso o lo siguen haciendo manual?

[Hans]
```

#### Template 2 — Profile Visitor Repetido
**Cuando:** Alguien visito el perfil 2+ veces y es avatar match
**Objetivo:** Conectar + abrir puerta

```
Hola [nombre],

Vi que pasaste por mi perfil — me dio curiosidad tu rol en [empresa]. [Detalle especifico de algo que viste en su perfil, por ejemplo: "llevas 8 anos en logistica, que es exactamente donde mas impacto tienen las automatizaciones"].

Si en algun momento quieres explorar como la IA puede simplificar [proceso especifico de su industria], con gusto platicamos.

[Hans]
```

#### Template 3 — Nueva Conexion del Avatar
**Cuando:** Alguien del avatar target envio conexion (o acepto la tuya)
**Objetivo:** Bienvenida + valor inmediato

```
Hola [nombre], gracias por conectar.

Vi que eres [cargo] en [empresa]. Justo publico contenido sobre como profesionales tecnicos en LATAM estan usando herramientas de IA para automatizar procesos sin programar.

Si hay algun tema especifico que te interese (reportes, flujos de aprobacion, integraciones), me cuentas y lo cubro en un post.

[Hans]
```

#### Template 4 — Quien Compartio Contenido
**Cuando:** Alguien hizo repost de un post de Hans
**Objetivo:** Agradecer + fortalecer la relacion

```
Hola [nombre],

Vi que compartiste mi post sobre [tema] — gracias, de verdad. Que tu audiencia en [industria] lo vea me ayuda mucho a entender que angulos resuenan.

Que parte del post te parecio mas util? Me sirve para crear mas de eso.

[Hans]
```

#### Template 5 — DM Espontaneo (Respuesta)
**Cuando:** Alguien envio un DM preguntando algo
**Objetivo:** Responder con valor + abrir relacion

```
Hola [nombre],

Buena pregunta sobre [tema]. [Respuesta directa y util en 2-3 oraciones].

Si quieres profundizar en eso, [oferta de valor: "tengo un post donde lo explico paso a paso" / "la proxima semana voy a publicar un carrusel sobre exactamente eso" / "con gusto lo platicamos en una llamada de 15 min"].

[Hans]
```

### Lo Que NUNCA Hacer en un DM

1. **No vender la academia en el primer mensaje.** Si la conversacion evoluciona y la persona pregunta, ahi si. Pero no antes.
2. **No usar copy de ventas.** Nada de "te gustaria descubrir como ganar $5,000/mes?" Eso es spam.
3. **No enviar links en el primer mensaje.** LinkedIn penaliza mensajes con links. Y se ve como spam.
4. **No enviar el mismo mensaje a multiples personas.** Cada DM debe tener al menos 1 elemento unico.
5. **No enviar mensajes de voz no solicitados.** Algunos los ven como invasivos.
6. **No hacer follow-up agresivo.** Si no responden, dejar pasar. Pueden volver luego a traves del contenido.

### Flujo de Conversacion Post-DM

Si la persona responde:
1. **Mantener conversacion genuina** — preguntar, escuchar, aportar valor
2. **Detectar si hay dolor/necesidad real** — sin forzar
3. **Si hay match natural:** ofrecer una llamada de 15 min para explorar como la IA puede ayudarle
4. **Si no hay match ahora:** mantener la relacion, seguir aportando valor con contenido
5. **Nunca forzar la transicion a venta**

### Tracking

Llevar registro simple en `outputs/linkedin/YYYY-MM-DD_warm-outreach-log.md`:

| Fecha | Persona | Senal que genero el DM | Template usado | Respuesta? | Siguiente paso |
|-------|---------|----------------------|----------------|-----------|----------------|

## Output (formato exacto)

Cuando Hans pide generar DMs, el output es:

```markdown
# Warm Outreach — YYYY-MM-DD

## DMs Generados (listos para enviar)

### DM 1: [Nombre de la persona]
- **Senal:** [que genero el contacto]
- **Perfil:** [cargo, empresa, experiencia]
- **Template base:** [cual se uso]
- **Mensaje personalizado:**

[Texto del DM listo para copiar/pegar]

- **Nota:** [cualquier contexto adicional para Hans]

[repetir para cada DM]

## Checklist Pre-Envio
- [ ] Cada DM tiene al menos 1 elemento personalizado real
- [ ] Ningun DM vende directamente
- [ ] Ningun DM tiene links
- [ ] Suena a Hans, no a robot
- [ ] Total de DMs esta semana <= 15
```

Guardar en: `outputs/linkedin/YYYY-MM-DD_warm-outreach.md`
