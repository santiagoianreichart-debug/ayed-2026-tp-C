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

