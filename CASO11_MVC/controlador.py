class Controlador:
    def __init__(self,modelo,vista):
        self.modelo = modelo
        self.vista=vista
        
    def ejecutar(self):
        opcion = ""
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion ==1:
                try:
                    nombre,precio,stock = self.vista.pedir_datos_articulo()
                    codigo = self.modelo.registrar(nombre,precio,stock)
                    self.vista.mensaje(f"Articulo con codigo {codigo} ingresado correctamente")
                except ValueError:
                    self.vista.error("Datos ingresados incorrectamente")
                
            elif opcion ==2:
                self.vista.mostrar_articulos(self.modelo.articulos)
            elif opcion == 3:
                try:
                    codigo = self.vista.pedir_codigo()
                    encontrado = self.modelo.buscar(codigo)
                    if encontrado is None:
                        self.vista.error("No existe ese código.")
                    else:
                        cantidad = self.vista.pedir_cantidad()
                        estado,mensaje = encontrado.vender(cantidad)
                        if estado ==True:
                            self.vista.mensaje(mensaje)
                        else:
                            self.vista.error(mensaje)
                except ValueError:
                    self.vista.error("Ingrese un número entero.")
            elif opcion==4:
                self.vista.mensaje("Saliendo")
                break