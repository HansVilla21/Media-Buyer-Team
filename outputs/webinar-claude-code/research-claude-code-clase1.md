# Research Completo: Claude Code — Clase Introductoria
Fecha: 2026-03-25
Preparado por: INVESTIGADOR — Momentum AI Academy
Para: Hans Villalobos — Clase en vivo hoy 7pm
Tipo: Research para contenido de clase + preparación pedagógica

---

## NOTA RÁPIDA PARA HANS

Este reporte está escrito en lenguaje simple, como si lo explicaras a alguien que nunca ha tocado código en su vida. Cada sección está pensada para que la puedas usar directamente como guion mental o referencia durante la clase. Los bloques de código que aparecen son exactamente lo que debes mostrar en pantalla.

---

## SECCIÓN 1 — QUÉ ES CLAUDE CODE (Y QUÉ LO HACE DIFERENTE)

### La explicación de 30 segundos (úsala para abrir la clase)

"El Claude que todos conocen — el de claude.ai, donde le hacemos preguntas — es como un asistente que te da respuestas. Muy útil. Pero Claude Code es algo completamente diferente: es como contratar a un programador experto que trabaja dentro de tu computador, en tiempo real. No te dice qué hacer. Él lo hace."

Esa es la diferencia central:
- **Claude web (claude.ai):** Te responde preguntas. Te explica. Te ayuda a pensar.
- **Claude Code:** Se instala en tu computador. Abre tus archivos. Los crea. Los modifica. Ejecuta tareas reales.

### La analogía que funciona con audiencias no técnicas

Imagina que tienes un asistente muy inteligente. El Claude normal es ese asistente sentado en otra oficina al que le llamas por teléfono y le preguntas cosas. Claude Code es ese mismo asistente, pero sentado a tu lado, con acceso a tu escritorio, a tus carpetas, a tu computador. Le dices "necesito un reporte de todas las clínicas de la ciudad con su teléfono" y él lo busca, lo organiza y te entrega el archivo terminado.

### Tabla de diferencias (muéstrala en pantalla)

| Característica | Claude web (claude.ai) | Claude Code |
|----------------|------------------------|-------------|
| Propósito | Conversación, preguntas, ideas | Crear y ejecutar tareas reales |
| Acceso a tu computador | Ninguno | Lee, crea y modifica archivos |
| Ejecuta código | No — solo lo sugiere | Sí — lo ejecuta de verdad |
| Dónde funciona | En el navegador | En la terminal de tu computador |
| Para qué sirve mejor | Preguntas, redacción, análisis | Automatización, scripts, herramientas |

### Por qué es tan relevante AHORA (marzo 2026)

Hay tres razones por las que este es el momento:

**1. El movimiento "vibe coding" se volvió viral**
"Vibe coding" significa crear apps, automatizaciones y herramientas completas usando solo lenguaje normal — sin escribir una sola línea de código tú mismo. Claude Code es la herramienta líder de este movimiento. Y Combinator (la aceleradora más famosa del mundo) reporta que startups están lanzando productos completos en un fin de semana usando exactamente este enfoque.

**2. Está disponible para cualquier persona con Claude Pro ($20/mes)**
Antes, este tipo de herramientas eran solo para developers con experiencia. Hoy cualquier persona con una suscripción de $20/mes puede instalar Claude Code en menos de 5 minutos y empezar a usarlo.

**3. Los resultados documentados son reales**
Thoughtworks — una de las consultoras de tecnología más respetadas del mundo — documentó un aumento del 200% en productividad de ingenieros usando Claude Code. Dos veces más trabajo, en el mismo tiempo.

**Dato de contexto para la clase:** El 84% de desarrolladores ya usa o planea usar herramientas de IA en su flujo de trabajo (Stack Overflow Developer Survey 2026). La transición pasó de "experimento" a "estándar de la industria".

---

## SECCIÓN 2 — CÓMO INSTALARLO (PASO A PASO, SÚPER SIMPLE)

### Lo que el estudiante necesita ANTES de instalar

1. **Una suscripción a Claude Pro** — cuesta $20/mes en claude.ai. Sin esto, no funciona. El plan gratuito no incluye Claude Code.
2. **Un computador con acceso a internet** — Windows, Mac o Linux, cualquiera funciona.
3. **Una terminal abierta** — explicación abajo.

