# Bitácora de desarrollo
## Planificador Académico con Prerrequisitos

### 1. Objetivo

Registrar las dificultades, correcciones y decisiones técnicas
durante la implementación del proyecto.

### 2. Registro de actividades

#### Actividad 1. Implementación de la clase Materia

**Trabajo realizado:** se implementó la clase Materia para
representar las materias mediante un código y un nombre.

**Validaciones:** se incorporó el rechazo de campos vacíos
y de valores que no sean cadenas de texto.

**Resultado:** las 6 pruebas unitarias pasaron correctamente.

#### Actividad 2. Implementación de la cola

**Trabajo realizado:** se implementó una cola FIFO con
operaciones para encolar, desencolar, consultar el frente
y obtener el tamaño.

**Validaciones:** se verificó el orden de salida y el
comportamiento cuando la cola está vacía.

**Resultado:** las 7 pruebas unitarias pasaron correctamente.

#### Actividad 3. Implementación del grafo dirigido

**Trabajo realizado:** se implementó el registro de materias
y las relaciones dirigidas de prerrequisitos.

**Validaciones:** se probaron las materias duplicadas,
las relaciones inválidas y el cálculo del grado de entrada.

**Resultado:** las 11 pruebas unitarias pasaron correctamente.

#### Actividad 4. Implementación del planificador

**Trabajo realizado:** se implementó el algoritmo de Kahn
para generar un plan académico por niveles y detectar ciclos.

**Dificultad encontrada:** una prueba de agrupación por niveles
esperaba que una materia con prerrequisitos y otra materia
independiente aparecieran separadas, aunque ambas podían
procesarse en el primer nivel.

**Solución aplicada:** se corrigió la prueba para considerar
que las materias independientes pueden compartir nivel cuando
no existen dependencias entre ellas.

**Resultado:** las 8 pruebas unitarias pasaron correctamente
después de corregir la prueba.

### 3. Integración de componentes

Se conectaron las estructuras y el planificador con la interfaz
de consola y el punto de entrada principal.

Se realizó una prueba manual registrando dos materias,
estableciendo una relación de prerrequisito y generando el plan
académico en el orden esperado.

### 4. Verificación general

Se ejecutó el comando:

`python -m unittest discover -s pruebas -v`

**Resultado observado:** 32 pruebas ejecutadas, sin fallos
ni errores.

### 5. Decisiones técnicas

- Mantener una estructura modular y responsabilidades separadas.
- Probar cada componente antes de integrarlo con los demás.
- Utilizar una cola FIFO para el algoritmo de Kahn.
- Representar los prerrequisitos mediante un grafo dirigido.
- Mantener la estructura de carpetas y archivos acordada.

### 6. Estado actual

Los componentes implementados superaron las pruebas unitarias
registradas y el flujo principal se verificó manualmente.

Quedan pendientes las revisiones adicionales que requiera
la rúbrica de la Fase 2 y la preparación de sus evidencias
y presentación.
