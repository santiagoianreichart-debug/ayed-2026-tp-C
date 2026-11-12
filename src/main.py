

from pathlib import Path

from src.config import TEMA
from src.dominio import (
    mostrar_catalogo,
    mostrar_detalle,
    buscar_cancion,
    mostrar_versiones,
)
from src.dominio.cancion import Cancion
from src.dominio.catalogo import crear_catalogo_desde_texto
from src.dominio.playlist import Playlist
from src.dominio.reproduccion import (
    buscar_cancion_por_id,
    reproducir_cancion,
    deshacer_reproduccion,
    agregar_a_cola,
    reproducir_siguiente,
)
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    ItemNoEncontradoError,
    PilaVaciaError,
    ColaVaciaError,
    ColeccionLlenaError,
    ArchivoInvalidoError,
)
from src.algoritmos.busqueda import busqueda_binaria
from src.algoritmos.ordenamiento import (
    ordenar_seleccion,
    ordenar_insercion,
)
from src.persistencia.texto import cargar_texto, guardar_texto
from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    actualizar_registro,
    posicion_del_id,
    alta_binario,
    baja_binario,
)


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


# Rutas de los archivos
RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data"

RUTA_CANCIONES_TXT = DATA / "canciones.txt"
RUTA_VERSIONES_TXT = DATA / "versiones.txt"
RUTA_CANCIONES_BIN = DATA / "canciones.bin"

ENCABEZADOS_CANCIONES = [
    "id",
    "titulo",
    "artista",
    "album",
    "genero",
    "anio",
    "duracion_seg",
]


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")

    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def mostrar_resultados(titulo, canciones):
    print(f"\n=== {titulo} ===")

    if not canciones:
        print("No se encontraron canciones.")
        return

    for i, cancion in enumerate(canciones, start=1):
        print(f"{i}. {cancion}")


def menu_busqueda_binaria(catalogo):
    texto = input(
        "\nIngresá el título exacto para la búsqueda binaria: "
    ).strip().casefold()

    if not texto:
        print("La búsqueda no puede estar vacía.")
        return

    canciones = list(catalogo)
    ordenar_insercion(
        canciones,
        lambda cancion: cancion.titulo.casefold(),
    )

    print(
        "Se ordenó una copia del catálogo por título "
        "para realizar la búsqueda binaria."
    )

    encontrada = busqueda_binaria(
        canciones,
        texto,
        lambda cancion: cancion.titulo.casefold(),
    )

    if encontrada is None:
        print("No se encontró una canción con ese título.")
    else:
        print(f"Canción encontrada: {encontrada}")


def menu_ordenamiento(catalogo):
    while True:
        print("\n=== Ordenamiento del catálogo (E4) ===")
        print("1. Selección por título")
        print("2. Inserción por artista")
        print("3. Inserción por año")
        print("4. Búsqueda binaria por título")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        canciones = list(catalogo)

        if opcion == "1":
            ordenar_seleccion(
                canciones,
                lambda cancion: cancion.titulo.casefold(),
            )
            mostrar_resultados(
                "Catálogo ordenado por título (selección)",
                canciones,
            )

        elif opcion == "2":
            ordenar_insercion(
                canciones,
                lambda cancion: cancion.artista.casefold(),
            )
            mostrar_resultados(
                "Catálogo ordenado por artista (inserción)",
                canciones,
            )

        elif opcion == "3":
            ordenar_insercion(
                canciones,
                lambda cancion: cancion.anio,
            )
            mostrar_resultados(
                "Catálogo ordenado por año (inserción)",
                canciones,
            )

        elif opcion == "4":
            menu_busqueda_binaria(catalogo)

        else:
            print("Opción inválida.")


def menu_historial(catalogo, historial):
    while True:
        print("\n=== Historial de reproducción ===")
        print("1. Reproducir canción")
        print("2. Deshacer última reproducción")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            try:
                id_cancion = int(input("Ingresá el ID de la canción: "))
                cancion = buscar_cancion_por_id(catalogo, id_cancion)
                reproducir_cancion(cancion, historial)

            except ItemNoEncontradoError:
                print("No se encontró ese elemento.")

            except ValueError:
                print("El ID debe ser un número.")

        elif opcion == "2":
            try:
                deshacer_reproduccion(historial)

            except PilaVaciaError:
                print("No hay acciones en el historial para deshacer.")

        else:
            print("Opción inválida.")


