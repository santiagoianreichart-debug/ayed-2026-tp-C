
"""Persistencia binaria de canciones mediante registros de longitud fija."""

import struct

from src.config import TEMA
from src.dominio.cancion import Cancion
from src.excepciones import ArchivoInvalidoError, ItemNoEncontradoError
from src.tads.lista_enlazada import ListaEnlazada


# Encabezado: magia (4 bytes), tema (1 byte), cantidad (4 bytes).
HEADER = struct.Struct("<4s1sI")

# Registro: id, titulo, artista, album, genero, anio y duracion.
FORMATO = struct.Struct("<I30s25s30s12s2H")

MAGIA = b"AYED"
TEMA_BINARIO = b"M"


def _codificar_texto(texto, cantidad):
    """Codifica texto UTF-8 y lo completa hasta alcanzar el tamaño fijo."""

    datos = str(texto).encode("utf-8")
    datos = datos[:cantidad]

    # Evita conservar caracteres UTF-8 cortados a la mitad.
    datos = datos.decode("utf-8", errors="ignore").encode("utf-8")

    return datos.ljust(cantidad, b"\0")


def _decodificar_texto(datos):
    """Convierte un campo binario de texto en una cadena."""

    return datos.split(b"\0", 1)[0].decode("utf-8")


def _item_a_tupla(cancion):
    """Convierte una Cancion en los campos del registro binario."""

    return (
        cancion.id,
        _codificar_texto(cancion.titulo, 30),
        _codificar_texto(cancion.artista, 25),
        _codificar_texto(cancion.album, 30),
        _codificar_texto(cancion.genero, 12),
        cancion.anio,
        cancion.duracion_seg,
    )


def _tupla_a_item(datos):
    """Convierte un registro binario en un objeto Cancion."""

    return Cancion(
        datos[0],
        _decodificar_texto(datos[1]),
        _decodificar_texto(datos[2]),
        _decodificar_texto(datos[3]),
        _decodificar_texto(datos[4]),
        datos[5],
        datos[6],
    )


def guardar_binario(ruta, catalogo):
    """Guarda el catálogo completo en un archivo binario."""

    try:
        with open(ruta, "wb") as archivo:
            archivo.write(
                HEADER.pack(MAGIA, TEMA_BINARIO, len(catalogo))
            )

            for cancion in catalogo:
                archivo.write(FORMATO.pack(*_item_a_tupla(cancion)))

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el archivo binario: {error}"
        )


def cargar_binario(ruta):
    """Carga un archivo binario y devuelve una ListaEnlazada."""

    try:
        with open(ruta, "rb") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError(
                    "Binario truncado: encabezado incompleto."
                )

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != MAGIA:
                raise ArchivoInvalidoError(
                    "La firma del archivo no corresponde al TP."
                )

            if tema != TEMA_BINARIO:
                raise ArchivoInvalidoError(
                    "El archivo no corresponde al tema Música."
                )

            catalogo = ListaEnlazada()

            for _ in range(cantidad):
                datos = archivo.read(FORMATO.size)

                if len(datos) != FORMATO.size:
                    raise ArchivoInvalidoError(
                        "Binario truncado: falta uno o más registros."
                    )

                tupla = FORMATO.unpack(datos)
                catalogo.insertar_al_final(_tupla_a_item(tupla))

            if archivo.read(1):
                raise ArchivoInvalidoError(
                    "El archivo contiene datos adicionales inesperados."
                )

            return catalogo

    except FileNotFoundError:
        raise ArchivoInvalidoError("No se encontró el archivo binario.")

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo leer el archivo binario: {error}"
        )


