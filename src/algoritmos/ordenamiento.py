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

def busqueda_ternaria(coleccion, clave, obtener_clave):
    """
    Busca 'clave' mediante búsqueda ternaria.
    La colección debe estar ordenada según obtener_clave.
    Devuelve el elemento encontrado o None.
    """
    izquierda = 0
    derecha = len(coleccion) - 1

    while izquierda <= derecha:

        tercio1 = izquierda + (derecha - izquierda) // 3
        tercio2 = derecha - (derecha - izquierda) // 3

        if obtener_clave(coleccion[tercio1]) == clave:
            return coleccion[tercio1]

        if obtener_clave(coleccion[tercio2]) == clave:
            return coleccion[tercio2]

        if clave < obtener_clave(coleccion[tercio1]):
            derecha = tercio1 - 1

        elif clave > obtener_clave(coleccion[tercio2]):
            izquierda = tercio2 + 1

        else:
            izquierda = tercio1 + 1
            derecha = tercio2 - 1

    return None