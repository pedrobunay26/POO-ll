class Vista:
    def mostrar_menu(self):
        print("""
    ***************  PAPELERIA  ***************
    1. Registrar articulo   3. Vender articulo
    2. Mostrar articulos    4. Salir
        """)

    def pedir_opcion(self):
        return input("Opción: ")

    def pedir_datos_articulo(self):
        nombre = input("Nombre: ")
        precio = input("Precio: ")
        stock = input("Stock: ")
        return nombre, precio, stock

    def pedir_codigo(self):
        return input("Código: ")

    def pedir_cantidad(self):
        return input("Cantidad: ")

    def mostrar_articulos(self, articulos):
        print(f"{'Código':<8}{'Nombre':<15}{'Precio':>8}{'Stock':>8}")
        for a in articulos:
            print(a)

    def mensaje(self, texto):
        print(texto)