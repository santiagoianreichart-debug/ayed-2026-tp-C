from src.dominio.playlist import Playlist
from src.config import TEMA
from src.dominio import (
    crear_catalogo,
    mostrar_catalogo,
    mostrar_detalle,
    buscar_cancion,
    mostrar_versiones,
    pendiente
)

from src.dominio.reproduccion import (
    buscar_cancion_por_id,
    reproducir_cancion,
    deshacer_reproduccion,
    agregar_a_cola,
    reproducir_siguiente
)

from src.tads.pila import Pila
from src.tads.cola import Cola

from src.excepciones import (
    ItemNoEncontradoError,
    PilaVaciaError,
    ColaVaciaError,
    ColeccionLlenaError
)


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")

    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


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


def menu_playlist(catalogo, playlist):
    while True:
        print("\n=== Playlist principal ===")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Mostrar playlist")
        print("4. Ver cantidad de canciones")
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
                print("La playlist está llena (máximo 6). No se puede agregar más.")

            except ValueError:
                print("El ID debe ser un número.")

        elif opcion == "2":
            try:
                id_cancion = int(input("Ingresá el ID de la canción a eliminar: "))
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
                for i, cancion in enumerate(playlist.mostrar(), start=1):
                    print(f"{i}. {cancion}")

        elif opcion == "4":
            print(f"\nCanciones en la playlist: {playlist.tamanio()}/6")

        else:
            print("Opción inválida.")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    catalogo = crear_catalogo()

    historial = Pila()
    cola = Cola()
    playlist = Playlist()
    opcion = None

    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":
            print("Se ha cerrado la Biblioteca Musical. Tenga un buen día.")

        elif opcion == "1":
            mostrar_catalogo(catalogo)

        elif opcion == "2":
            mostrar_detalle(catalogo)

        elif opcion == "3":
            buscar_cancion(catalogo)

        elif opcion == "4":
            pendiente()

        elif opcion == "5":
            mostrar_versiones(catalogo)

        elif opcion == "6":
            menu_playlist(catalogo, playlist)

        elif opcion == "7":
            menu_historial(catalogo, historial)

        elif opcion == "8":
            menu_cola(catalogo, cola, historial)

        elif opcion == "9":
            pendiente()

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()