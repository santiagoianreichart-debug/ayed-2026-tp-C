def busqueda_lineal(coleccion, clave, obtener_clave):
    """Devuelve el elemento cuya clave es igual a 'clave', o None si no existe. """
    for elemento in coleccion: 
        if obtener_clave is None: 
            if elemento == clave: 
                return elemento 
        elif obtener_clave(elemento) == clave: 
            return elemento 
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""
    """Búsqueda binaria. REQUIERE que la colección esté ordenada por esa clave."""     
    izq = 0    
    der = len(coleccion) - 1 
    while izq <= der:         
        medio = (izq + der) // 2         
        valor = obtener_clave(coleccion[medio]) 
        if valor == clave: 
            return coleccion[medio] 
        elif valor < clave:             
            izq = medio + 1       # la clave está en la mitad derecha 
        else:             
            der = medio - 1       
    return None
