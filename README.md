# TP integrador — AyED C2 2026

Repositorio del grupo. Partir de este esqueleto. No borrar la estructura de `src/` ni de `docs/`.

## Integrantes

| Nombre | Mail | GitHub |
| --- | --- | --- |
| Nahuel Armesto | armestonahuel2@hotmail.com | https://github.com/Morfeo4264 |
| Juan Pablo Machi | juanpablomacchi0@gmail.com | https://github.com/juanpablomacchi0-ui |
| Santiago Reichart | santiagoianreichart@gmail.com | https://github.com/santiagoianreichart-debug |

**Tema elegido:** Biblioteca musical 

## Que hace
El programa desde la interfaz permite:
- Listar el catálogo de canciones.
- Ver el detalle de una canción.
- Buscar canciones (búsqueda lineal y búsqueda binaria).
- Ordenar el catálogo (selección, inserción, Quick Sort y QuickSort Media de 3).
- Listar las versiones de una canción mediante recursión.
- ABM del catálogo: alta, baja y modificación de canciones.
- Playlist (colección principal) con un tope de 6 canciones.
- Historial de reproducciones (pila).
- Cola de reproducción (cola).
- Persistencia en archivos de texto (`.txt`) y en archivo binario con `struct`.

## Limitaciones

- El alta no valida canciones duplicadas: se puede cargar la misma canción dos veces con IDs distintos. Si ambas se marcan como versión de la misma canción original, "Listar versiones" las muestra como dos versiones distintas.
- La búsqueda binaria solo es válida con el catálogo ordenado por la clave buscada. Si no lo está, puede devolver "no encontrado" aunque la canción exista.
- La recursión de versiones avanza por índice, así que con catálogos de más de ~1000 canciones supera el límite de recursión de Python.
- Los textos tienen ancho fijo en el binario (título 30, artista 25, álbum 30 y género 12 bytes). Al dar de baja una canción, el historial y la cola pueden seguir mostrándola.

## Cómo ejecutar

Desde la raíz del repo, con Python 3.10 o superior:

```text
python -m src.main
```

En Windows, si `python` no anda: `py -3 -m src.main`.

Solo biblioteca estándar. No hay `requirements.txt` a propósito.

## Entregas

Cada vencimiento se marca con un tag. Ver `GIT.md`.

| Tag | Vence |
| --- | --- |
| `preentrega` (opcional, solo repo) | domingo 30-ago-2026 23:59 |
| `entrega-1` | domingo 06-sep-2026 23:59 |
| `entrega-2` | domingo 20-sep-2026 23:59 |
| `entrega-3` | domingo 04-oct-2026 23:59 |
| `entrega-4` | domingo 01-nov-2026 23:59 |
| `entrega-5` | domingo 15-nov-2026 23:59 |
| `entrega-6` | domingo 22-nov-2026 23:59 |

Defensa oral (reemplaza el 2do parcial): 25 y 27-nov-2026.

La cátedra corrige el **tag**, no el último commit suelto de `main`.

El grupo se avisa por mail a diego.ambrossio@unab.edu.ar **y** angel.bianco@unab.edu.ar. Ver `GIT.md`.