### Qué es una terminal (explícalo así para no técnicos)

"La terminal es esa pantalla negra con texto blanco que ves en las películas cuando los hackers 'hackean' algo. La buena noticia: no necesitas saber nada de hackeo. Solo necesitas saber abrirla y escribir un comando."

**Cómo abrirla:**
- **Windows:** Buscar "PowerShell" en el menú de inicio y abrirlo
- **Mac:** Buscar "Terminal" en Spotlight (Cmd + Espacio, escribir Terminal)
- **Linux:** Ctrl + Alt + T

### Instalación (el método más simple en 2026)

**Para Mac y Linux** — copiar y pegar este comando en la terminal:
```
curl -fsSL https://claude.ai/install.sh | bash
```

**Para Windows** — en PowerShell, copiar y pegar:
```
irm https://claude.ai/install.ps1 | iex
```

Eso es todo. El instalador hace todo el trabajo solo.

**Verificar que quedó instalado correctamente:**
```
claude --version
```
Si aparece un número de versión, está instalado correctamente.

### Primer inicio de sesión (solo la primera vez)

Después de instalar, escribir:
```
claude auth login
```
Esto abre el navegador para iniciar sesión con la cuenta de Claude. Solo se hace una vez.

### Tiempo total de instalación: menos de 5 minutos

Este es un punto importante para decirles a los estudiantes: no hay excusa de "es muy difícil de instalar". Son dos comandos y un inicio de sesión.

### Errores comunes y cómo resolverlos

| Error frecuente | Qué significa | Solución simple |
|-----------------|---------------|-----------------|
| "command not found" | El computador no reconoce el comando | Cerrar y abrir la terminal de nuevo. Si persiste, reiniciar el computador. |
| "permission denied" | El computador pide permisos | En Mac/Linux: agregar `sudo` antes del comando. En Windows: abrir PowerShell como administrador |
| "login failed" | Problema con la cuenta | Verificar que la suscripción Claude Pro esté activa en claude.ai |
| La terminal no responde | El comando está corriendo | Esperar 30 segundos. Si sigue sin responder, presionar Ctrl+C y volver a intentar |
| "Node.js not found" (solo si aparece) | Versión antigua del instalador | Descargar Node.js gratis en nodejs.org, instalar, y volver a intentar |

**Nota para la clase:** Si alguien tiene problemas de instalación, el 90% de los casos se resuelve reiniciando la terminal o el computador. El otro 10% se resuelve en la comunidad.

---

## SECCIÓN 3 — CÓMO SE USA (LO MÁS BÁSICO)

### Cómo iniciar una sesión de trabajo

1. Abrir la terminal
2. Navegar a la carpeta donde quieres trabajar (o simplemente estar en el escritorio)
3. Escribir:
```
claude
```
Así de simple. Claude Code abre y está listo para recibir instrucciones.

### Cómo darle instrucciones (el principio más importante)

"Habla con Claude Code como si le estuvieras explicando algo a un asistente humano muy inteligente. No uses lenguaje técnico. Describe el RESULTADO que quieres, no los pasos técnicos."

**Ejemplos de instrucciones que cualquiera puede usar en su primera sesión:**

| En lugar de esto (técnico) | Di esto (natural) |
|----------------------------|-------------------|
| "Write a Python script to scrape" | "Necesito un programa que busque en Google Maps todos los restaurantes de mi ciudad y guarde sus nombres y teléfonos en un archivo Excel" |
| "Create a bash script" | "Quiero que cada vez que llegue un correo con la palabra 'factura', se copie automáticamente a una carpeta específica" |
| "Build a webhook integration" | "Cuando alguien llene el formulario de mi sitio web, que automáticamente se agregue al Excel de clientes y me llegue una notificación de WhatsApp" |

### Comandos básicos que necesitas conocer

Dentro de Claude Code, hay algunos comandos especiales que empiezan con `/`:

