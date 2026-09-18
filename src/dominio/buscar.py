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