def menu_cola(catalogo, cola, historial):
    while True:
        print("\n=== Cola de reproducción ===")
        print("1. Agregar canción a la cola")
        print("2. Reproducir siguiente")
        print("3. Ver próxima canción")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            try:
                id_cancion = int(input("Ingresá el ID de la canción: "))
                cancion = buscar_cancion_por_id(catalogo, id_cancion)
                agregar_a_cola(cancion, cola)

            except ItemNoEncontradoError:
                print("No se encontró ese elemento.")

            except ValueError:
                print("El ID debe ser un número.")

        elif opcion == "2":
            try:
                reproducir_siguiente(cola, historial)

            except ColaVaciaError:
                print("No hay elementos en la cola.")

        elif opcion == "3":
            try:
                print(f"\nPróxima canción: {cola.ver_frente()}")

            except ColaVaciaError:
                print("No hay elementos en la cola.")

        else:
            print("Opción inválida.")


def guardar_catalogo_texto(catalogo):
    DATA.mkdir(parents=True, exist_ok=True)

    filas = []

    for cancion in catalogo:
        filas.append({
            "id": cancion.id,
            "titulo": cancion.titulo,
            "artista": cancion.artista,
            "album": cancion.album,
            "genero": cancion.genero,
            "anio": cancion.anio,
            "duracion_seg": cancion.duracion_seg,
        })

    relaciones = []

    for cancion in catalogo:
        if cancion.version_de is not None:
            relaciones.append({
                "cancion_id": cancion.id,
                "version_de_id": cancion.version_de,
            })

    guardar_texto(
        RUTA_CANCIONES_TXT,
        filas,
        ENCABEZADOS_CANCIONES,
    )

    guardar_texto(
        RUTA_VERSIONES_TXT,
        relaciones,
        ["cancion_id", "version_de_id"],
    )


def aplicar_relaciones(catalogo):
    canciones_por_id = {
        cancion.id: cancion for cancion in catalogo
    }

    relaciones = cargar_texto(RUTA_VERSIONES_TXT)

    for cancion in catalogo:
        cancion.version_de = None

    for relacion in relaciones:
        id_cancion = int(relacion["cancion_id"])
        id_original = int(relacion["version_de_id"])

        if id_cancion not in canciones_por_id:
            raise ArchivoInvalidoError(
                f"No existe la canción con ID {id_cancion}."
            )

        if id_original not in canciones_por_id:
            raise ArchivoInvalidoError(
                f"No existe la canción original con ID {id_original}."
            )

        canciones_por_id[id_cancion].version_de = id_original


def sincronizar_binario(catalogo):
    """Guarda el estado actual del catálogo en el archivo binario."""

    DATA.mkdir(parents=True, exist_ok=True)
    guardar_binario(RUTA_CANCIONES_BIN, catalogo)


def guardar_cambios(catalogo):
    """Mantiene sincronizados los archivos de texto y binario."""

    guardar_catalogo_texto(catalogo)
    sincronizar_binario(catalogo)


def leer_entero(mensaje):
    return int(input(mensaje).strip())


def siguiente_id(catalogo):
    mayor = 0

    for cancion in catalogo:
        if cancion.id > mayor:
            mayor = cancion.id

    return mayor + 1


def menu_alta(catalogo):
    print("\n=== Alta de canción ===")

    id_cancion = siguiente_id(catalogo)
    print(f"ID asignado: {id_cancion}")

    titulo = input("Título: ").strip()
    artista = input("Artista: ").strip()
    album = input("Álbum: ").strip()
    genero = input("Género: ").strip()

    if not titulo or not artista or not album or not genero:
        print("Todos los campos de texto son obligatorios.")
        return

    try:
        anio = leer_entero("Año: ")
        duracion = leer_entero("Duración en segundos: ")

        if anio <= 0 or duracion <= 0:
            print("El año y la duración deben ser positivos.")
            return

        version_texto = input(
            "ID de la canción original (Enter si no es versión): "
        ).strip()

        version_de = None

        if version_texto:
            version_de = int(version_texto)
            buscar_cancion_por_id(catalogo, version_de)

        cancion = Cancion(
            id_cancion,
            titulo,
            artista,
            album,
            genero,
            anio,
            duracion,
            version_de,
        )

        sincronizar_binario(catalogo)
        alta_binario(RUTA_CANCIONES_BIN, cancion)

        catalogo.insertar_al_final(cancion)
        guardar_catalogo_texto(catalogo)

        print(f"Se agregó correctamente: {cancion}")

    except ItemNoEncontradoError:
        print("No existe la canción original indicada.")

    except ValueError:
        print("El año, la duración y el ID deben ser números.")

    except ArchivoInvalidoError as error:
        print(f"No se pudo completar el alta: {error}")