| Comando | Para qué sirve | Cuándo usarlo |
|---------|----------------|----------------|
| `/help` | Ver lista de todos los comandos disponibles | Cuando estás perdido |
| `/clear` | Borrar la conversación y empezar de cero | Cuando quieres cambiar de tema completamente |
| `Shift + Tab` | Activar el "Modo Plan" | Cuando la tarea es grande y quieres que Claude piense antes de hacer |
| `Ctrl + C` | Detener lo que está haciendo | Cuando algo salió mal o quieres interrumpir |

### El Modo Plan (explícalo así)

"El Modo Plan es cuando le dices a Claude: no hagas nada todavía. Primero explícame cómo lo vas a hacer y espera mi aprobación."

Es como si contrataras a un plomero y antes de que rompa paredes, te mostrara el plano de lo que va a hacer y esperara que tú digas "sí, adelante."

Para activarlo: presionar `Shift + Tab` antes de empezar.

### Qué puede hacer Claude Code que el Claude normal NO puede

Esto es lo que hace la diferencia real para el avatar de Hans:

1. **Crear archivos reales en tu computador** — no solo escribir texto, sino guardar archivos .xlsx, .pdf, .csv que puedes abrir inmediatamente
2. **Conectarse con APIs de otros servicios** — WhatsApp, Gmail, Google Sheets, sin que tú sepas programar
3. **Ejecutar tareas automáticas** — "revisa esta carpeta cada hora y si hay archivos nuevos, procésalos y envíalos por email"
4. **Leer y analizar tus archivos** — le puedes pasar un Excel con 10,000 filas y te dice qué tiene, qué le falta, o lo procesa según tus instrucciones
5. **Construir herramientas completas** — apps, dashboards, bots — todo con instrucciones en lenguaje normal

---

## SECCIÓN 4 — CASOS DE USO PRÁCTICOS Y ACCESIBLES

### Para uso personal (día a día)

Estos son ejemplos de cosas que cualquier persona puede pedirle en su primera semana:

**1. Organizador de archivos automático**
"Tengo la carpeta de Descargas llena de archivos sin orden. Crea un script que organice todo por tipo de archivo: fotos en una carpeta, PDFs en otra, videos en otra. Que se ejecute automáticamente cada semana."

**2. Resumen diario de correos**
"Todas las mañanas a las 8am, revisa mis correos del día anterior, identifica los más importantes y mándame un resumen por WhatsApp."

**3. Backup automático**
"Cada noche a las 11pm, copia automáticamente mis archivos de trabajo a esta carpeta de respaldo."

**4. Convertidor de formatos**
"Tengo 50 archivos Word de contratos. Conviértelos todos a PDF y guárdalos en una nueva carpeta."

**5. Renombrador masivo de fotos**
"Tengo 200 fotos de un evento que se llaman IMG_001, IMG_002, etc. Renómbralas como 'Boda_Maria_Juan_001', 'Boda_Maria_Juan_002', etc."

### Para generar ingresos (servicios a clientes)

Estos son los servicios que ya están siendo vendidos en el mercado hispanohablante:

**1. Sistema de prospección de negocios — precio referencia: $600-800 USD**
Pedirle a Claude Code: "Crea un programa que busque todas las clínicas dentales de [ciudad], con su nombre, teléfono, dirección y correo si está disponible. Guárdalo en un Excel listo para usar."

Un vendedor de servicios puede usar esto para conseguir 50-100 prospectos calificados en minutos. Eso es valor concreto y cobrable.

**2. Automatización de reportes para empresas — precio referencia: $800-1,200 USD**
Pedirle: "Mi cliente tiene este Excel con ventas del mes. Cada lunes necesita un reporte automático que sume por vendedor, calcule las comisiones y genere un PDF listo para presentar."

Este servicio puede cobrarse como setup único o como retainer mensual.

**3. Bot de respuestas para WhatsApp Business — precio referencia: $1,200-1,500 USD**
Claude Code puede crear el script que se conecta con la API de WhatsApp Business y responde preguntas frecuentes automáticamente, clasifica leads y agenda citas.

**4. Herramienta interna de empresa — precio referencia: $1,500-2,000 USD**
"Mi cliente necesita un sistema donde sus vendedores puedan registrar visitas a clientes, y que genere automáticamente el reporte mensual para la gerencia."

