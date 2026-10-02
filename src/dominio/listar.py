def mostrar_catalogo(catalogo):
    print("\n=== Catálogo de canciones ===")

    for i, cancion in enumerate(catalogo, start=1):
        print(f"{i}. {cancion}")

    #for item in catalogo:     
    #   print(item)