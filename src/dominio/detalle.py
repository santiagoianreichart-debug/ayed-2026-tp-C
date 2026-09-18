from src.dominio.listar import mostrar_catalogo


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
    print(f"ID: {cancion.id}")
    print(f"Título: {cancion.titulo}")
    print(f"Artista: {cancion.artista}")
    print(f"Álbum: {cancion.album}")
    print(f"Género: {cancion.genero}")
    print(f"Año: {cancion.anio}")
    print(f"Duración (segundos): {cancion.duracion_seg}")