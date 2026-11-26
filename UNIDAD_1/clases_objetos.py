# Crear una clase
#class Libro:
#    pass

    
libro1=Libro()
print(type(libro1))

class Libro:
    def __init__(self,nombre,autor,estado):
        self.nombre=nombre
        self.autor=autor
        self.estado=estado
    def mostrar(self):
        print(self.nombre)
        print(self.estado)
        
    def __str__(self):
        return f""
        
    def cambiar_estado(self,estado1):
        self.estado=estado1
        
        
libro2=Libro("Python intrtmiedio","Sandoval","Diponible")
libro2.mostrar()
print(libro2)
libro2.cambiar_estado("Prestado")
print(libro2)
