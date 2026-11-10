notas = [10,8,9,5]

print (notas)
print (notas[1])
notas.append(20)
print(notas)
print (max(notas))
notas.insert(1,10)
print (notas)
print (len(notas))
print (notas[-1])
print (sum(notas))
print (notas[0])
print(notas[-2:])
print(notas[:2])
print(min(notas))
notas.remove(10)
notas = sorted(notas)
print(notas[2:])
print(notas[:2])
print(notas[::3])

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

print(meses[0])
print(meses[-1])
# meses.insert(1, "Enero")

estudiante ={
    "cedula": "123456789",
    "nombre": "pedro",
    "correo": "pedrojose@gmail.com",
    "celular": "0987234672",
    "notas": [10, 8, 9, 5]
}

print(estudiante["nombre"])
print(estudiante.keys())

conjunto_a = {1, 1,5,4,6,8}
conjunto_b = {1,9,6,5,4}

print(conjunto_a & conjunto_b)

print(conjunto_a | conjunto_b)

socio = {
    "cedula": "0102030405",                 # str: puede empezar con 0
    "nombre": "  ana lucía pérez ",          # str con espacios y minúsculas
    "edad": 34,                              # int
    "activo": True,                          # bool
    "garante": None,                         # None: todavía no tiene
    "cuentas": [                             # list de dict
        {"numero": "AH-001", "tipo": "ahorros", "saldo": 1520.75},
        {"numero": "PF-010", "tipo": "plazo fijo", "saldo": 5000.0},
        {"numero": "AH-002", "tipo": "ahorros", "saldo": 80.5},
    ],
}

print(socio["nombre"].strip())
print(socio.get("nombre").strip())
print("La cedula es", socio.get("cedula"), " y la edad es", socio.get("edad"))
print(f"Activo: {socio['activo']}")
lista = [cuenta["saldo"] for cuenta in socio["cuentas"]]
print("SALDO: ",lista)
print(socio["cuentas"][1]["saldo"])