**5. Analizador de datos de ventas — precio referencia: $500-800 USD**
"Tengo los datos de ventas de los últimos 6 meses de un restaurante. Analiza qué días venden más, qué platillos son más rentables y genera 5 recomendaciones para mejorar."

### La primera automatización que cualquiera puede construir en una semana

**El scraper de prospectos** es el punto de entrada perfecto porque:
- El resultado es inmediato y visible (un Excel con contactos reales)
- No requiere conectarse a ningún servicio externo
- Se puede vender de inmediato a cualquier negocio que necesite prospectos
- El proceso de aprender a pedírselo a Claude Code es un buen entrenamiento para proyectos más complejos

---

## SECCIÓN 5 — INTEGRACIÓN CON OTRAS HERRAMIENTAS

### Cómo explicarle las APIs a alguien que nunca las ha usado

"Una API es como la ventanilla de un banco. El banco tiene todo el dinero adentro, pero tú no puedes entrar al vault. La ventanilla es la forma oficial y segura de acceder. Las APIs son las ventanillas de los servicios de internet — la forma oficial de que dos programas se hablen entre sí."

Cuando Claude Code se conecta con WhatsApp, con Gmail, con Google Sheets — lo hace a través de sus APIs. Tú no necesitas saber cómo funciona la API. Solo le dices a Claude Code qué quieres conectar y él se encarga del resto.

### Integración con n8n (el stack principal de Hans)

n8n y Claude Code son un combo poderoso. Así se usan juntos:

**Rol de n8n:** Conecta servicios y crea flujos visuales. Cuando pasa A, hace B. Muy visual, muy flexible.

**Rol de Claude Code:** Crea los scripts, herramientas y lógica que necesitas para que n8n haga cosas más complejas.

**Ejemplo del combo:**
- n8n detecta cuando llega un email con una factura adjunta
- Claude Code (a través de un script) lee el PDF de la factura, extrae los datos y los formatea
- n8n toma esos datos y los guarda en Google Sheets y notifica por Slack
- Tú no tocas nada — todo pasa automático

**Cómo conectarlos técnicamente (para mostrar en pantalla, sin que tengas que explicar el código):**
En n8n, existe un nodo llamado "HTTP Request" que puede llamar a la API de Anthropic (la misma que usa Claude Code). Eso significa que puedes hacer que un flujo de n8n le haga preguntas a Claude y use sus respuestas para decidir qué hacer después.

### Otras herramientas que se integran bien

| Herramienta | Para qué conectarla con Claude Code |
|-------------|-------------------------------------|
| Google Sheets | Leer y escribir datos, generar reportes automáticos |
| Gmail / Outlook | Clasificar correos, responder automáticamente, extraer información |
| WhatsApp Business (API) | Bots de respuesta, notificaciones automáticas, clasificación de leads |
| Airtable | Base de datos de clientes, actualización automática |
| Slack / Discord | Notificaciones internas, bots de equipo |
| Notion | Actualizaciones automáticas de wikis y documentos |
| Make (Integromat) | Mismo principio que n8n — flujos visuales con Claude como cerebro |
| Excel (Microsoft) | Hay un complemento oficial de Anthropic para Excel — se instala desde Microsoft AppSource |

### La lógica que hay que enseñar (el insight más valioso de esta sección)

"Claude Code no reemplaza a n8n ni a Make. Los hace más poderosos. n8n conecta cosas. Claude Code le da inteligencia a esas conexiones. Uno sin el otro es limitado. Los dos juntos son una agencia de automatización que cabe en una laptop."

---

## SECCIÓN 6 — TENDENCIAS Y CONTEXTO ACTUAL (MARZO 2026)

### Por qué Claude Code es relevante AHORA

**El dato más fuerte:** El 84% de desarrolladores ya usa o planea usar herramientas de IA como estándar de trabajo (Stack Overflow 2026). Ya no es una tendencia — es la nueva normalidad de cómo se trabaja con tecnología.

**El movimiento "vibe coding" tiene tracción real:**
- Y Combinator (la aceleradora de Silicon Valley más importante) documenta startups lanzando MVPs completos en un fin de semana con Claude Code
- Hacker News (el foro técnico más leído del mundo) tuvo un hilo viral con el título "Tengo 60 años. Claude Code mató mi pasión por programar" — generó cientos de miles de interacciones. Por qué es relevante para la clase: hay gente que ve esto como amenaza (los que ya saben programar) y gente que lo ve como oportunidad (los que nunca supieron). El avatar de Hans está en el segundo grupo.
- El movimiento ya tiene nombre en inglés (vibe coding), lo que indica que pasó de experimento a fenómeno cultural