def menu_modificacion(catalogo):
    print("\n=== Modificación de canción ===")

    try:
        id_cancion = leer_entero("ID de la canción a modificar: ")
        cancion = buscar_cancion_por_id(catalogo, id_cancion)
        posicion = posicion_del_id(catalogo, id_cancion)

        print("Dejá vacío un campo para conservar su valor.")
        print(f"Título actual: {cancion.titulo}")
        titulo = input("Nuevo título: ").strip()

        print(f"Artista actual: {cancion.artista}")
        artista = input("Nuevo artista: ").strip()

        print(f"Álbum actual: {cancion.album}")
        album = input("Nuevo álbum: ").strip()

        print(f"Género actual: {cancion.genero}")
        genero = input("Nuevo género: ").strip()

        print(f"Año actual: {cancion.anio}")
        anio_texto = input("Nuevo año: ").strip()

        print(f"Duración actual: {cancion.duracion_seg}")
        duracion_texto = input("Nueva duración en segundos: ").strip()

        print(f"Versión de ID actual: {cancion.version_de}")
        version_texto = input(
            "Nuevo ID original (Enter conserva, 0 elimina relación): "
        ).strip()

        nuevo_anio = cancion.anio
        nueva_duracion = cancion.duracion_seg
        nueva_version = cancion.version_de

        if anio_texto:
            nuevo_anio = int(anio_texto)

        if duracion_texto:
            nueva_duracion = int(duracion_texto)

        if version_texto:
            nueva_version = int(version_texto)

            if nueva_version == 0:
                nueva_version = None
            else:
                if nueva_version == id_cancion:
                    print("Una canción no puede ser versión de sí misma.")
                    return

                buscar_cancion_por_id(catalogo, nueva_version)

        if nuevo_anio <= 0 or nueva_duracion <= 0:
            print("El año y la duración deben ser positivos.")
            return

        sincronizar_binario(catalogo)

        if titulo:
            cancion.titulo = titulo

        if artista:
            cancion.artista = artista

        if album:
            cancion.album = album

        if genero:
            cancion.genero = genero

        cancion.anio = nuevo_anio
        cancion.duracion_seg = nueva_duracion
        cancion.version_de = nueva_version

        actualizar_registro(
            RUTA_CANCIONES_BIN,
            posicion,
            cancion,
        )

        guardar_catalogo_texto(catalogo)

        print(f"Se modificó correctamente: {cancion}")

    except ItemNoEncontradoError:
        print("No se encontró la canción indicada.")

    except ValueError:
        print("Los valores numéricos ingresados no son válidos.")

    except ArchivoInvalidoError as error:
        print(f"No se pudo completar la modificación: {error}")


def menu_baja(catalogo, playlist):
    print("\n=== Baja de canción ===")

    try:
        id_cancion = leer_entero("ID de la canción a eliminar: ")
        cancion = buscar_cancion_por_id(catalogo, id_cancion)
        posicion = posicion_del_id(catalogo, id_cancion)

        confirmar = input(
            f"¿Seguro que querés eliminar '{cancion.titulo}'? (s/n): "
        ).strip().lower()

        if confirmar != "s":
            print("Operación cancelada.")
            return

        sincronizar_binario(catalogo)
        baja_binario(RUTA_CANCIONES_BIN, posicion)

        for otra in catalogo:
            if otra.version_de == id_cancion:
                otra.version_de = None

        catalogo.eliminar(cancion)

        if cancion in playlist.mostrar():
            playlist.eliminar(cancion)

        guardar_catalogo_texto(catalogo)

        print(f"Se eliminó correctamente: {cancion}")

    except ItemNoEncontradoError:
        print("No se encontró la canción indicada.")

    except ValueError:
        print("El ID debe ser un número.")

    except ArchivoInvalidoError as error:
        print(f"No se pudo completar la baja: {error}")


def menu_abm(catalogo, playlist):
    while True:
        print("\n=== Administración del catálogo ===")
        print("1. Alta de canción")
        print("2. Modificar canción")
        print("3. Baja de canción")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            menu_alta(catalogo)

        elif opcion == "2":
            menu_modificacion(catalogo)

        elif opcion == "3":
            menu_baja(catalogo, playlist)

        else:
            print("Opción inválida.")


