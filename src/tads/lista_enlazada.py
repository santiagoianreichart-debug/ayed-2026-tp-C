from nodo import Nodo
class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
        self._cabeza = None
        self._tamanio = 0
        #raise NotImplementedError

    def esta_vacia(self):
        return self._cabeza is None
        #raise NotImplementedError

    def tamanio(self):
        return self._tamanio
        #raise NotImplementedError

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        self._tamanio += 1
        #raise NotImplementedError

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1
        #raise NotImplementedError

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError

    def eliminar(self, dato):
        if self.esta_vacia():
            return 
        # Caso 1: es la cabeza 
        if self._cabeza.dato == dato:         
            self._cabeza = self._cabeza.siguiente         
            self._tamanio -= 1 
            return 
        # Caso 2: buscar el nodo anterior     
        actual = self._cabeza 
        while actual.siguiente is not None: 
            if actual.siguiente.dato == dato:             
                actual.siguiente = actual.siguiente.siguiente
                self._tamanio -= 1 
                return         
            actual = actual.siguiente
        #raise NotImplementedError

    def buscar(self, dato):
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None
        #raise NotImplementedError

    def __iter__(self):
        return self._Iterador(self._cabeza)
        #raise NotImplementedError

    class _Iterador:
        def __init__(self, cabeza):
            self._actual = cabeza

        def __iter__(self):
            return self

        def __next__(self):
            if self._actual is None:
                raise StopIteration
            dato = self._actual.dato
            self._actual = self._actual.siguiente
            return dato