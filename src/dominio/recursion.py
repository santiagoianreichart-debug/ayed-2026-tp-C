def listar_versiones_recursivas(canciones, id_cancion, indice=0):
    if indice == len(canciones):
        return []

    cancion = canciones[indice]

    if cancion.version_de == id_cancion:
        versiones = [cancion]
        versiones += listar_versiones_recursivas(canciones, cancion.id)
        versiones += listar_versiones_recursivas(canciones, id_cancion, indice + 1)
        return versiones

    return listar_versiones_recursivas(canciones, id_cancion, indice + 1)


