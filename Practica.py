from functools import reduce

cantidad=int(input("ingrese el numero de estudiantes: "))

estudiantes =list(map(lambda x:input("ingrese el nombre del estudiantes: "),range(cantidad)))

notas = list(map(lambda x:int (input("ingrese las notas de los estudiantes: ")), range(cantidad)))

combinado = list (zip( estudiantes,notas))

promedio=reduce(lambda x, y:x+y,notas)/cantidad

def aprobado (combinado):
    return list(filter(lambda x: x[1] >= 70, combinado))
pasan = aprobado(combinado)

def reaprobado (combinado):
    return list(filter(lambda x: x[1] < 70, combinado))
nopasan = reaprobado(combinado)

print("Estudiantes y notas: ")
print(combinado)
print("promedio de las notas: ")
print(promedio)
print("Estudinates que pasaron: ")
print(pasan)
print("Estudiantes que no aprobado")
print(nopasan)
