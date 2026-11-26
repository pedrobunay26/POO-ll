from modelo import *
from controlador import *
from vista import Vista

modelo = Inventario()
vista = Vista()
controlador = Controlador(modelo,vista)

controlador.ejecutar()