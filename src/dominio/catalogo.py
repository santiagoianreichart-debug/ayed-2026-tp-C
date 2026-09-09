import csv
from pathlib import Path

from src.dominio.cancion import Cancion


def crear_catalogo():
    canciones = [
        Cancion(1, "La Flaca", "Jarabe de Palo", "La Flaca", "Pop/Rock en español", 1996, 240),
        Cancion(2, "Sin Documentos", "Los Rodríguez", "Sin Documentos", "Rock/Pop Rock", 1993, 260),
        Cancion(3, "Muriendo de Plena", "Rubén Rada", "Quién va a cantar", "Salsa/Tropical", 2000, 210),
        Cancion(4, "Microdancing", "Babasónicos", "Mucho", "Rock alternativo/Indie", 2008, 200),
        Cancion(5, "11 y 6", "Fito Páez", "Giros", "Trova rosarina/Pop Rock", 1985, 230),
        Cancion(6, "Just What I Needed", "The Cars", "The Cars", "Rock", 1978, 236),
        Cancion(7, "Sultans of Swing", "Dire Straits", "Dire Straits", "Rock", 1978, 348),
        Cancion(8, "Have You Ever Seen the Rain?", "Creedence Clearwater Revival", "Pendulum", "Rock", 1970, 160),
        Cancion(9, "Beat It", "Michael Jackson", "Thriller", "Pop/Rock", 1982, 258),
        Cancion(10, "Enjoy the Silence", "Depeche Mode", "Violator", "Synth-pop", 1990, 374),
        Cancion(11, "Boulevard of Broken Dreams", "Green Day", "American Idiot", "Rock", 2004, 262),
        Cancion(12, "Africa", "Toto", "Toto IV", "Rock", 1982, 295),
        Cancion(13, "Ride", "Twenty One Pilots", "Blurryface", "Alternative", 2015, 214),
        Cancion(14, "You Talk", "Babyshambles", "Shotter's Nation", "Indie Rock", 2007, 190),
        Cancion(15, "The Adults Are Talking", "The Strokes", "The New Abnormal", "Indie Rock", 2020, 309),
    ]

    return canciones

#def crear_catalogo():
    ruta = Path(__file__).resolve().parents[2] / "data" / "canciones.csv"

    catalogo = []

    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            cancion = Cancion(
                fila["id"],
                fila["titulo"],
                fila["artista"],
                fila["album"],
                fila["genero"],
                fila["anio"],
                fila["duracion_seg"],
            )

            catalogo.append(cancion)

    return catalogo

