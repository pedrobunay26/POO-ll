class Tour:
    def __init__(self,codigo, nombre, precio, cupos):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.cupos=cupos
        
    
    def validar_archivo():
        try:
            with open("tours.txt","r",encoding="utf-8") as archivo:
                tour =[]
                for tour in archivo:
                    datos = tour.strip().split(",")
               
                    tour = Tour(
                    int(datos[0]),
                    datos[1],
                    float(datos[2]),
                    int(datos[3])
                    )
                    tour.append()
        except FileNotFoundError:
            
            with open("tours.txt","w",encoding="utf-8") as archivo:
                tour=[
                       Tour(1,"Centro Historico", 15.00,20)
                   ]
                archivo.write(tour)
                
    validar_archivo()