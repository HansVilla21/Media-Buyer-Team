# Catalogo de Senales de Interes en LinkedIn

_Ultima actualizacion: 2026-03-30_
_Skill de referencia: `.agent/skills/linkedin/signal-detector/SKILL.md`_

---

## Que es una senal de interes

Una senal es cualquier accion que una persona hace en LinkedIn que indica algun nivel de interes en Hans, su contenido o su expertise. Las senales son la base del warm outreach — solo contactamos a personas que mostraron interes primero.

**Principio fundamental:** Nosotros NO hacemos cold outreach. Respondemos a senales.

---

## Catalogo de Senales

### Senales de Alta Fuerza (Score 4-5)

| Senal | Score | Que indica | Accion recomendada |
|-------|-------|-----------|-------------------|
| DM espontaneo preguntando algo | 5 | Interes directo, posible lead | Responder en <24h, abrir conversacion |
| Comentarios en 3+ posts | 5 | Seguidor comprometido | DM personalizado agradeciendo + pregunta genuina |
| Comentarios en 2 posts | 4 | Interes activo y recurrente | Responder con profundidad + visitar su perfil |
| Share/Repost de contenido | 4 | Advocacy: quiere que SU red vea esto | Agradecer publicamente + DM |
| Profile visit 2+ veces | 4 | Interes deliberado, esta evaluando | Conexion con nota o DM si ya conectados |
| Conexion con nota personalizada | 4 | Interes con esfuerzo | Mensaje de bienvenida personalizado |

### Senales de Media Fuerza (Score 2-3)

| Senal | Score | Que indica | Accion recomendada |
|-------|-------|-----------|-------------------|
| Comentario sustancioso (1 post) | 3 | Engagement real | Responder con profundidad |
| Save/Bookmark | 3 | Valor percibido alto | No accionable directamente, pero indica contenido util |
| Conexion sin nota | 2 | Interes basico | Visitar perfil, si es avatar match enviar bienvenida |
| Profile visit 1 vez | 2 | Curiosidad | Solo actuar si es avatar match claro |
| Like/Reaction | 1-2 | Engagement minimo | No actuar proactivamente |

### Senales de Contexto (no son acciones directas)

| Senal | Que indica | Como detectar |
|-------|-----------|---------------|
| Cambio de trabajo reciente | Persona en transicion, posible interes en habilidades nuevas | LinkedIn notifica cambios de trabajo de conexiones |
| Publica sobre frustacion con procesos manuales | Dolor activo del avatar | Monitorear posts de Tier 3 |
| Comenta en posts de competidores/peers | Interes en el nicho | Revisar comentarios en posts de Tier 1 y 2 |
| Cumple aniversario laboral (10+ anos) | Reflexion profesional, posible interes en cambio | LinkedIn notifica aniversarios |

---

## Filtro de Avatar Match

Antes de actuar sobre cualquier senal, verificar:

| Criterio | Sub-avatar 1 | Sub-avatar 2 |
|---------|-------------|-------------|
| Cargo | Ingeniero, analista, PM, contador, data | Empleado general, admin, soporte |
| Experiencia | 6+ anos | 2+ anos |
| Empresa | Mediana-grande, zona franca, multinacional | Cualquier empresa |
| Region | LATAM | LATAM |
| Plataforma preferida | LinkedIn (principal) | Instagram (principal) |

**Reglas:**
- 3 de 4 criterios = Avatar Match (actuar con prioridad)
- 2 de 4 = Avatar Parcial (actuar con menor prioridad)
- 0-1 = No Avatar (no invertir tiempo proactivo)

---

## Rutina Semanal de Signal Detection

**Cuando:** Lunes o viernes, 15 minutos
**Donde:** LinkedIn Analytics + notificaciones

1. Revisar "Quien vio tu perfil" — identificar avatar matches
2. Revisar comentarios de la semana — identificar recurrentes
3. Revisar nuevas conexiones — clasificar por avatar match
4. Revisar DMs — priorizar respuestas
5. Revisar si alguien compartio contenido — agradecer
6. Anotar todo en `outputs/linkedin/YYYY-MM-DD_signal-detection.md`

---

## Patrones a Detectar (despues de 3+ semanas)

- Que tipo de contenido genera mas profile views?
- De que industria vienen las senales mas fuertes?
- Que cargos aparecen mas?
- Hay personas que aparecen semana tras semana? (leads calientes)
- Las senales aumentan con ciertos tipos de post?
- Hay correlacion entre el metodo 5-5-5 y las senales recibidas?

---

## Conexion con Otros Skills

| Skill | Como se conecta |
|-------|----------------|
| `signal-detector` | Ejecuta esta rutina y produce el reporte |
| `warm-outreach` | Recibe las senales calificadas y genera DMs |
| `retro-analyst` | Trackea las metricas de senales semana a semana |
| `icp-mapper` | Define que cuentas son avatar match |
| `post-writer` | El contenido es el generador de senales |
