class Articulo:
    def __init__(self,codigo,nombre,precio,stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def vender(self,cantidad):
        if cantidad <=0 :
            print("Error: Cantidad invalida")
            return False
        elif cantidad>self.stock:
            print("Error: Cantidad mayor a la del stock")
            return False
        else:
            self.stock-=cantidad
            return True

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<15}{self.precio:>8.2f}{self.stock:>8}"

articulos = [
    Articulo(1,"Cuaderno",1.50,50),
    Articulo(2,"Lapiz",0.30,100)
]

while True:
    print("""
    ***************  PAPELERIA  ***************
    1. Registrar articulo   3. Vender articulo
    2. Mostrar articulos    4. Salir
""")
    opcion=int(input("Ingrese una opcion: "))

    if opcion ==1:
        codigo = len(articulos) + 1
        nombre = input("Ingrese el nombre del articulo: ")
        precio = float(input("Ingrese el precio del articulo: "))
        stock = int(input("Ingrese el stock: "))
        articulos.append(Articulo(codigo,nombre,precio,stock))

    elif opcion ==2:
        print(f"{'Código':<8}{'Nombre':<15}{'Precio':>8}{'Stock':>8}")
        for a in articulos:
            print(a)
    elif opcion == 3:
        try:
            codigo = int(input("Código: "))
            encontrado = None
            for a in articulos:
                if a.codigo == codigo:
                    encontrado = a
            if encontrado is None:
                print("Error: no existe ese código.")
            else:
                cantidad = int(input("Cantidad: "))
                if encontrado.vender(cantidad):
                    print(f"Listo. Quedan {encontrado.stock} unidades.")
        except ValueError:
            print("Error: ingrese un número entero.")
    elif opcion==4:
        print("Saliendo")
        break

        

    
