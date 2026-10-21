
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
    inicio = perf_counter()

    for _ in range(repeticiones):
        funcion()

    fin = perf_counter()
    return (fin - inicio) / repeticiones


def medir_tamano(nombre, canciones):
    n = len(canciones)
    clave_titulo = lambda cancion: cancion.titulo.casefold()

    # Preparar una lista ordenada para la búsqueda binaria.
    ordenadas = list(canciones)
    ordenar_insercion(ordenadas, clave_titulo)

    # Búsquedas: se mide el algoritmo, no la preparación de datos.
    tiempo_lineal = medir_promedio(
        lambda: busqueda_lineal(
            canciones,
            CLAVE_INEXISTENTE,
            clave_titulo,
        ),
        REPETICIONES_BUSQUEDA,
    )

    tiempo_binaria = medir_promedio(
        lambda: busqueda_binaria(
            ordenadas,
            CLAVE_INEXISTENTE,
            clave_titulo,
        ),
        REPETICIONES_BUSQUEDA,
    )

    # Ordenamientos: cada repetición crea una copia nueva.
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

    print(f"\n{nombre}: n = {n}")
    print(f"Búsqueda lineal:    {tiempo_lineal:.8f} segundos")
    print(f"Búsqueda binaria:   {tiempo_binaria:.8f} segundos")
    print(f"Ordenamiento selección: {tiempo_seleccion:.8f} segundos")
    print(f"Ordenamiento inserción: {tiempo_insercion:.8f} segundos")


def main():
    catalogo = crear_catalogo()
    canciones = list(catalogo)

    print("=== Mediciones de algoritmos E4 ===")
    print("Tiempos promedio por operación.")
    print("Las búsquedas usan una clave inexistente para recorrer")
    print("toda la colección en la búsqueda lineal.")

    medir_tamano("Catálogo original", canciones)
    medir_tamano("Catálogo ampliado", canciones * 10)


if __name__ == "__main__":
    main()
