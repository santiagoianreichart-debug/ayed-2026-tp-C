import csv
from pathlib import Path

from src.dominio.cancion import Cancion


def crear_catalogo():
    ruta = Path(__file__).resolve().parents[2] / "data" / "canciones.csv"

    catalogo = []

    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            cancion = Cancion(
                fila["titulo"],
                fila["artista"],
                fila["album"],
                fila["genero"],
                int(fila["anio"]),
            )

            catalogo.append(cancion)

    return catalogo