**Estadísticas de productividad documentadas:**
- Thoughtworks: +200% de output de código por ingeniero usando Claude Code
- La adopción en empresas pasó de "algunos equipos lo prueban" a "infraestructura estándar" entre 2025 y 2026

### Comparación con otras herramientas (para que Hans pueda contextualizar)

Esta tabla es para que Hans sepa ubicar Claude Code en el mapa. No necesita hablar de todas las herramientas — solo de las que el estudiante probablemente ya escuchó.

| Herramienta | Para qué sirve mejor | Para no programadores | Precio |
|-------------|---------------------|----------------------|--------|
| **Claude Code** | Tareas autónomas complejas, proyectos grandes, automatización real | Funciona bien si sabes describir lo que quieres | $20/mes (Claude Pro) |
| **Cursor** | Editor de código con IA integrada, para quien ya edita código | Requiere saber algo de programación | $20/mes |
| **GitHub Copilot** | Sugerencias de código mientras programas | El más accesible para principiantes que quieran aprender a programar | $10/mes |
| **Windsurf** | Proyectos y equipos grandes, codebases enormes | Fácil de usar pero diseñado para equipos técnicos | $15/mes |
| **ChatGPT + código** | Generar fragmentos de código para copiar y pegar | No ejecuta, no tiene acceso a archivos | $20/mes |

**El ángulo de ventas para Hans:** "La diferencia entre Claude Code y usar ChatGPT para 'generar código' es la diferencia entre pedirle una receta a alguien y contratar a un chef que cocina en tu cocina. Uno te da instrucciones. El otro hace el trabajo."

### Datos adicionales de adopción para usar en la clase

- Claude Code superó a herramientas similares en el benchmark SWE-bench con 80.8% de resolución de problemas complejos de código
- La valoración de Anthropic llegó a $380,000 millones de dólares en 2026 — esto indica que el mercado está apostando fuerte a esta empresa y a sus herramientas
- Claude Code ya genera más de $1,000 millones en ingresos anualizados como producto independiente

---

## SECCIÓN 7 — RECURSOS ÚTILES PARA HANS Y PARA COMPARTIR CON ESTUDIANTES

### Documentación oficial

- **Documentación oficial de Claude Code (Anthropic):** docs.anthropic.com/claude-code
- **Comunidad oficial de Anthropic:** La documentación incluye guías post-instalación accesibles con el comando `/help` dentro de Claude Code
- **API de Anthropic (para conexiones con n8n/Make):** console.anthropic.com

### Videos de referencia (en español)

- **"Aplicación con Claude Code Gratis en 5 minutos"** — Andrés Vivas (publicado 13 marzo 2026). Muestra crear apps simples desde cero con prompts en español. Enfocado en LATAM. Buscar en YouTube.
- **Canales del ecosistema Claude en español:** Buscar "Claude Code en español 2026" en YouTube — hay tutoriales nuevos publicados en las últimas semanas.

### Herramientas complementarias que mencionar en la clase

- **claude.ai** — Para empezar con el chat normal antes de pasar a Claude Code
- **console.anthropic.com** — Para obtener la API key cuando quieran integraciones avanzadas
- **nodejs.org** — Solo si necesitan instalar Node.js manualmente (el instalador nuevo no lo requiere)

### Comunidades donde está la conversación (para los estudiantes más avanzados)

- **Reddit r/ClaudeAI** — Comunidad activa, en inglés, donde se comparten casos de uso reales
- **Discord de Anthropic** — Canal oficial de la empresa
- **YouTube en español** — Buscar "vibe coding en español" o "Claude Code LATAM" para encontrar contenido reciente
- **Grupos de LinkedIn y Facebook** — "IA en Español", "Automatización con IA LATAM"

### Lo que Hans puede hacer ANTES de la clase para prepararse (si tiene 1 hora)

