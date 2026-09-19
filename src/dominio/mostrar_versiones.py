from src.dominio.listar import mostrar_catalogo
from src.dominio.recursion import listar_versiones_recursivas


def mostrar_versiones(catalogo):
    mostrar_catalogo(catalogo)

    opcion_cancion = input("\nElegí el número de la canción original: ").strip()

    if not opcion_cancion.isdigit():
        print("Ingresá un número válido.")
        return

    indice = int(opcion_cancion) - 1

    if indice < 0 or indice >= len(catalogo):
        print("Número de canción inválido.")
        return

    cancion = catalogo[indice]
    versiones = listar_versiones_recursivas(catalogo, cancion.id)

    print(f"\n=== Versiones de {cancion.titulo} ===")

    if not versiones:
        print("No se encontraron versiones.")
    else:
        for version in versiones:
            print(f"- {version}")