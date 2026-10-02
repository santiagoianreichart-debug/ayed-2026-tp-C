from lista_enlazada import ListaEnlazada
from excepciones import ColaVaciaError

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()
        #raise NotImplementedError

    def encolar(self, dato):
        self._items.insertar_al_final(dato)
        #raise NotImplementedError

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        frente = self._items._cabeza.dato
        self._items.eliminar(frente)
        return frente
        #raise NotImplementedError

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self._items._cabeza.dato
        #raise NotImplementedError

    def esta_vacia(self):
        return self._items.esta_vacia()
        #raise NotImplementedError
