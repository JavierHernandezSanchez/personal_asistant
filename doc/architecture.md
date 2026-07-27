# Arquitectura del Asistente Personal

## 1. Visión

El objetivo no es crear un chatbot.

El objetivo es construir un sistema capaz de ayudar al usuario en su trabajo diario mediante razonamiento, memoria y herramientas.

El LLM es un componente del sistema, no el sistema.

## 2. Principios
### 1. Responsabilidad única
cada módulo hace una sola cosa y no mezclamos responsabilidades

### 1. Componentes intercambiables
debe ser posible cambiar OpenAI, Whisper o SQLite por alternativas sin reescribir el proyecto. Esto obliga a escribir interfaces limpias

### 1. El asistente piensa y las herramientas actuan
el LLM nunca ejecuta código, nunca borra archivos o abre programas. Indica que necesita usar una herramienta y el programa decide si se ejecuta.

### 1. Toda acción debe ser trazable
si el asistente hace algo debe ser capaz de responder por qué lo hizo. Se registran acciones y decisiones.

### 1. La memoria pertenece al asitente, no al modelo
no dependemos de la ventana de contexto para recorar cosas importantes.

## 3. Grandes módulos

* Usuario
* Interfaz
* Agent: the agent coordinates the execution of tasks by using the available tools, memory and language model. It does not implement any capability itself; it dlegates responsibilities to specialized components.
    - Planner
    - Memoria
    - Herramientas
    - LLM
    - Configuración
    - Política de decisión y coordinación
    - Eventos
    - Seguridad

el núcleo del proyecto es el agente que conoce al resto de componentes y utiliza un LLM solo cuando necesita inteligencia lingüistica o razonamiento.

## 4. Flujo general
Usuario -> Interpretación -> Plan -> Herramientas -> Resultado -> Respuesta

## 5. Lo que no es
No intenta sustituir un sistema operativo.
No automatiza acciones peligrosas por defecto.
No depende de un proveedor concreto.
No almacena secretos en texto plano.
No mezcla lógica de negocio con llamadas al modelo.

