
def ordenar_seleccion(coleccion, obtener_clave):
    """Ordena ascendentemente por selección, modificando la lista."""
    n = len(coleccion)

    for i in range(n - 1):
        pos_min = i

        for j in range(i + 1, n):
            if obtener_clave(coleccion[j]) < obtener_clave(
                coleccion[pos_min]
            ):
                pos_min = j

        # El intercambio se hace al terminar de buscar el mínimo.
        coleccion[i], coleccion[pos_min] = (
            coleccion[pos_min],
            coleccion[i]
        )

    return coleccion


def ordenar_insercion(coleccion, obtener_clave):
    """Ordena ascendentemente por inserción, modificando la lista."""
    for i in range(1, len(coleccion)):
        actual = coleccion[i]
        j = i - 1

        while (
            j >= 0
            and obtener_clave(coleccion[j]) > obtener_clave(actual)
        ):
            coleccion[j + 1] = coleccion[j]
            j -= 1

        coleccion[j + 1] = actual

    return coleccion
