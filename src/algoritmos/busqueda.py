
def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """Devuelve la primera coincidencia o None si no existe."""
    for elemento in coleccion:
        if obtener_clave is None:
            coincide = elemento == clave
        else:
            coincide = obtener_clave(elemento) == clave

        if coincide:
            return elemento

    return None


def buscar_todos_lineal(coleccion, coincide):
    """Devuelve todos los elementos que cumplen una condición."""
    resultados = []

    for elemento in coleccion:
        if coincide(elemento):
            resultados.append(elemento)

    return resultados


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """Busca una clave en una colección ordenada ascendentemente."""
    izq = 0
    der = len(coleccion_ordenada) - 1

    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion_ordenada[medio])

        if valor == clave:
            return coleccion_ordenada[medio]
        elif valor < clave:
            izq = medio + 1
        else:
            der = medio - 1

    return None
