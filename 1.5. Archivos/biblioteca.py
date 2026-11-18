from datetime import date

ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"

LIBROS_INICIALES = [
    {
        "codigo": 1,
        "titulo": "Python para todos",
        "autor": "Charles Severance",
        "estado": "Disponible",
    },
    {
        "codigo": 2,
        "titulo": "Aprende Java",
        "autor": "Ana Torres",
        "estado": "Disponible",
    },
    {
        "codigo": 3,
        "titulo": "Bases de datos",
        "autor": "Carlos Mora",
        "estado": "Disponible",
    },
]


def guardar_libros(libros):
    with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as archivo:
        for libro in libros:
            linea = f"{libro['codigo']},{libro['titulo']},"
            linea += f"{libro['autor']},{libro['estado']}\n"
            archivo.write(linea)


def cargar_libros():
    libros = []
    try:
        with open(ARCHIVO_LIBROS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                libros.append(
                    {
                        "codigo": int(datos[0]),
                        "titulo": datos[1],
                        "autor": datos[2],
                        "estado": datos[3],
                    }
                )
    except FileNotFoundError:
        print("No se encontró libros.txt: se usan los libros iniciales.")
        for libro in LIBROS_INICIALES:
            libros.append(dict(libro))
        guardar_libros(libros)
    return libros


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Error: debe escribir un número entero.")


libros = cargar_libros()
# prestamos = cargar_prestamos()
opcion = 0
while opcion != 8:

    print("""
    ===============================================
              BIBLIOTECA DIGITAL TECAZUAY
    ===============================================
    1. Registrar Libro       5. Devolver libro 
    2. Mostrar Libro         6. Mostrar prestamos
    3.  Buscar libro         7. Reporte general
    4. Prestar libro         8. Salir
    """)

    opcion = leer_entero("Elija una opción: ")
    if opcion == 1:
        libros = cargar_libros()
        print("1")
    elif opcion == 2:
        print("2")
    elif opcion == 3:
        print("3")
    elif opcion == 4:
        print("4")
    elif opcion == 5:
        print("5")
    elif opcion == 6:
        print("6")
    elif opcion == 7:
        print("7")
    elif opcion == 8:
        guardar_libros(libros)
        print("guardando")

    else:
        print("Opción no válida: elija un número del 1 al 8.")
