
def ordenar_seleccion(coleccion, obtener_clave):
    """Ordena ascendentemente por selección, modificando la lista."""
    for i in range(len(coleccion)):
        menor = i

        for j in range(i + 1, len(coleccion)):
            if obtener_clave(coleccion[j]) < obtener_clave(coleccion[menor]):
                menor = j

        coleccion[i], coleccion[menor] = coleccion[menor], coleccion[i]

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

#primer algoritmo adicional
def ordenar_quicksort_con_mediana_de_tres(coleccion, obtener_clave):
    """Ordena ascendentemente con Quick Sort y mediana de tres."""

    def mediana_de_tres(inicio, fin):
        medio = (inicio + fin) // 2

        a = obtener_clave(coleccion[inicio])
        b = obtener_clave(coleccion[medio])
        c = obtener_clave(coleccion[fin])

        if (a <= b <= c) or (c <= b <= a):
            return medio
        elif (b <= a <= c) or (c <= a <= b):
            return inicio
        else:
            return fin

    def quicksort(inicio, fin):
        if inicio >= fin:
            return

        pivote_idx = mediana_de_tres(inicio, fin)

        coleccion[pivote_idx], coleccion[fin] = (
            coleccion[fin],
            coleccion[pivote_idx],
        )

        pivote = obtener_clave(coleccion[fin])
        i = inicio - 1

        for j in range(inicio, fin):
            if obtener_clave(coleccion[j]) <= pivote:
                i += 1
                coleccion[i], coleccion[j] = (
                    coleccion[j],
                    coleccion[i],
                )

        coleccion[i + 1], coleccion[fin] = (
            coleccion[fin],
            coleccion[i + 1],
        )

        pos_pivote = i + 1
        quicksort(inicio, pos_pivote - 1)
        quicksort(pos_pivote + 1, fin)

    quicksort(0, len(coleccion) - 1)
    return coleccion


#segundo algoritmo adicional
 
def ordenar_quicksort(coleccion, obtener_clave):
    """Ordena ascendentemente con Quick Sort, modificando la lista."""
    _quicksort(coleccion, 0, len(coleccion) - 1, obtener_clave)
    return coleccion


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