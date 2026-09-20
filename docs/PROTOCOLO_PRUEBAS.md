# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).


=======
| P01 | E2 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |no corrido | |
| P02 | E2 | Buscar un ítem inexistente (id = -1) | id = -1 | mensaje claro, el menú sigue | no corrido | |
| P03 | E2 | Recursión sobre un ítem con cover | id con derivados | imprime el resultado(s) | no corrido | |
| P04 | E2 | Recursión sobre un ítem sin cover | id sin derivados | mensaje "no se encontró algún cover"  | no corrido | |
| P05 | E2 | Ver detalle de un ítem existente  | número válido de catálogo | muestra todos los campos del ítem, sin error | no corrido | |
| P06 | E2 | Ver detalle con número fuera de rango | ej: número a ingresar = 999 | mensaje "Número de canción inválido.", el menú sigue | no corrido | |
| P07 | E2 | Buscar por texto existente | texto = título o artista real | lista de coincidencias, no vacía | no corrido | |
| P08 | E2 | Ingresar una opción de menú inexistente | opción = "10" | mensaje "Opción inválida.", el menú vuelve a mostrarse sin cerrar el programa | no corrido | |

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P09 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  |  |
| P10 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  |  |
| P11 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |  |
| P12 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  |  |
| P13 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P14 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P15 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P16 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P17 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P18 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P19 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
>>>
>>>> 421c11d (Actualiza el protocolo de pruebas)