def actualizar_registro(ruta, posicion, item):
    """Modifica un registro por posición, sin reescribir el archivo completo."""

    if posicion < 0:
        raise ArchivoInvalidoError("La posición no puede ser negativa.")

    try:
        with open(ruta, "r+b") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError("Encabezado binario incompleto.")

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != MAGIA or tema != TEMA_BINARIO:
                raise ArchivoInvalidoError("El archivo binario no es válido.")

            if posicion >= cantidad:
                raise ArchivoInvalidoError("La posición está fuera del archivo.")

            archivo.seek(HEADER.size + posicion * FORMATO.size)
            archivo.write(FORMATO.pack(*_item_a_tupla(item)))

    except FileNotFoundError:
        raise ArchivoInvalidoError("No se encontró el archivo binario.")

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo actualizar el registro: {error}"
        )


def posicion_del_id(catalogo, id_buscado):
    """Devuelve la posición (desde cero) de una canción según su ID."""

    for posicion, cancion in enumerate(catalogo):
        if cancion.id == id_buscado:
            return posicion

    raise ItemNoEncontradoError(
        f"No hay una canción con ID {id_buscado}."
    )

"""Persistencia binaria de canciones mediante registros de longitud fija."""

import struct

from src.config import TEMA
from src.dominio.cancion import Cancion
from src.excepciones import ArchivoInvalidoError, ItemNoEncontradoError
from src.tads.lista_enlazada import ListaEnlazada


# Encabezado: magia (4 bytes), tema (1 byte), cantidad (4 bytes).
HEADER = struct.Struct("<4s1sI")

# Registro: id, titulo, artista, album, genero, anio y duracion.
FORMATO = struct.Struct("<I30s25s30s12s2H")

MAGIA = b"AYED"
TEMA_BINARIO = b"M"


def _codificar_texto(texto, cantidad):
    """Codifica texto UTF-8 y lo completa hasta alcanzar el tamaño fijo."""

    datos = str(texto).encode("utf-8")
    datos = datos[:cantidad]

    # Evita conservar caracteres UTF-8 cortados a la mitad.
    datos = datos.decode("utf-8", errors="ignore").encode("utf-8")

    return datos.ljust(cantidad, b"\0")


def _decodificar_texto(datos):
    """Convierte un campo binario de texto en una cadena."""

    return datos.split(b"\0", 1)[0].decode("utf-8")


def _item_a_tupla(cancion):
    """Convierte una Cancion en los campos del registro binario."""

    return (
        cancion.id,
        _codificar_texto(cancion.titulo, 30),
        _codificar_texto(cancion.artista, 25),
        _codificar_texto(cancion.album, 30),
        _codificar_texto(cancion.genero, 12),
        cancion.anio,
        cancion.duracion_seg,
    )


def _tupla_a_item(datos):
    """Convierte un registro binario en un objeto Cancion."""

    return Cancion(
        datos[0],
        _decodificar_texto(datos[1]),
        _decodificar_texto(datos[2]),
        _decodificar_texto(datos[3]),
        _decodificar_texto(datos[4]),
        datos[5],
        datos[6],
    )


def guardar_binario(ruta, catalogo):
    """Guarda el catálogo completo en un archivo binario."""

    try:
        with open(ruta, "wb") as archivo:
            archivo.write(
                HEADER.pack(MAGIA, TEMA_BINARIO, len(catalogo))
            )

            for cancion in catalogo:
                archivo.write(FORMATO.pack(*_item_a_tupla(cancion)))

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el archivo binario: {error}"
        )


def cargar_binario(ruta):
    """Carga un archivo binario y devuelve una ListaEnlazada."""

    try:
        with open(ruta, "rb") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError(
                    "Binario truncado: encabezado incompleto."
                )

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != MAGIA:
                raise ArchivoInvalidoError(
                    "La firma del archivo no corresponde al TP."
                )

            if tema != TEMA_BINARIO:
                raise ArchivoInvalidoError(
                    "El archivo no corresponde al tema Música."
                )

            catalogo = ListaEnlazada()

            for _ in range(cantidad):
                datos = archivo.read(FORMATO.size)

                if len(datos) != FORMATO.size:
                    raise ArchivoInvalidoError(
                        "Binario truncado: falta uno o más registros."
                    )

                tupla = FORMATO.unpack(datos)
                catalogo.insertar_al_final(_tupla_a_item(tupla))

            if archivo.read(1):
                raise ArchivoInvalidoError(
                    "El archivo contiene datos adicionales inesperados."
                )

            return catalogo

    except FileNotFoundError:
        raise ArchivoInvalidoError("No se encontró el archivo binario.")

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo leer el archivo binario: {error}"
        )