def menu_playlist(catalogo, playlist):
    while True:
        print("\n=== Playlist principal ===")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Mostrar playlist")
        print("4. Ver cantidad de canciones")
        print("5. Administrar catálogo (ABM)")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            try:
                id_cancion = int(input("Ingresá el ID de la canción: "))
                cancion = buscar_cancion_por_id(catalogo, id_cancion)
                playlist.agregar(cancion)
                print(f"\nAgregada a la playlist: {cancion}")

            except ItemNoEncontradoError:
                print("No se encontró ese elemento.")

            except ColeccionLlenaError:
                print(
                    "El equipo está lleno (máximo 6). "
                    "No se puede agregar más."
                )

            except ValueError:
                print("El ID debe ser un número.")

        elif opcion == "2":
            try:
                id_cancion = int(
                    input("Ingresá el ID de la canción a eliminar: ")
                )
                cancion = buscar_cancion_por_id(catalogo, id_cancion)
                playlist.eliminar(cancion)
                print(f"\nEliminada de la playlist: {cancion}")

            except ItemNoEncontradoError:
                print("No se encontró ese elemento.")

            except ValueError:
                print("El ID debe ser un número.")

        elif opcion == "3":
            if playlist.esta_vacia():
                print("\nLa playlist está vacía.")
            else:
                print("\n=== Playlist principal ===")
                for i, cancion in enumerate(
                    playlist.mostrar(),
                    start=1,
                ):
                    print(f"{i}. {cancion}")

        elif opcion == "4":
            print(f"\nCanciones en la playlist: {playlist.tamanio()}/6")

        elif opcion == "5":
            menu_abm(catalogo, playlist)

        else:
            print("Opción inválida.")


def menu_archivos(catalogo):
    while True:
        print("\n=== Persistencia de archivos ===")
        print("1. Cargar catálogo desde texto")
        print("2. Guardar catálogo en texto")
        print("3. Guardar catálogo en binario")
        print("4. Cargar catálogo desde binario")
        print("0. Volver")

        opcion = input("> ").strip()

        try:
            if opcion == "0":
                return catalogo

            elif opcion == "1":
                catalogo = crear_catalogo_desde_texto(
                    RUTA_CANCIONES_TXT,
                    RUTA_VERSIONES_TXT,
                )
                sincronizar_binario(catalogo)

                print(
                    f"Se cargaron {len(catalogo)} canciones desde texto."
                )

            elif opcion == "2":
                guardar_catalogo_texto(catalogo)
                print("Catálogo guardado correctamente en texto.")

            elif opcion == "3":
                guardar_cambios(catalogo)
                print("Catálogo guardado correctamente en binario y texto.")

            elif opcion == "4":
                catalogo = cargar_binario(RUTA_CANCIONES_BIN)
                aplicar_relaciones(catalogo)

                print(
                    f"Se cargaron {len(catalogo)} canciones desde binario."
                )

            else:
                print("Opción inválida.")

        except ArchivoInvalidoError as error:
            print(f"Error en los archivos: {error}")

        except (KeyError, ValueError) as error:
            print(f"Error en los datos: {error}")


def main():
    if TEMA not in TEMAS:
        print(
            "Seteá TEMA en src/config.py: "
            "'pokedex', 'recetario' o 'musica'."
        )
        return

    # El programa inicia leyendo el catálogo completo desde los TXT.
    try:
        catalogo = crear_catalogo_desde_texto(
            RUTA_CANCIONES_TXT,
            RUTA_VERSIONES_TXT,
        )
    except ArchivoInvalidoError as error:
        print(f"No se pudo cargar el catálogo inicial: {error}")
        return

    historial = Pila()
    cola = Cola()
    playlist = Playlist()
    opcion = None

    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":
            print("Chau.")

        elif opcion == "1":
            mostrar_catalogo(catalogo)

        elif opcion == "2":
            mostrar_detalle(catalogo)

        elif opcion == "3":
            buscar_cancion(catalogo)

        elif opcion == "4":
            menu_ordenamiento(catalogo)

        elif opcion == "5":
            mostrar_versiones(catalogo)

        elif opcion == "6":
            menu_playlist(catalogo, playlist)

        elif opcion == "7":
            menu_historial(catalogo, historial)

        elif opcion == "8":
            menu_cola(catalogo, cola, historial)

        elif opcion == "9":
            catalogo = menu_archivos(catalogo)

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
