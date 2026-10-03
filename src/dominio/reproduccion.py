from src.excepciones import ItemNoEncontradoError
from src.tads.pila import Pila
from src.tads.cola import Cola


def buscar_cancion_por_id(catalogo, id_cancion):
    for cancion in catalogo:
        if cancion.id == id_cancion:
            return cancion

    raise ItemNoEncontradoError("No se encontró ese elemento.")


def reproducir_cancion(cancion, historial):
    historial.apilar(cancion)
    print(f"\nReproduciendo: {cancion}")


def deshacer_reproduccion(historial):
    cancion = historial.desapilar()
    print(f"\nDeshaciendo última reproducción: {cancion}")

    if not historial.esta_vacia():
        print(f"Volviste a: {historial.ver_tope()}")
    else:
        print("No hay una canción anterior.")


def agregar_a_cola(cancion, cola):
    cola.encolar(cancion)
    print(f"\nAgregada a la cola: {cancion}")


def reproducir_siguiente(cola, historial):
    cancion = cola.desencolar()
    historial.apilar(cancion)
    print(f"\nReproduciendo desde la cola: {cancion}")