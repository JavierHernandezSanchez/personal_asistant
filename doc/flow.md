# Qué hace el sistema cuando el usuario dice algo al asistente?

- Usuario
- Interfaz
- Agente
    - Comprende la petición
    - Consulta la memoria
    - Decide un plan
    - Ejecuta herramientas
    - Verifica resultados
    - Genera una respuesta
- Usuario

## Herramienta
 Representa una capacidad del sistema
 No toma decisiones
 Recibe parámetros
 Ejecuta una acción
 Devuelve un resultado
 
 ## Plan
 Un plan es una secuencia de acciones para resolver una tarea
 El agente puede modificar el plan durante la ejecución
 No ejecuta código

 ## Memoria
 La memoria almacena el conocimiento persistente del sistema
 Debe poder recuperar información
 No decide cuando se debe utilizar

 ## LLm
 Servicio externo
 no conoce el sistema
 no conoce las herramientas
 No conoce la memoria
 Solo recibe contexto y produce texto estructurado

 ## Tarea

Una tarea representa un objetivo solicitado al sistema.
Describe qué resultado desea obtener el usuario, pero no especifica cómo alcanzarlo.
Una tarea puede requerir uno o varios planes para completarse.
Las tareas pueden dividirse en subtareas.

## Acción
Una acción es una operación atómica ejecutable por el sistema:
- Leer un archivo
- Llamar a un LLM
- Guardar memoria
- Ejecutar una búsqueda
- Enviar un correo

Las acciones son generadas por el planificador y ejecutadas por el agente

Toda acción tiene:
- Entrada
- Ejecutor
- Salida
- Estado

## Contexto

- Conversación reciente
- Memoria
- Tarea actual
- Plan
- Historial de acciones
- Environment
- Permisos
- Configuración
- Datos externos

## Capacidad
Una herramienta es una implementación, el agente no piensa en implementaciones sino en capacidades, por ejemplo leer documentos es una capacidad, ReadPDFTool y ReadDocxTool son implementaciones

## Ejecución
representa una instancia concreta de un trabajo, todo lo que ocurre durante una petición pertenece a la misma ejecución
- contexto
- logs
- acciones
- errores
- métricas
- decisioens

Usuario -> Ejecución -> Tarea -> Planificador -> Plan (estrategia) -> Acción (Paso concreto) -> Capacidad -> Herramienta -> Resultado