def actualizar_registro(ruta, posicion, item):
    """Modifica un registro por posición, sin reescribir el archivo completo."""

    if posicion < 0:
        raise ArchivoInvalidoError("La posición no puede ser negativa.")

    try:
        with open(ruta, "r+b") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError("Encabezado binario incompleto.")

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != MAGIA or tema != TEMA_BINARIO:
                raise ArchivoInvalidoError("El archivo binario no es válido.")

            if posicion >= cantidad:
                raise ArchivoInvalidoError("La posición está fuera del archivo.")

            archivo.seek(HEADER.size + posicion * FORMATO.size)
            archivo.write(FORMATO.pack(*_item_a_tupla(item)))

    except FileNotFoundError:
        raise ArchivoInvalidoError("No se encontró el archivo binario.")

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo actualizar el registro: {error}"
        )


def posicion_del_id(catalogo, id_buscado):
    """Devuelve la posición (desde cero) de una canción según su ID."""

    for posicion, cancion in enumerate(catalogo):
        if cancion.id == id_buscado:
            return posicion

    raise ItemNoEncontradoError(
        f"No hay una canción con ID {id_buscado}."
    )
def alta_binario(ruta, item):
    """Agrega una canción al final y actualiza la cantidad del encabezado."""

    try:
        registro = FORMATO.pack(*_item_a_tupla(item))

        with open(ruta, "r+b") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError("Encabezado binario incompleto.")

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != MAGIA or tema != TEMA_BINARIO:
                raise ArchivoInvalidoError("El archivo binario no es válido.")

            archivo.seek(0, 2)
            tamanio_esperado = HEADER.size + cantidad * FORMATO.size

            if archivo.tell() != tamanio_esperado:
                raise ArchivoInvalidoError("El archivo binario está incompleto.")

            archivo.write(registro)

            archivo.seek(0)
            archivo.write(HEADER.pack(magia, tema, cantidad + 1))

    except FileNotFoundError:
        raise ArchivoInvalidoError("No se encontró el archivo binario.")

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo agregar la canción: {error}"
        )


def baja_binario(ruta, posicion):
    """Elimina una canción por posición y reescribe el archivo."""

    if posicion < 0:
        raise ArchivoInvalidoError("La posición no puede ser negativa.")

    try:
        with open(ruta, "r+b") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError("Encabezado binario incompleto.")

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != MAGIA or tema != TEMA_BINARIO:
                raise ArchivoInvalidoError("El archivo binario no es válido.")

            if posicion >= cantidad:
                raise ArchivoInvalidoError("La posición está fuera del archivo.")

            registros = []

            for _ in range(cantidad):
                datos = archivo.read(FORMATO.size)

                if len(datos) != FORMATO.size:
                    raise ArchivoInvalidoError(
                        "Binario truncado: falta uno o más registros."
                    )

                registros.append(datos)

            if archivo.read(1):
                raise ArchivoInvalidoError(
                    "El archivo contiene datos adicionales inesperados."
                )

            del registros[posicion]

            archivo.seek(0)
            archivo.truncate()

            archivo.write(HEADER.pack(magia, tema, len(registros)))

            for datos in registros:
                archivo.write(datos)

    except FileNotFoundError:
        raise ArchivoInvalidoError("No se encontró el archivo binario.")

    except (OSError, struct.error, UnicodeError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo eliminar la canción: {error}"
        )
