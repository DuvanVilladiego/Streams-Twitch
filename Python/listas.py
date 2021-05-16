# lista = ["Matemáticas","Física","Química","Historia","Lengua"]
# notas = [*lista]

# for x in range(len(lista)):
#     print(lista[x])
#     notas[x] = input("digite nota:")
# for x in range(len(lista)):
#     print("obtuve",notas[x],"en",lista[x])


# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
# Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las
# muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las
# asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# loteria = [1,2,3,4,5,6]

# for x in range(len(loteria)):
#     loteria[x] = int(input("digite la loteria por digitos: "))

# loteria.sort()

# for x in range(len(loteria)):
#     print("los numeros en orden ascendente son", loteria[x])

# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los
# almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


# lista=[1,2,3,4,5,6,7,8,9,10]

# for x in reversed(range(len(lista))):
#     print(lista[x])

# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por
# pantalla en orden inverso separados por comas.


""" lista = ["Matemáticas","Física","Química","Historia","Lengua"]
notas = [*lista]

for x in range(len(lista)):
    print(lista[x])
    notas[x] = int(input("digite nota:"))
for x in range(len(lista)):
    if notas[x]<3:
        print("obtuve",notas[x],"en",lista[x],"tienes que repetir")

 """

""" Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física,
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar
por pantalla las asignaturas que el usuario tiene que repetir. """


""" lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(len(lista)):
    if x % 3 == 0:
        print(lista[x])
 """

""" Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante. """

""" palabra = input("digite su palabra: ")
lista = list(palabra)

if lista == lista[::-1]:
    print("es un palindromo")
else:
    print("no es un palindromo")
 """
""" Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. """