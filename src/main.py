from src.config import TEMA
from src.dominio import (
    crear_catalogo,
    mostrar_catalogo,
    mostrar_detalle,
    buscar_cancion, 
    mostrar_versiones,
    pendiente
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
        elif opcion == "5":
            mostrar_versiones(catalogo)
        elif opcion in {"4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()