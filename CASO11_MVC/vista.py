class Vista:
    def mostrar_menu(self):
        print("""
    ***************  PAPELERIA  ***************
    1. Registrar articulo   3. Vender articulo
    2. Mostrar articulos    4. Salir
        """)
        return int(input("Opción: "))
        

    def pedir_datos_articulo(self):
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        return nombre, precio, stock

    def pedir_codigo(self):
        return int(input("Código: "))

    def pedir_cantidad(self):
        return int(input("Cantidad: "))

    def mostrar_articulos(self, articulos):
        print(f"{'Código':<8}{'Nombre':<15}{'Precio':>8}{'Stock':>8}")
        for a in articulos:
            print(a)

    def mensaje(self, texto):
        print(texto)
        
    def error(self, texto):
        print(texto)