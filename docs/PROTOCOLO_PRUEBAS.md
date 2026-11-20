# Protocolo de pruebas

Pruebas **manuales**. Cada fila representa un caso de prueba ejecutado desde la consola.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos documentados en E2, ejecutados en E3 y 15 pruebas de regresión en E6 (pila, cola, archivos, recursión, búsquedas y ordenamiento).

## 1. Pruebas de las entregas E2 a E5

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E2 | Arrancar el programa y listar catálogo | Dataset de la cátedra | Lista no vacía, sin traceback | pasa | |
| P02 | E2 | Buscar un ítem inexistente | ID = -1 | Mensaje claro, el menú sigue | pasa | Mensaje: "No se encontraron canciones." |
| P03 | E2 | Recursión sobre un ítem con cover | ID con derivados | Imprime los resultados | pasa | |
| P04 | E2 | Recursión sobre un ítem sin cover | ID sin derivados | Mensaje "No se encontraron versiones." | pasa | |
| P05 | E2 | Ver detalle de un ítem existente | Número válido de catálogo | Muestra todos los campos del ítem, sin error | pasa | |
| P06 | E2 | Ver detalle con número fuera de rango | Número = 999 | Mensaje "Número de canción inválido.", el menú sigue | pasa | |
| P07 | E2 | Buscar por texto existente | Título o artista real | Lista de coincidencias no vacía | pasa | |
| P08 | E2 | Ingresar una opción de menú inexistente | Opción = 10 | Mensaje "Opción inválida.", el menú vuelve a mostrarse | pasa | |
| P09 | E3 | Agregar a la colección principal hasta el tope | Playlist de 6 canciones | El séptimo intento falla con excepción propia | pasa | Se agregaron 6 canciones. Al intentar agregar una séptima, mostró: "El equipo está lleno (máximo 6). No se puede agregar más." |
| P10 | E3 | Desapilar historial vacío | Pila vacía | Excepción propia, menú sigue | pasa | Mostró: "No hay acciones en el historial para deshacer." |
| P11 | E3 | Desencolar cola vacía | Cola vacía | Excepción propia, menú sigue | pasa | Mostró: "No hay elementos en la cola." |
| P12 | E3 | Listar colección con el iterador | IDs 1, 6 y 8 | El orden coincide con las inserciones | pasa | Las canciones se mostraron en el mismo orden de inserción, numeradas 1, 2 y 3. |
| P13 | E4 | Búsqueda lineal de un nombre existente | Título de una canción existente | Lo encuentra y lo muestra | pasa | |
| P14 | E4 | Búsqueda lineal de un nombre inexistente | `zzz_no_existe` | No encontrado, sin traceback, el menú sigue | pasa | |
| P15 | E4 | Búsqueda binaria con catálogo desordenado | Catálogo desordenado | Avisa o reordena; no da un falso "no encontrado" | pasa | |
| P16 | E4 | Ordenar por un criterio y después por otro | Título y año | El orden cambia correctamente según cada criterio | pasa | |
| P17 | E5 | Ordenar por Quicksort por título | Título | El orden cambia correctamente | pasa | |
| P18 | E5 | Ordenar por Quicksort mediana de tres por artista | Artista | El orden cambia correctamente | pasa | |
| P19 | E5 | Guardar CSV, salir y volver a entrar | Catálogo | Los datos se conservan | pasa | |
| P20 | E5 | Guardar binario y modificar un registro por ID | ID existente | Al recargar, el campo modificado se conserva | pasa | |
| P21 | E5 | Abrir un binario truncado o con magia incorrecta | Archivo inválido | Excepción de archivo inválido, sin traceback | pasa | |

## 2. Regresión final E6

Las siguientes verificaciones corresponden a los 15 casos solicitados para la entrega E6. Se reutilizan las pruebas anteriores cuando cubren el mismo comportamiento.

| ID | Acción | Prueba relacionada | Resultado | Notas |
| --- | --- | --- | --- | --- |
| E6-P01 | Iniciar el programa y listar el catálogo | P01 | pasa | Verificado nuevamente en E6. |
| E6-P02 | Buscar un elemento inexistente | P02 | pasa | Se muestra un mensaje claro y el menú continúa. |
| E6-P03 | Ejecutar la operación recursiva con versiones derivadas | P03 | pasa | Prueba documentada en E2. |
| E6-P04 | Ejecutar la operación recursiva sin versiones derivadas | P04 | pasa | Prueba documentada en E2. |
| E6-P05 | Completar la colección principal hasta el límite | P09 | pasa | Se verifica el límite de 6 canciones. |
| E6-P06 | Deshacer una acción con el historial vacío | P10 | pasa | Se captura la excepción propia. |
| E6-P07 | Reproducir con la cola vacía | P11 | pasa | Se captura la excepción propia. |
| E6-P08 | Recorrer la colección mediante el iterador | P12 | pasa | Se conserva el orden de inserción. |
| E6-P09 | Realizar una búsqueda lineal existente | P13 | pasa | Prueba documentada en E4. |
| E6-P10 | Realizar una búsqueda lineal inexistente | P14 | pasa | No produce traceback. |
| E6-P11 | Realizar una búsqueda binaria con catálogo desordenado | P15 | pasa | Se controla el orden de los datos. |
| E6-P12 | Ordenar por dos criterios diferentes | P16 | pasa | Prueba documentada en E4. |
| E6-P13 | Guardar en TXT, salir y volver a iniciar | Nueva prueba E6 | pasa | Verificado nuevamente en E6. El catálogo se conserva después de reiniciar. |
| E6-P14 | Guardar en binario, modificar un registro y recargar | P20 | pasa | Prueba documentada en E5. |
| E6-P15 | Cargar un archivo binario corrupto | P21 | pasa | Se controla el error de archivo inválido. |

## 3. Validación adicional de entradas

| Acción | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- |
| Ingresar texto (`abc`) cuando se solicita el año al dar de alta una canción | Mensaje de error controlado, sin traceback | pasa | Se mostró: "El año, la duración y el ID deben ser números." |
