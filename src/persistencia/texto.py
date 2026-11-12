
import csv

from src.excepciones import ArchivoInvalidoError


def cargar_texto(ruta):
    """Lee un archivo de texto separado por comas y devuelve una lista de diccionarios."""

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)

            encabezados = next(lector, None)

            if not encabezados:
                raise ArchivoInvalidoError("El archivo está vacío o no tiene encabezados.")

            filas = []

            for numero_linea, valores in enumerate(lector, start=2):
                if not valores:
                    continue

                if len(valores) != len(encabezados):
                    raise ArchivoInvalidoError(
                        f"Cantidad incorrecta de campos en la línea {numero_linea}."
                    )

                fila = dict(zip(encabezados, valores))
                filas.append(fila)

            return filas

    except FileNotFoundError:
        raise ArchivoInvalidoError("No se encontró el archivo indicado.")

    except (UnicodeDecodeError, csv.Error):
        raise ArchivoInvalidoError("El archivo tiene un formato inválido.")


def guardar_texto(ruta, filas, encabezados):
    """Guarda una lista de diccionarios en un archivo de texto separado por comas."""

    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow(encabezados)

            for fila in filas:
                valores = [fila.get(encabezado, "") for encabezado in encabezados]
                escritor.writerow(valores)

    except (OSError, csv.Error):
        raise ArchivoInvalidoError("No se pudo guardar el archivo.")


# Se conservan los nombres anteriores por compatibilidad.
def cargar_csv(ruta):
    return cargar_texto(ruta)


def guardar_csv(ruta, filas, encabezados):
    return guardar_texto(ruta, filas, encabezados)
