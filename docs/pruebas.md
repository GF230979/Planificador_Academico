# Registro de pruebas
## Planificador Académico con Prerrequisitos

### 1. Objetivo

Documentar las pruebas unitarias realizadas para verificar
el funcionamiento de los componentes principales del proyecto.

### 2. Entorno de ejecución

- Lenguaje: Python.
- Herramienta de pruebas: unittest.
- Comando utilizado: `python -m unittest discover -s pruebas -v`.

### 3. Resultados de las pruebas

| Archivo | Pruebas ejecutadas | Resultado |
|---|---:|---|
| test_materia.py | 6 | Exitoso |
| test_cola.py | 7 | Exitoso |
| test_grafo.py | 11 | Exitoso |
| test_planificador.py | 8 | Exitoso |
| Total | 32 | Exitoso |

### 4. Verificaciones realizadas

#### Materia
Se verificó la creación de materias, la eliminación de espacios
exteriores, el rechazo de datos inválidos y la comparación
de códigos sin distinguir mayúsculas y minúsculas.

<img width="1287" height="303" alt="imagen" src="https://github.com/user-attachments/assets/4258e2bd-9dd3-47a4-81fb-7db624dd52c6" />


#### Cola
Se verificó el estado inicial vacío, el ingreso y retiro de
elementos, el orden FIFO, la consulta del frente y el tamaño.
<img width="1071" height="315" alt="imagen" src="https://github.com/user-attachments/assets/34d56271-f0a2-486c-9de7-3d2159943bf0" />

#### Grafo
Se verificó el registro de materias, la creación de relaciones
de prerrequisitos, el cálculo del grado de entrada y el rechazo
de materias o relaciones inválidas y duplicadas.
<img width="1345" height="412" alt="imagen" src="https://github.com/user-attachments/assets/58601e83-310e-40fa-a562-96211f01b1f9" />

#### Planificador
Se verificó la planificación de un grafo vacío, el orden de
los prerrequisitos, la agrupación por niveles, el tratamiento
de materias independientes y la detección de ciclos.
<img width="1427" height="338" alt="imagen" src="https://github.com/user-attachments/assets/7dc98803-5b37-4477-8671-68262907b099" />

### 5. Resultado general

La ejecución general reportó 32 pruebas ejecutadas,
sin fallos ni errores.

### 6. Evidencia

La evidencia corresponde a la captura de la terminal en la que
se ejecutó el comando:

`python -m unittest discover -s pruebas -v`

El resultado mostrado fue `Ran 32 tests` y `OK`.
<img width="1391" height="862" alt="imagen" src="https://github.com/user-attachments/assets/a05cf11e-5562-4219-a5ce-43a51bdd4f63" />

