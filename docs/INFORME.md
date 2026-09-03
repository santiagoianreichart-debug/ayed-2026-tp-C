# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca Musical
- Por qué lo eligieron (5–8 líneas): Lo elegimos porque somos usuarios de Spotify y nos parecio el proyecto más cercano a nuestros gustos. También porque queremos aplicar nuestros conocimientos en crear un catalogo, listas de reproducción, etc; similares a dicha aplicación.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Catálogo es la lista completa de canciones, cada canción del CSV se convierte en el objeto "Cancion" por lo tanto es mutable ya que pueden editarse, crearse o eliminarse canciones de la lista.

Ítem del catálogo es una instancia de la clase Cancion. Es inmutable ya que funciona como "plantilla" o molde para cada canción pero sus atributos: titulo, artista, album, genero y anio son mutables.

Colección Principal es una lista creada por el usuario al añadir o borrar canciones, es mutable. Funciona como una lista derivada del Catálogo.

Pila es el historial de acciones del usuario ordenado desde la última acción realizada. Es mutable ya que depende de borrar o agregar canciones.

Cola es la lista de reproducción de la biblioteca, se reproduce de acuerdo al orden en que fueron agregadas (primero el primero, último el último). Es mutable ya que el usuario puede agregar o terminar de escuchar las canciones.

ASCII: 

CATÁLOGO (todas las canciones de la database)
   
   | 
  
   +--> COLECCIÓN PRINCIPAL (playlist creada por el usuario)
  
   |
   
   +--> PILA (historial de acciones)
   
   |
  
   +--> COLA (lista de reproducción actual)

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
