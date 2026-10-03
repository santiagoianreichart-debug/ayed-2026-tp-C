from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError


class Playlist:
    """Colección principal de canciones basada en ListaEnlazada."""

    CAPACIDAD_MAXIMA = 6

    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        if self.esta_llena():
            raise ColeccionLlenaError(
                "La playlist está llena (máximo 6). No se puede agregar más."
            )

        self._canciones.insertar_al_final(cancion)

    def eliminar(self, cancion):
        self._canciones.eliminar(cancion)

    def esta_vacia(self):
        return self._canciones.esta_vacia()

    def esta_llena(self):
        return self._canciones.tamanio() >= self.CAPACIDAD_MAXIMA

    def tamanio(self):
        return self._canciones.tamanio()

    def mostrar(self):
        return self._canciones