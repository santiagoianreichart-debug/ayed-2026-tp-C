from src.config import TEMA
from src.dominio.catalogo import crear_catalogo


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_catalogo(catalogo):
    print("\n=== Catálogo de canciones ===")

    for i, cancion in enumerate(catalogo, start=1):
        print(f"{i}. {cancion}")


def mostrar_detalle(catalogo):
    mostrar_catalogo(catalogo)

    opcion = input("\nElegí el número de una canción: ").strip()

    if not opcion.isdigit():
        print("Ingresá un número válido.")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(catalogo):
        print("Número de canción inválido.")
        return

    cancion = catalogo[indice]

    print("\n=== Detalle de la canción ===")
    print(f"Título: {cancion.titulo}")
    print(f"Artista: {cancion.artista}")
    print(f"Álbum: {cancion.album}")
    print(f"Género: {cancion.genero}")
    print(f"Año: {cancion.anio}")


def buscar_cancion(catalogo):
    texto = input("\nIngresá el título o artista a buscar: ").strip().lower()

    if not texto:
        print("La búsqueda no puede estar vacía.")
        return

    encontrados = []

    for cancion in catalogo:
        if texto in cancion.titulo.lower() or texto in cancion.artista.lower():
            encontrados.append(cancion)

    if not encontrados:
        print("No se encontraron canciones.")
        return

    print("\n=== Resultados de búsqueda ===")

    for i, cancion in enumerate(encontrados, start=1):
        print(f"{i}. {cancion}")


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


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    catalogo = crear_catalogo()

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
        elif opcion in {"4", "5", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()