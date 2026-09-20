# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E2 | Arrancar el programa y listar catálogo | menú, ingresar 1 para el listado | lista no vacía, sin traceback | | |
| P02 | E2 | Buscar un ítem inexistente | ingresar 3 para buscar una canción inexistente | mensaje "no se encuentra esa canción", el menú sigue | | |
| P03 | E2 | Recursión sobre un ítem con cover | ingresar 5 y buscar una canción con covers | imprime el resultado(s) | | |
| P04 | E2 | Recursión sobre un ítem sin cover | ingresar 5 y buscar una canción sin covers | mensaje "no se encontró algún cover"  | | |
| P05 | E2 | Ver detalle de un ítem existente  | ingresar 2 y escribir una canción existente | muestra todos los campos del ítem, sin error | | |
| P06 | E2 | Ver detalle con número fuera de rango | ingresar 2 y escribir una canción que no existe | mensaje "Título de canción inexistente.", el menú sigue | | |
| P07 | E2 | Buscar un ítem existente | ingresar 3, buscar un título existente | lista de coincidencias, no vacía | | |
| P08 | E2 | Ingresar una opción de menú inexistente | ingresar 10 | mensaje "Opción inválida.", el menú vuelve a mostrarse sin cerrar el programa | | |

=== Catálogo de canciones ===
1. La Flaca - Jarabe de Palo (1996)
2. Sin Documentos - Los Rodríguez (1993)
3. Muriendo de Plena - Rubén Rada (2000)
4. Microdancing - Babasónicos (2008)
5. 11 y 6 - Fito Páez (1985)
6. 11 y 6 (En Vivo) - Fito Páez (2008)
7. Just What I Needed - The Cars (1978)
8. Sultans of Swing - Dire Straits (1978)
9. Have You Ever Seen the Rain? - Creedence Clearwater Revival (1970)
10. Have You Ever Seen the Rain? - Joan Jett (1981)
11. Have You Ever Seen the Rain? - Spin Doctors (1991)
12. Beat It - Michael Jackson (1982)
13. Enjoy the Silence - Depeche Mode (1990)
14. Boulevard of Broken Dreams - Green Day (2004)
15. Africa - Toto (1982)
16. Africa - Weezer (2019)
17. Ride - Twenty One Pilots (2015)
18. You Talk - Babyshambles (2007)
19. The Adults Are Talking - The Strokes (2020) | funciona como se esperaba |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  -1
Opción inválida. | funciona como se esperaba |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa | === Biblioteca musical —

AyED C2 2026 ===
1. Listar catálogo
2. Ver detalle
3. Buscar
4. Ordenar
5. Operación recursiva
6. Colección principal (equipo / menú / playlist)
7. Historial (pila)
8. Cola
9. Guardar / cargar archivos
0. Salir
> 5

=== Catálogo de canciones ===
1. La Flaca - Jarabe de Palo (1996)
2. Sin Documentos - Los Rodríguez (1993)
3. Muriendo de Plena - Rubén Rada (2000)
4. Microdancing - Babasónicos (2008)
5. 11 y 6 - Fito Páez (1985)
6. 11 y 6 (En Vivo) - Fito Páez (2008)
7. Just What I Needed - The Cars (1978)
8. Sultans of Swing - Dire Straits (1978)
9. Have You Ever Seen the Rain? - Creedence Clearwater Revival (1970)
10. Have You Ever Seen the Rain? - Joan Jett (1981)
11. Have You Ever Seen the Rain? - Spin Doctors (1991)
12. Beat It - Michael Jackson (1982)
13. Enjoy the Silence - Depeche Mode (1990)
14. Boulevard of Broken Dreams - Green Day (2004)
15. Africa - Toto (1982)
16. Africa - Weezer (2019)
17. Ride - Twenty One Pilots (2015)
18. You Talk - Babyshambles (2007)
19. The Adults Are Talking - The Strokes (2020)

Elegí el número de la canción original: 9

=== Versiones de Have You Ever Seen the Rain? ===
- Have You Ever Seen the Rain? - Joan Jett (1981)
- Have You Ever Seen the Rain? - Spin Doctors (1991) | funciono como se esperaba |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) | 
=== Biblioteca musical — AyED C2 2026 ===
1. Listar catálogo
2. Ver detalle
3. Buscar
4. Ordenar
5. Operación recursiva
6. Colección principal (equipo / menú / playlist)
7. Historial (pila)
8. Cola
9. Guardar / cargar archivos
0. Salir
> 5

=== Catálogo de canciones ===
1. La Flaca - Jarabe de Palo (1996)
2. Sin Documentos - Los Rodríguez (1993)
3. Muriendo de Plena - Rubén Rada (2000)
4. Microdancing - Babasónicos (2008)
5. 11 y 6 - Fito Páez (1985)
6. 11 y 6 (En Vivo) - Fito Páez (2008)
7. Just What I Needed - The Cars (1978)
8. Sultans of Swing - Dire Straits (1978)
9. Have You Ever Seen the Rain? - Creedence Clearwater Revival (1970)
10. Have You Ever Seen the Rain? - Joan Jett (1981)
11. Have You Ever Seen the Rain? - Spin Doctors (1991)
12. Beat It - Michael Jackson (1982)
13. Enjoy the Silence - Depeche Mode (1990)
14. Boulevard of Broken Dreams - Green Day (2004)
15. Africa - Toto (1982)
16. Africa - Weezer (2019)
17. Ride - Twenty One Pilots (2015)
18. You Talk - Babyshambles (2007)
19. The Adults Are Talking - The Strokes (2020)

Elegí el número de la canción original: 3

=== Versiones de Muriendo de Plena ===
No se encontraron versiones. | funciono como se esperaba |
