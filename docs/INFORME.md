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
