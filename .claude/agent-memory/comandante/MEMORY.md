# MEMORY — COMANDANTE

## Patron de trabajo de Hans
- Hans trabaja tarde en la noche (planificacion a las 11 PM) y ejecuta al dia siguiente
- Cuando dice "hoy" puede significar "mañana en la manana" — siempre verificar el contexto temporal antes de asumir fechas
- Ante urgencia maxima, Hans necesita un plan HORA POR HORA ultra concreto, no estrategia abstracta
- El plan debe ser tan claro que pueda abrirlo al despertar y ejecutar sin pensar

## Correccion de fechas — lecion aprendida (2026-03-24)
- Los agentes generaron todos los archivos con las fechas un dia corridas (miercoles 25, jueves 26) cuando el evento real era miercoles 26 y jueves 27
- El reel se graba el martes 25 (no el 24 que era la noche de planificacion)
- Cuando Hans da un contexto de "evento en X dias", verificar la fecha exacta antes de producir todos los archivos

## Estructura de archivos de evento urgente (patron confirmado)
Cuando hay un evento con 24-48h de ventana, los agentes producen estos archivos en este orden:
1. `outputs/research/` — investigacion + estrategia
2. `outputs/reels/` — guion del reel de lanzamiento
3. `outputs/stories/` — secuencias de stories por dia
4. `outputs/reels/` — mensajes de outreach a leads (se guarda en reels por ahora)
5. `outputs/ads/` — estrategia de paid media
6. `outputs/plan-ejecucion-[fecha].md` — plan hora por hora para Hans

## Preferencias de formato confirmadas
- Hans necesita outputs LISTOS PARA USAR — no borradores
- Los planes de ejecucion deben incluir: hora exacta, accion concreta, archivo de referencia
- Los mensajes de outreach deben incluir el texto listo para copiar-pegar con [nombre] como unico placeholder
- Las instrucciones de grabacion/edicion deben ser paso a paso, no genericas

## Stack tecnologico confirmado para webinars
- Plataforma: Google Meet (<100 personas) o Zoom (>100 personas)
- Registro: DM con palabra clave (ej: "CLAUDE") o Google Form simple
- Automatizacion de DMs: ManyChat (Hans ya sabe configurarlo)
- Edicion video: CapCut