1. Instalar Claude Code en su computador (menos de 5 minutos, instrucciones en Sección 2)
2. Ejecutar un ejemplo sencillo en vivo: pedirle que "cree un archivo Excel con los meses del año y las ventas ficticias de un negocio"
3. Mostrar en pantalla el resultado — ese momento donde aparece el archivo creado es el momento WOW de la clase
4. Tener preparada la demo de scraper de prospectos si tiene más tiempo

---

## RESUMEN DE LOS 5 PUNTOS MÁS IMPORTANTES DE LA CLASE

Estos son los 5 conceptos que los estudiantes DEBEN llevarse de la clase:

1. **La diferencia fundamental:** Claude web responde. Claude Code actúa. Esa es la distinción más importante.

2. **La instalación es trivial:** Dos comandos, un inicio de sesión, menos de 5 minutos. No hay excusa de "es muy difícil".

3. **No necesitas saber programar:** Solo necesitas saber describir lo que quieres. El principio del "vibe coding".

4. **Los casos de uso son reales y cobrables:** Scraper de prospectos, reportes automáticos, bots de WhatsApp — todo se construye con Claude Code y todo tiene mercado.

5. **Claude Code + n8n = el stack completo:** No son rivales. n8n conecta. Claude Code le da inteligencia. Juntos permiten automatizaciones que antes requerían un equipo de developers.

---

## ÁNGULOS DE CONTENIDO SUGERIDOS (post-clase)

Después de la clase, Hans puede crear contenido sobre:

1. "Hice esto con Claude Code en 10 minutos sin saber programar" — demo en reel
2. "La herramienta que usé para conseguir 100 prospectos en 5 minutos" — ángulo de resultado
3. "Por qué el plan de $20/mes que más te conviene en IA no es el que crees" — comparación Claude Pro vs ChatGPT Pro
4. "Esto es lo que está pasando en Silicon Valley y nadie te lo está diciendo en español" — ángulo de tendencia

---

## FUENTES

- Perplexity sonar-pro (8 búsquedas, 25 marzo 2026): "Claude Code qué es diferencia Claude web", "Claude Code instalación paso a paso 2026", "Claude Code comandos básicos primer sesión", "Claude Code casos de uso no programadores automatización", "Claude Code integración n8n Make herramientas no-code", "Claude Code vs Cursor vs GitHub Copilot no programadores 2026", "Claude Code tendencias adopción marzo 2026", "Claude Code recursos tutoriales documentación principiantes"
- Anthropic Claude Code documentation (referenciado en resultados de Perplexity)
- Thoughtworks AI productivity report (citado en múltiples fuentes)
- Stack Overflow Developer Survey 2026 (84% de adopción de IA en developers)
- Y Combinator vibe coding documentation
- Hacker News viral thread sobre Claude Code (2025-2026)
- Tutorial YouTube: Andrés Vivas — "Claude Code en 5 minutos en español" (13 marzo 2026)

---

## NOTAS PARA HANS

**Sobre el nivel técnico de la clase:** La audiencia de Hans no son programadores. Son profesionales que quieren resultado. La clase debe enfocarse en el RESULTADO (qué puedo hacer, qué puedo cobrar) y tratar la instalación/uso técnico como un paso rápido, no como el tema central.

**El momento WOW de la clase:** Instalar Claude Code en vivo y ejecutar la primera instrucción en pantalla ("crea un archivo Excel con..."). Ver que en 30 segundos aparece el archivo creado en el computador es el momento que convierte a un escéptico en creyente.

**Advertencia sobre versiones:** La instalación con `npx claude-code` (el método antiguo con Node.js) está deprecada desde la versión 2.1.15 de Claude Code. El método correcto en 2026 es el instalador nativo con `curl` o `irm`. Mencionar esto si alguien encuentra tutoriales viejos de YouTube que usen el método de npm.

**Oportunidad de posicionamiento para Hans:** Claude Code es de Anthropic, la misma empresa cuyo modelo Claude usa Hans en todas sus automatizaciones. Eso crea coherencia de marca. Hans no enseña "IA genérica" — enseña el ecosistema de Anthropic, que es hoy la referencia técnica más avanzada del mercado. Ese ángulo de "estamos en el ecosistema correcto" es poderoso.
