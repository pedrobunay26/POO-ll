def pregunta1(frase):
    return len(frase.split())
    
def pregunta2(a,b):
    return len(a&b)

def pregunta3():
    return type(10.0)

def pregunta4():
    return "ab" * 3

def pregunta5():
    return int(9.99)

def pregunta6():
    for n in [1, 2, 3, 4]:
        if n == 3:
            break
        print(n, end=" ")
        

def pregunta7():
    for i in range(3, 0, -1):
        print(i, end=" ")

def pregunta8(total,n):
    while n <= 5:
        total += n
        n += 1
    return(total)

def pregunta9():
    for i in range(3):
        for j in range(2):
            print("*", end="")

def pregunta10():
    for x in [2, 4, 6]:
        if x == 7:
            return("Encontrado")
            break
        else:
            return("No encontrado")

def pregunta11():
    numeros = []
    while True:
        numero = input("Ingrese un número o 'fin' para finalizar: ")
        if numero == "fin":
            break
        numeros.append(int(numero))

    lista_pares = []
    lista_impares = []

    for i in numeros:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    print("\n Lista de pares:", sorted(lista_pares), "Su suma es:", sum(lista_pares))
    print(" Lista de impares:", sorted(lista_impares), "Su suma es:", sum(lista_impares))


while True:
    print("\n ****** Menu de Usuarios")
    print("1. Ingresar Nombre")
    print("2. Menu Secundario")
    print("3. Salir")
    opcion = int (input("Ingrese una opcion:  "))

    if opcion ==1:
        nombre = input("Ingrese su nombre:  ")
        print(f"\n BIENVENIDO ESTIMADO {nombre.upper()} ESPERO QUE SE ENCUENTRE BIEN EL DIA DE HOY ")
        
    elif opcion == 2:
        while True:
            print("\n Menu de Preguntas")
            print("1. Pregunta 1")
            print("2. Pregunta 2")
            print("3. Pregunta 3")
            print("4. Pregunta 4")
            print("5. Pregunta 5")
            print("6. Pregunta 6")
            print("7. Pregunta 7")
            print("8. Pregunta 8")
            print("9. Pregunta 9")
            print("10. Pregunta 10")
            print("11. Pregunta 11")
            print("12. Salir ")
            
            opcion2 = int (input("Ingrese una opcion:\n"))
            if opcion2 == 1:
                print("La respuesta es: ", pregunta1("aprendo Python en TEC"))
                
            elif opcion2 == 2:
                print("La respuesta es: ", pregunta2({1, 2, 3, 4},{3, 4, 5}))
                
            elif opcion2 == 3:
                print("La respuesta es: ", pregunta3())
                
            elif opcion2 == 4:
                print("La respuesta es: ", pregunta4())
                
            elif opcion2 == 5:
                print("La respuesta es: ", pregunta5())
                
            elif opcion2 == 6:
                print("La respuesta es: ",end=" ")
                pregunta6()
                
            elif opcion2 == 7:
                print("La respuesta es: ", end=" ")
                pregunta7()
                
            elif opcion2 == 8:
                print("La respuesta es: ", pregunta8(0,1))
                
            elif opcion2 == 9:
                print("La respuesta es: ", end=" ")
                pregunta9()
            elif opcion2 == 10:
                print("La respuesta es: ", pregunta10())
                
            elif opcion2 == 11:
                pregunta11()
                           
            elif opcion2 == 12:
                break
            
    elif opcion ==3:
        break
            
