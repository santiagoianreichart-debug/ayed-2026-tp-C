def duracion_total_recursiva(canciones, indice=0):
    if indice == len(canciones):
        return 0

    return canciones[indice].duracion_seg + duracion_total_recursiva(
        canciones, indice + 1
    )