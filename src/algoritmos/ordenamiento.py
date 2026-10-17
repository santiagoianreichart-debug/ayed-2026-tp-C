def ordenar_seleccion(coleccion, obtener_clave):
    """Ordenamiento por selección. Devuelve una nueva secuencia, 
    no usa sorted."""
    """Ordena la colección in place por selección (ascendente).""" 
    n = len(coleccion) 
    for i in range(n - 1):         
        pos_min = i 
        for j in range(i + 1, n): 
            if obtener_clave(coleccion[j]) < obtener_clave(coleccion[pos_min]):                 
                pos_min = j         
                coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i] 
    return coleccion


def ordenar_insercion(coleccion, obtener_clave):
    """Ordenamiento por inserción. Devuelve una nueva secuencia, 
    no usa sorted."""
    """Ordena la colección in place por inserción (ascendente).""" 
    for i in range(1, len(coleccion)):         
        actual = coleccion[i]         
        j = i - 1 
        while j >= 0 and obtener_clave(coleccion[j]) > obtener_clave(actual):             
            coleccion[j + 1] = coleccion[j]               
            j -= 1         
        coleccion[j + 1] = actual               
    return coleccion 

def ordenar_por_anio_desc(coleccion, obtener_clave):
    """ Ordena la colección por año de mayor a menor
    según la clave indicada.
    """
    for elemento in coleccion:
        if not isinstance(obtener_clave(elemento), (int)):
            raise TypeError(
                "El año debe ser en números enteros."
            )

    n = len(coleccion)

    for i in range(n - 1):
        pos_max = i

        for j in range(i + 1, n):
            if obtener_clave(coleccion[j]) > obtener_clave(coleccion[pos_max]):
                pos_max = j

        coleccion[i], coleccion[pos_max] = (
            coleccion[pos_max],
            coleccion[i]
        )

    return coleccion