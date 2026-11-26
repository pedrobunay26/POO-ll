from datetime import date

ARCHIVO_LIBROS = "Trabajo_grupal/libros.txt"
ARCHIVO_PRESTAMOS = "Trabajo_grupal/prestamos.txt"

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


# -------------------------------------------------------------------------------


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print(f"El texto no puede estar vacio {mensaje}")

        elif "," in texto:
            print(f"El texto no puede llevar comas (,)")

        else:
            return texto


def buscar_por_codigo(libros, codigo):
    for libro in libros:
        if libro["codigo"] == codigo:
            return libro

    return None


# ahora si mi parte
def registrar_libro(libros):
    titulo = leer_texto("titulo: ")
    autor = leer_texto("Autor: ")

    mayor = 0
    for libro in libros:
        if libro["codigo"] > mayor:
            mayor = libro["codigo"]

    nuevo = {
        "codigo": mayor + 1,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible",
    }
    libros.append(nuevo)
    guardar_libros(libros)
    print(f"Libro registrado con el codigo {nuevo['codigo']}.")
    return nuevo


# b. mostrar libros
def mostrar_libros(libros):

    print(f"{'Codigo':<8}{'Titulo':<30}{'Autor':<22}{'estado':<12}")
    print("-" * 72)
    cantidad = 0
    for libro in libros:
        print(
            f"{libro['codigo']:<8}{libro['titulo']:<30}{libro['autor']:<22}{libro['estado']:<12}"
        )
        cantidad += 1
    return cantidad


# c- buscar llibro
def buscar_libro(libros):
    palabra = leer_texto("Palabra a buscar en el titulo: ").lower()
    encontrados = 0
    for libro in libros:
        if palabra in libro["titulo"].lower():
            print(
                f"{libro['codigo']:<8}{libro['titulo']:<30}{libro['autor']:<22}{libro['estado']:<12}"
            )
            encontrados += 1
    if encontrados == 0:
        print("No se encontro ningun libro con esa palabra ")
    return encontrados


# ya hasta aqui


# --------------------------------------------------------------------------------------
# Mi parte es esta pedrito buñay sjsjsjjsjssjj
def cargar_prestamos():
    prestamos = []
    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                prestamos.append(
                    {
                        "numero": int(datos[0]),
                        "codigo_libro": int(datos[1]),
                        "estudiante": datos[2],
                        "fecha": datos[3],
                        "estado": datos[4],
                    }
                )
    except FileNotFoundError:
        print("No se encontró prestamos.txt: se inicia con una lista vacia.")
    return prestamos


def guardar_prestamos(prestamos):
    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as archivo:
        for prestamo in prestamos:
            linea = f"{prestamo['numero']},{prestamo['codigo_libro']},{prestamo['estudiante']},{prestamo['fecha']},{prestamo['estado']}\n"
            archivo.write(linea)

def prestar_libro(libros, prestamos):
    codigo = leer_entero("Ingrese el codigo del libro: ")
    libro = buscar_por_codigo(libros, codigo)
    if libro is None:
        print("Error: el codigo del libro no existe")
        return False
    if libro["estado"] != "Disponible":
        print("Error: el libro se encuentra prestado")
        return False
    estudiante = leer_texto("Ingrese su nombre: ")
    if prestamos:
        numeros = [prestamo["numero"] for prestamo in prestamos]
        numero = max(numeros) + 1
    else:
        numero = 1
    fecha = str(date.today())
    prestamo = {
        "numero": numero,
        "codigo_libro": codigo,
        "estudiante": estudiante,
        "fecha": fecha,
        "estado": "Activo",
    }
    prestamos.append(prestamo)
    libro["estado"] = "Prestado"
    guardar_libros(libros)
    guardar_prestamos(prestamos)
    print("Prestamo registrado correctamente")
    return True


def devolver_libro(libros, prestamos):
    codigo = leer_entero("Ingrese el codigo del libro: ")
    libro = buscar_por_codigo(libros, codigo)
    if libro is None:
        print("Error: el codigo del libro no existe")
        return False
    if libro["estado"] != "Prestado":
        print("Error: el libro no se encuentra prestado")
        return False
    libro["estado"] = "Disponible"
    for prestamo in prestamos:
        if prestamo["codigo_libro"] == codigo and prestamo["estado"] == "Activo":
            prestamo["estado"] = "Devuelto"
            break
    guardar_libros(libros)
    guardar_prestamos(prestamos)
    print("Libro devuelto correctamente")
    return True


def mostrar_prestamos(libros, prestamos):
    if not prestamos:
        print("No existe prestamos registrados")
        return
    print("*****Lista de Prestamos*****")
    for prestamo in prestamos:
        libro = buscar_por_codigo(libros, prestamo["codigo_libro"])
        if libro is not None:
            titulo = libro["titulo"]
        else:
            titulo = "Libro no encontrado"
        print("*****************************************************")
        print(f"Numero: {prestamo['numero']}")
        print(f"Libro: {titulo}")
        print(f"Estudiante: {prestamo['estudiante']}")
        print(f"Fecha: {prestamo['fecha']}")
        print(f"Estado: {prestamo['estado']}")
        print("*****************************************************")

def reporte_general(libros, prestamos):
    disponibles = 0
    prestados = 0
    for libro in libros:
        if libro["estado"] == "Disponible":
            disponibles += 1
        elif libro["estado"] == "Prestado":
            prestados += 1

    activos = 0
    total_prestamos = 0
    for prestamo in prestamos:
        total_prestamos += 1 
        if prestamo["estado"] == "Activo":
            activos += 1

    try:
        porcentaje = (prestados / len(libros)) * 100
    except ZeroDivisionError:
        porcentaje = 0.0
        print("No hay libros registrados.")

    print("********Reporte General********")
    print(f"Libros disponibles: {disponibles}")
    print(f"Libros prestados : {total_prestamos}")
    print(f"Prestamos activos: {activos}")
    print(f"Porcentaje de libros prestados: {porcentaje:.2f}%")
    

libros = cargar_libros()
prestamos = cargar_prestamos()
opcion = 0
while opcion != 8:

    print("""
    ===============================================
              BIBLIOTECA DIGITAL TECAZUAY
    ===============================================
    1. Registrar Libro       5. Devolver libro 
    2. Mostrar Libro         6. Mostrar prestamos
    3. Buscar libro          7. Reporte general
    4. Prestar libro         8. Salir
    ===============================================
    """)

    opcion = leer_entero("Elija una opción: ")
    if opcion == 1:
        libros = cargar_libros()
        registrar_libro(libros)
    elif opcion == 2:
        mostrar_libros(libros)
    elif opcion == 3:
        buscar_libro(libros)
    elif opcion == 4:
        prestar_libro(libros, prestamos)
    elif opcion == 5:
        devolver_libro(libros, prestamos)
    elif opcion == 6:
        mostrar_prestamos(libros, prestamos)
    elif opcion == 7:
        reporte_general(libros,prestamos)
    elif opcion == 8:
        guardar_libros(libros)
        print("Guardado")

    else:
        print("Opción no válida: elija un número del 1 al 8.")
