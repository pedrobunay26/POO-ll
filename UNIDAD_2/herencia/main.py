from estudiante import Estudiante
from docente import Docente

estudiantes=[
Estudiante("Pedro","Buñay","0151195419","0919283563","pedro@gmail.com",22,"Ricaurte","TDSU",[8,7,9,7.8,6.5]),
Estudiante(nombre="Kevin",apellido="Chicaiza",cedula="0109293864",celular="0953785682",correo="kevin@gmail.com",edad=22,direccion="Yanaturo",carrera="TDSU",notas=[9,8,9,7,6]),
Estudiante(nombre="Karen",apellido="Carabajo",cedula="0173247289",celular="0918765436",correo="karen@gmail.com",edad=19,direccion="Ricaurte",carrera="TDSU",notas=[8,7,9,8,9]),
Estudiante(nombre="Domenica",apellido="Crespo",cedula="0189778719",celular="0919598643",correo="domenica@gmail.com",edad=20,direccion="Molinopamba",carrera="TDSU",notas=[8,8,9,7,8]),
Estudiante(nombre="Steven",apellido="Ortiz",cedula="0159837487",celular="0935763566",correo="Steven@gmail.com",edad=24,direccion="Miraflores",carrera="TDSU",notas=[8,7,9,4,5])
]

print(Estudiante.validar_edad())
# print(estudiante.__str__())
docente = Docente("Veronica","Chimbo","1183247282","0910934546","veronica@gmail.com",35,"Ricaurte","POO ll",18)
docente = Docente("Iliana","Tinoco","1498234779","'0983764525'","Iliana@gmail.com",30,"Miraflores","Expresion oral",15)
docente = Docente("Diana","Romero","1183247282","0910934546","diana@gmail.com",35,"Ricaurte","Estadistica",20)
docente = Docente("Carmen","Tacuri","1183247282","0910934546","carmen@gmail.com",35,"Ricaurte","Desarrollo Web",16)
docente = Docente("Veronica","Segarra","1183247282","0910934546","veronicaSegarra@gmail.com",35,"Ricaurte","Base de Datos",12)
print(f"El docente {docente.validar_edad()}")
print(docente.__str__())
