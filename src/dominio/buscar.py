
from src.algoritmos.busqueda import busqueda_lineal


def contiene_texto(texto, clave):
    """Comprueba manualmente si texto aparece dentro de clave."""
    if len(texto) > len(clave):
        return False

    for inicio in range(len(clave) - len(texto) + 1):
        coincide = True

        for posicion in range(len(texto)):
            if texto[posicion] != clave[inicio + posicion]:
                coincide = False
                break

        if coincide:
            return True

    return False


def buscar_cancion(catalogo):
    texto = input("\nIngresá el título o artista a buscar: ").strip().lower()

    if not texto:
        print("La búsqueda no puede estar vacía.")
        return

    encontrados = []

    for cancion in catalogo:
        coincidencia_titulo = contiene_texto(
            texto, cancion.titulo.lower()
        )
        coincidencia_artista = contiene_texto(
            texto, cancion.artista.lower()
        )

        if coincidencia_titulo or coincidencia_artista:
            encontrados.append(cancion)

    if not encontrados:
        print("No se encontraron canciones.")
        return

    print("\n=== Resultados de búsqueda ===")

    for i, cancion in enumerate(encontrados, start=1):
        print(f"{i}. {cancion}")

    # Se utiliza también el algoritmo propio para localizar
    # la primera canción que coincide con el texto buscado.
    primera = busqueda_lineal(
        encontrados,
        texto,
        lambda cancion: cancion.titulo.lower()
        if contiene_texto(texto, cancion.titulo.lower())
        else cancion.artista.lower()
    )

    if primera is not None:
        print(f"\nPrimera coincidencia localizada: {primera}")
