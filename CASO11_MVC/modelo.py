class Articulo:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= 0:
            return False , "Error: la cantidad debe ser mayor que cero"
        if cantidad > self.stock:
            
            return False,f"Error: solo hay {self.stock} unidades."
        self.stock -= cantidad
        return True,f"Listo. Quedan {self.stock} unidades."

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<15}{self.precio:>8.2f}{self.stock:>8}"


class Inventario:

    def __init__(self):
        self.articulos = [
            Articulo(1, "Cuaderno", 1.50, 50),
            Articulo(2, "Lápiz", 0.30, 100),
        ]

    def registrar(self, nombre, precio, stock):
        codigo = len(self.articulos) + 1
        self.articulos.append(Articulo(codigo, nombre, precio, stock))
        return codigo

    def buscar(self, codigo):
        encontrado = None
        for a in self.articulos:
            if a.codigo == codigo:
                encontrado = a
        return encontrado