from time import perf_counter

from src.dominio.catalogo import crear_catalogo
from src.algoritmos.busqueda import (
    busqueda_lineal,
    busqueda_binaria,
)
from src.algoritmos.ordenamiento import (
    ordenar_seleccion,
    ordenar_insercion,
)


REPETICIONES_BUSQUEDA = 5000
REPETICIONES_ORDENAMIENTO = 50
CLAVE_INEXISTENTE = "zzz_no_existe"


def medir_promedio(funcion, repeticiones):
    """Devuelve el tiempo promedio por operación, en segundos."""
    inicio = perf_counter()

    for _ in range(repeticiones):
        funcion()

    fin = perf_counter()
    return (fin - inicio) / repeticiones


def medir_tamano(nombre, canciones):
    n = len(canciones)
    clave_titulo = lambda cancion: cancion.titulo.casefold()

    # Preparar una colección ordenada para la búsqueda binaria.
    ordenadas = list(canciones)
    ordenar_insercion(ordenadas, clave_titulo)

    # Elegir un título existente para la búsqueda exitosa.
    clave_existente = canciones[n // 2].titulo.casefold()

    print(f"\n{nombre}: n = {n}")

    # Búsqueda lineal exitosa.
    tiempo_lineal_exito = medir_promedio(
        lambda: busqueda_lineal(
            canciones,
            clave_existente,
            clave_titulo,
        ),
        REPETICIONES_BUSQUEDA,
    )

    # Búsqueda lineal fallida: recorre toda la colección.
    tiempo_lineal_fallo = medir_promedio(
        lambda: busqueda_lineal(
            canciones,
            CLAVE_INEXISTENTE,
            clave_titulo,
        ),
        REPETICIONES_BUSQUEDA,
    )

    # Búsqueda binaria exitosa.
    tiempo_binaria_exito = medir_promedio(
        lambda: busqueda_binaria(
            ordenadas,
            clave_existente,
            clave_titulo,
        ),
        REPETICIONES_BUSQUEDA,
    )

    # Búsqueda binaria fallida.
    tiempo_binaria_fallo = medir_promedio(
        lambda: busqueda_binaria(
            ordenadas,
            CLAVE_INEXISTENTE,
            clave_titulo,
        ),
        REPETICIONES_BUSQUEDA,
    )

    print("Búsquedas (tiempo promedio por operación):")
    print(f"  Lineal exitosa:   {tiempo_lineal_exito:.8f} segundos")
    print(f"  Lineal fallida:   {tiempo_lineal_fallo:.8f} segundos")
    print(f"  Binaria exitosa:  {tiempo_binaria_exito:.8f} segundos")
    print(f"  Binaria fallida:  {tiempo_binaria_fallo:.8f} segundos")

    # Cada ordenamiento recibe una copia nueva.
    tiempo_seleccion = medir_promedio(
        lambda: ordenar_seleccion(
            list(canciones),
            clave_titulo,
        ),
        REPETICIONES_ORDENAMIENTO,
    )

    tiempo_insercion = medir_promedio(
        lambda: ordenar_insercion(
            list(canciones),
            clave_titulo,
        ),
        REPETICIONES_ORDENAMIENTO,
    )

    print("Ordenamientos (tiempo promedio por operación):")
    print(f"  Selección:        {tiempo_seleccion:.8f} segundos")
    print(f"  Inserción:        {tiempo_insercion:.8f} segundos")


def main():
    catalogo = crear_catalogo()
    canciones = list(catalogo)

    print("=== Mediciones de algoritmos E4 ===")
    print("Se usa time.perf_counter() y se informa el promedio.")
    print("La búsqueda binaria utiliza una colección ordenada.")
    print("Las búsquedas fallidas utilizan una clave inexistente.")
    print("Los ordenamientos reciben una copia nueva en cada repetición.")

    medir_tamano("Catálogo original", canciones)
    medir_tamano("Catálogo ampliado x10", canciones * 10)
    medir_tamano("Catálogo ampliado x100", canciones * 100)


if __name__ == "__main__":
    main()