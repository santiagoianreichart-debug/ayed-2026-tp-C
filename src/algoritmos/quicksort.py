def ordenar_quicksort(coleccion, obtener_clave):
    """Ordena una colección usando el algoritmo Quicksort."""
    _quicksort(coleccion, 0, len(coleccion) - 1, obtener_clave)


def _quicksort(coleccion, inicio, fin, obtener_clave):
    if inicio >= fin:
        return

    izquierda = inicio
    derecha = fin

    medio = (inicio + fin) // 2
    pivote = obtener_clave(coleccion[medio])

    while izquierda <= derecha:
        while obtener_clave(coleccion[izquierda]) < pivote:
            izquierda += 1

        while obtener_clave(coleccion[derecha]) > pivote:
            derecha -= 1

        if izquierda <= derecha:
            coleccion[izquierda], coleccion[derecha] = (
                coleccion[derecha],
                coleccion[izquierda],
            )
            izquierda += 1
            derecha -= 1

    if inicio < derecha:
        _quicksort(coleccion, inicio, derecha, obtener_clave)

    if izquierda < fin:
        _quicksort(coleccion, izquierda, fin, obtener_clave)