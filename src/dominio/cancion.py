class Cancion:
    def __init__(self, titulo, artista, album, genero, anio):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.anio})"