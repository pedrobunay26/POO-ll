#Declaracion de funciones
def saludar():
    print("Hola Pedro")
saludar()

#Funcion con parametros
'''
def calcular_edad(anio_nacimiento,anio_actual):
    print("La edad es: ",anio_actual - anio_nacimiento ," años")
a = int(input("Ingrese su año de nacimiento"))
b = int(input("Ingrese el año actual"))
calcular_edad(a,b)    

#funciones con retorno

def calcular_iva(precio,iva):
    return precio*iva

resultado = calcular_iva(20,0.15)
print("El iva es: ",resultado)

#Funcines con valores por defecto

def calcular_iva(precio,iva = 0.15):
    return precio*iva

resultado = calcular_iva(20)
print("El iva es: ",resultado)

resultado = calcular_iva(20,0.12)
print("El iva es: ",resultado)

def calcular_par(numeros):
    for i in numeros:
        if i%2==0:
            print("El numero",i,"es par")
        else:
            print("El numero",i,"es impar")
numeros = range(0,1000)
calcular_par(numeros)

lista_pares = range(5,0,-1)
for e in lista_pares:
    print(e,end=" ")
    
#Funciones con tuplas

def suma_numeros (*a):
    return sum(a)
print("La suma es: ",suma_numeros(1,2,3))
'''
#Funciones con diccionario

def estudiantes(**lista_estudiantes):
    suma_total = 0
    for nombre,edad in lista_estudiantes.items():
        print("El estudiante",nombre,"tiene",edad)
        suma_total += edad
    print(suma_total)
    
estudiantes(Veronica=20,Juan =22,Maria=30,Karen =19,Steven =24,kevin = 22)

