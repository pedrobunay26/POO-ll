class Reserva:  
   
    def _init_(self, numero, codigo, cantidad, total, fecha, estado):
            self.numero = numero
            self.codigo = codigo
            self.cantidad = cantidad
            self.total = total
            self.fecha = fecha
            self.estado = estado

    def crear_reserva(tours):
        with open("reservas.txt", "w", encoding="utf-8") as archivo:
            for i in tours:
                i = f"{i.nunero},{i.codigo},{i.cantidad},{i.total},{i.fecha},{i.estado}"
                archivo.write(i)