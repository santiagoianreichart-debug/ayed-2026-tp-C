# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca Musical
- Por qué lo eligieron (5–8 líneas): Lo elegimos porque somos usuarios de Spotify y nos parecio el proyecto más cercano a nuestros gustos. También porque queremos aplicar nuestros conocimientos en crear un catalogo, listas de reproducción, etc; similares a dicha aplicación.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

El catálogo contiene las canciones disponibles en la biblioteca. En E1 se encuentra armado manualmente mediante una lista de objetos `Cancion`.

Un ítem del catálogo es una instancia de la clase `Cancion`. Cada objeto contiene los datos de una canción: id, título, artista, álbum, género, año y duración. El objeto `Cancion` es mutable porque sus atributos pueden modificarse.

El catálogo también es mutable porque se representa mediante una lista de Python, cuyos elementos pueden agregarse o eliminarse.

Los atributos de tipo `str`, como título, artista, álbum y género, son objetos inmutables. Lo mismo ocurre con los atributos de tipo `int`, como id, año y duración. Si se asigna otro valor a uno de estos atributos, se reemplaza el objeto anterior por otro valor.

La Colección Principal será una lista creada por el usuario a partir de las canciones del catálogo. Es mutable porque se podrán agregar o eliminar canciones.

La Pila representará el historial de acciones del usuario. Es mutable y seguirá el principio LIFO (Last In, First Out), por el cual la última acción agregada será la primera en retirarse.

La Cola representará la lista de reproducción. Es mutable y seguirá el principio FIFO (First In, First Out), por el cual la primera canción agregada será la primera en salir.

ASCII:

CATÁLOGO
(todas las canciones)
      |
      +--> COLECCIÓN PRINCIPAL
      |    (playlist creada por el usuario)
      |
      +--> PILA
      |    (historial de acciones)
      |
      +--> COLA
           (lista de reproducción actual)


## 3. Recursión (E2)

Se implementó una función recursiva para listar todas las versiones derivadas de una canción a partir de la relación entre `version_de` e `id`.

* **Función:** `listar_versiones_recursivas(canciones, id_cancion, indice=0)`.
* **Caso base:** cuando `indice == len(canciones)`, se llegó al final del catálogo. En ese momento no quedan canciones por analizar y la función retorna una lista vacía.
* **Caso recursivo:** se analiza la canción ubicada en el índice actual. Si su atributo `version_de` coincide con el ID buscado, se agrega como versión y se realiza una llamada recursiva para buscar si esa versión tiene otras versiones derivadas. Luego se continúa recorriendo el catálogo para encontrar otras versiones de la canción original.

### Traza

Se toma como ejemplo la canción `"Have You Ever Seen the Rain?"` de Creedence Clearwater Revival, cuyo ID es `8`.

En el catálogo existen dos versiones derivadas:

* ID `16`: Have You Ever Seen the Rain? - Joan Jett (1981), con `version_de = 8`.
* ID `17`: Have You Ever Seen the Rain? - Spin Doctors (1991), con `version_de = 8`.

La llamada inicial es:

```text
listar_versiones_recursivas(catalogo, 8, 0)
```

La función recorre el catálogo hasta encontrar una canción cuyo `version_de` sea `8`.

```text
listar_versiones_recursivas(catalogo, 8, 0)
    ↓
recorre el catálogo
    ↓
encuentra Joan Jett (ID 16, version_de = 8)
    ↓
agrega Joan Jett a la lista
    ↓
llamada recursiva:
listar_versiones_recursivas(catalogo, 16, 0)
    ↓
recorre el catálogo buscando versiones de Joan Jett
    ↓
no encuentra ninguna
    ↓
llega al final del catálogo
    ↓
caso base → retorna []
    ↓
vuelve a la llamada que buscaba versiones de ID 8
    ↓
continúa recorriendo el catálogo
    ↓
encuentra Spin Doctors (ID 17, version_de = 8)
    ↓
agrega Spin Doctors a la lista
    ↓
llamada recursiva:
listar_versiones_recursivas(catalogo, 17, 0)
    ↓
recorre el catálogo buscando versiones de Spin Doctors
    ↓
no encuentra ninguna
    ↓
llega al final del catálogo
    ↓
caso base → retorna []
    ↓
continúa la búsqueda de versiones de ID 8
    ↓
llega al final del catálogo
    ↓
caso base → retorna []
```

### Resultado

```text
Have You Ever Seen the Rain? - Joan Jett (1981)
Have You Ever Seen the Rain? - Spin Doctors (1991)
```

La función utiliza recursividad porque se vuelve a llamar a sí misma para resolver el mismo problema sobre una versión encontrada. De esta manera, si una versión tuviera a su vez otras versiones derivadas, la misma lógica permitiría continuar recorriendo esas relaciones.




- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
