from src.dominio.cancion import Cancion
from src.tads.lista_enlazada import ListaEnlazada
from src.persistencia.texto import cargar_texto
from src.excepciones import ArchivoInvalidoError

def crear_catalogo():
    catalogo = ListaEnlazada()

    catalogo.insertar_al_final(
        Cancion(1, "La Flaca", "Jarabe de Palo", "La Flaca", "Pop/Rock en español", 1996, 240)
    )
    catalogo.insertar_al_final(
        Cancion(2, "Sin Documentos", "Los Rodríguez", "Sin Documentos", "Rock/Pop Rock", 1993, 260)
    )
    catalogo.insertar_al_final(
        Cancion(3, "Muriendo de Plena", "Rubén Rada", "Quién va a cantar", "Salsa/Tropical", 2000, 210)
    )
    catalogo.insertar_al_final(
        Cancion(4, "Microdancing", "Babasónicos", "Mucho", "Rock alternativo/Indie", 2008, 200)
    )
    catalogo.insertar_al_final(
        Cancion(5, "11 y 6", "Fito Páez", "Giros", "Trova rosarina/Pop Rock", 1985, 230)
    )
    catalogo.insertar_al_final(
        Cancion(18, "11 y 6 (En Vivo)", "Fito Páez", "No Sé Si Es Baires o Madrid", "Trova rosarina/Pop Rock", 2008, 238, version_de=5)
    )
    catalogo.insertar_al_final(
        Cancion(6, "Just What I Needed", "The Cars", "The Cars", "Rock", 1978, 236)
    )
    catalogo.insertar_al_final(
        Cancion(7, "Sultans of Swing", "Dire Straits", "Dire Straits", "Rock", 1978, 348)
    )
    catalogo.insertar_al_final(
        Cancion(8, "Have You Ever Seen the Rain?", "Creedence Clearwater Revival", "Pendulum", "Rock", 1970, 160)
    )
    catalogo.insertar_al_final(
        Cancion(16, "Have You Ever Seen the Rain?", "Joan Jett", "I Love Rock 'n Roll", "Rock", 1981, 174, version_de=8)
    )
    catalogo.insertar_al_final(
        Cancion(17, "Have You Ever Seen the Rain?", "Spin Doctors", "If the River Was Whiskey", "Rock", 1991, 190, version_de=8)
    )
    catalogo.insertar_al_final(
        Cancion(9, "Beat It", "Michael Jackson", "Thriller", "Pop/Rock", 1982, 258)
    )
    catalogo.insertar_al_final(
        Cancion(10, "Enjoy the Silence", "Depeche Mode", "Violator", "Synth-pop", 1990, 374)
    )
    catalogo.insertar_al_final(
        Cancion(11, "Boulevard of Broken Dreams", "Green Day", "American Idiot", "Rock", 2004, 262)
    )
    catalogo.insertar_al_final(
        Cancion(12, "Africa", "Toto", "Toto IV", "Rock", 1982, 295)
    )
    catalogo.insertar_al_final(
        Cancion(19, "Africa", "Weezer", "Weezer (Teal Album)", "Rock", 2019, 241, version_de=12)
    )
    catalogo.insertar_al_final(
        Cancion(13, "Ride", "Twenty One Pilots", "Blurryface", "Alternative", 2015, 214)
    )
    catalogo.insertar_al_final(
        Cancion(14, "You Talk", "Babyshambles", "Shotter's Nation", "Indie Rock", 2007, 190)
    )
    catalogo.insertar_al_final(
        Cancion(15, "The Adults Are Talking", "The Strokes", "The New Abnormal", "Indie Rock", 2020, 309)
    )

    return catalogo
def crear_catalogo_desde_texto(ruta_canciones, ruta_versiones):
    """Construye el catálogo musical leyendo archivos de texto."""

    filas = cargar_texto(ruta_canciones)
    relaciones = cargar_texto(ruta_versiones)

    catalogo = ListaEnlazada()
    canciones_por_id = {}

    try:
        for fila in filas:
            cancion = Cancion(
                int(fila["id"]),
                fila["titulo"],
                fila["artista"],
                fila["album"],
                fila["genero"],
                int(fila["anio"]),
                int(fila["duracion_seg"]),
            )

            if cancion.id in canciones_por_id:
                raise ArchivoInvalidoError(
                    f"El ID {cancion.id} está repetido."
                )

            canciones_por_id[cancion.id] = cancion
            catalogo.insertar_al_final(cancion)

        for relacion in relaciones:
            id_cancion = int(relacion["cancion_id"])
            id_original = int(relacion["version_de_id"])

            if id_cancion not in canciones_por_id:
                raise ArchivoInvalidoError(
                    f"No existe la canción con ID {id_cancion}."
                )

            if id_original not in canciones_por_id:
                raise ArchivoInvalidoError(
                    f"No existe la canción original con ID {id_original}."
                )

            canciones_por_id[id_cancion].version_de = id_original

    except (KeyError, ValueError) as error:
        raise ArchivoInvalidoError(
            f"Los datos del catálogo tienen un formato incorrecto: {error}"
        )

    return catalogo