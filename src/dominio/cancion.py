class Cancion:
    def __init__(
        self,
        id,
        titulo,
        artista,
        album,
        genero,
        anio,
        duracion_seg,
        version_de=None,
    ):
        self.id = int(id)
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = int(anio)
        self.duracion_seg = int(duracion_seg)
        self.version_de = version_de

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.anio})"