from datetime import date

ARCHIVO_LIBROS = "Trabajo_grupal/libros.txt"
ARCHIVO_PRESTAMOS = "Trabajo_grupal/prestamos.txt"

class Libro:
    def __init__(self, codigo, titulo, autor, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def mostrar(self):
        print(f"{self.codigo:<8}{self.titulo:<30}"
              f"{self.autor:<22}{self.estado:<12}")

    def cambiar_estado(self, estado1):
        self.estado = estado1

    def __str__(self):
        return (f"Codigo: {self.codigo}, Titulo: {self.titulo}, "
                f"Autor: {self.autor}, Estado: {self.estado}")
    
class Prestamo:
    def __init__(self, numero, codigo_libro, estudiante, fecha, estado):
        self.numero = numero
        self.codigo_libro = codigo_libro
        self.estudiante = estudiante
        self.fecha = fecha
        self.estado = estado

    def mostrar(self):
        print(f"Numero: {self.numero}")
        print(f"Codigo del libro: {self.codigo_libro}")
        print(f"Estudiante: {self.estudiante}")
        print(f"Fecha: {self.fecha}")
        print(f"Estado: {self.estado}")

    def cambiar_estado(self, estado1):
        self.estado = estado1

    def __str__(self):
        return (f"Numero: {self.numero}, Codigo del libro: {self.codigo_libro}, "
                f"Estudiante: {self.estudiante}, Fecha: {self.fecha}, "
                f"Estado: {self.estado}")

def guardar_libros(libros):
    with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as archivo:
        for libro in libros:
            linea = f"{libro.codigo},{libro.titulo},"
            linea += f"{libro.autor},{libro.estado}\n"
            archivo.write(linea)

def cargar_libros():
    libros = []

    try:
        with open(ARCHIVO_LIBROS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                libro = Libro(
                    int(datos[0]),
                    datos[1],
                    datos[2],
                    datos[3]
                )

                libros.append(libro)

    except FileNotFoundError:
        print("No se encontro libros.txt: se usan los libros iniciales.")

        libros.append(
            Libro(1, "Python para todos", "Charles Severance", "Disponible")
        )
        libros.append(
            Libro(2, "Aprende Java", "Ana Torres", "Disponible")
        )
        libros.append(
            Libro(3, "Bases de datos", "Carlos Mora", "Disponible")
        )

        guardar_libros(libros)

    return libros

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe escribir un numero entero.")

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print(f"El texto no puede estar vacio {mensaje}")
        elif "," in texto:
            print("El texto no puede llevar comas (,)")
        else:
            return texto

def buscar_por_codigo(libros, codigo):
    for libro in libros:
        if libro.codigo == codigo:
            return libro

    return None

def registrar_libro(libros):
    titulo = leer_texto("Titulo: ")
    autor = leer_texto("Autor: ")

    mayor = 0

    for libro in libros:
        if libro.codigo > mayor:
            mayor = libro.codigo

    nuevo = Libro(
        mayor + 1,
        titulo,
        autor,
        "Disponible"
    )

    libros.append(nuevo)
    guardar_libros(libros)

    print(f"Libro registrado con el codigo {nuevo.codigo}.")
    return nuevo

def mostrar_libros(libros):
    print(f"{'Codigo':<8}{'Titulo':<30}{'Autor':<22}{'Estado':<12}")
    print("-" * 72)

    cantidad = 0

    for libro in libros:
        libro.mostrar()
        cantidad += 1

    return cantidad

def buscar_libro(libros):
    palabra = leer_texto("Palabra a buscar en el titulo: ").lower()
    encontrados = 0

    for libro in libros:
        if palabra in libro.titulo.lower():
            libro.mostrar()
            encontrados += 1

    if encontrados == 0:
        print("No se encontro ningun libro con esa palabra.")

    return encontrados

def cargar_prestamos():
    prestamos = []

    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                prestamo = Prestamo(
                    int(datos[0]),
                    int(datos[1]),
                    datos[2],
                    datos[3],
                    datos[4]
                )

                prestamos.append(prestamo)

    except FileNotFoundError:
        print("No se encontro prestamos.txt: se inicia con una lista vacia.")

    return prestamos

def guardar_prestamos(prestamos):
    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as archivo:
        for prestamo in prestamos:
            linea = (f"{prestamo.numero},{prestamo.codigo_libro},"
                     f"{prestamo.estudiante},{prestamo.fecha},"
                     f"{prestamo.estado}\n")
            archivo.write(linea)

def prestar_libro(libros, prestamos):
    codigo = leer_entero("Ingrese el codigo del libro: ")
    libro = buscar_por_codigo(libros, codigo)

    if libro is None:
        print("Error: el codigo del libro no existe.")
        return False

    if libro.estado != "Disponible":
        print("Error: el libro se encuentra prestado.")
        return False

    estudiante = leer_texto("Ingrese su nombre: ")

    if prestamos:
        numeros = []

        for prestamo in prestamos:
            numeros.append(prestamo.numero)

        numero = max(numeros) + 1
    else:
        numero = 1

    fecha_actual = str(date.today())

    prestamo = Prestamo(
        numero,
        codigo,
        estudiante,
        fecha_actual,
        "Activo"
    )

    prestamos.append(prestamo)
    libro.cambiar_estado("Prestado")

    guardar_libros(libros)
    guardar_prestamos(prestamos)

    print("Prestamo registrado correctamente.")
    return True

def devolver_libro(libros, prestamos):
    codigo = leer_entero("Ingrese el codigo del libro: ")
    libro = buscar_por_codigo(libros, codigo)

    if libro is None:
        print("Error: el codigo del libro no existe.")
        return False

    if libro.estado != "Prestado":
        print("Error: el libro no se encuentra prestado.")
        return False

    libro.cambiar_estado("Disponible")

    for prestamo in prestamos:
        if prestamo.codigo_libro == codigo and prestamo.estado == "Activo":
            prestamo.cambiar_estado("Devuelto")
            break

    guardar_libros(libros)
    guardar_prestamos(prestamos)

    print("Libro devuelto correctamente.")
    return True

def mostrar_prestamos(libros, prestamos):
    if not prestamos:
        print("No existen prestamos registrados.")
        return

    print("***** Lista de Prestamos *****")

    for prestamo in prestamos:
        libro = buscar_por_codigo(libros, prestamo.codigo_libro)

        if libro is not None:
            titulo = libro.titulo
        else:
            titulo = "Libro no encontrado"

        print("*****************************************************")
        print(f"Numero: {prestamo.numero}")
        print(f"Libro: {titulo}")
        print(f"Estudiante: {prestamo.estudiante}")
        print(f"Fecha: {prestamo.fecha}")
        print(f"Estado: {prestamo.estado}")
        print("*****************************************************")

def reporte_general(libros, prestamos):
    disponibles = 0
    prestados = 0

    for libro in libros:
        if libro.estado == "Disponible":
            disponibles += 1
        elif libro.estado == "Prestado":
            prestados += 1

    activos = 0
    total_prestamos = 0

    for prestamo in prestamos:
        total_prestamos += 1

        if prestamo.estado == "Activo":
            activos += 1

    try:
        porcentaje = (prestados / len(libros)) * 100
    except ZeroDivisionError:
        porcentaje = 0.0
        print("No hay libros registrados.")

    print("******** Reporte General ********")
    print(f"Libros disponibles: {disponibles}")
    print(f"Libros prestados: {total_prestamos}")
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

    opcion = leer_entero("Elija una opcion: ")

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
        reporte_general(libros, prestamos)

    elif opcion == 8:
        guardar_libros(libros)
        guardar_prestamos(prestamos)
        print("Datos guardados. Hasta pronto.")

    else:
        print("Opcion no valida: elija un numero del 1 al 8.")
