# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

# def mi_funcion(): 
#     print("¡Hola amiga!")

# mi_funcion()

# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

# def saludo(nombre):
#     print("¡hola",nombre + "!")

# nombre = input("como se llama: ")
# saludo(nombre)

# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

# def fact(num):
#     if num>0:
#         for x in range(1,num):
#             num = num * x
#         return num
    
# print(fact(int(input("ingrese un numero: "))))

# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

# def fact(cash,iva = 21):
#     return cash + (cash*(iva/100))

# cash = int(input("costo del producto: "))
# iva = int(input("digite el porcentaje de iva sin el %: "))
# print(fact(cash,iva))

# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando 
# la primera función.

# import math

# def area(radio):
#     return round(math.pi * radio**2 , 2)

# def volumen(radio,altura):
#     return area(radio)*altura

# print(volumen(int(input("digite el radio: ")),int(input("digite la altura: "))))

# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.


# def med(lista):
#     return float((sum(lista)/len(lista)))

# print(med([1,2,3,4,5,6,7,8,9,10]))


# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.


# def cuadrado(lista):
#     for x in range(len(lista)):
#         lista[x] = lista[x]**2
#     return lista

# print(cuadrado([1,2,3,4,5,6,7,8,9,10]))


# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media,
# varianza y desviación típica.


# from math import sqrt

# dicc = {"media": 0,"varianza": 0, "desviacion": 0}

# def found(lista):
#     cont=0
#     dicc["media"] = float((sum(lista)/len(lista)))
#     for x in range(len(lista)):
#         cont = cont + ((lista[x] - dicc["media"])**2)
#     dicc["varianza"] = cont/len(lista)
#     dicc["desviacion"] = round(sqrt(dicc["varianza"]),2)

# found([1,2,3,4,5])
# print(dicc)


# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y 
# otra que calcule el mínimo común múltiplo.


# def mcd(num1,num2):
#     num0 = 0
#     cont = 0
#     if num1 < num2:
#         num0 = num1
#         num1 = num2
#         num2 = num0
#     for x in range(1,num1):
#         if num1%x == 0 and num2%x == 0 :
#             cont = x
#     return cont

# def mcm(num1,num2):
#     num0 = 0
#     cont = 0
#     if num1 < num2:
#         num0 = num1
#         num1 = num2
#         num2 = num0
#     return (num1*num2)/mcd(num1,num2)

# print(mcd(32,68))
# print(mcm(32,68))


# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

# print(int('11111111', 2))  #=> te da 255`
# print(bin(10))

# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
