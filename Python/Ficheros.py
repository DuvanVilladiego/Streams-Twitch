# Ejercicio 1

# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt 
# la tabla de multiplicar de ese número, done n es el número introducido.

# import os

# def numero():
#     num = int(input("digite un numero entre 1 y 10: "))
#     fichero = ("tabla-" + str(num) + ".txt")
#     file = open(fichero, "w")
#     for x in range(10):
#         writer = ( str(num) + " x " +  str(x+1) + " = " + str((x+1)*num))
#         file.write(writer + os.linesep)
#     file.close()

# numero()

# Ejercicio 2

# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt 
# con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.


# import os

# def numero():
#     num = int(input("digite un numero entre 1 y 10: ")) 
#     fichero = ("tabla-" + str(num) + ".txt")
#     try:
#         file = open(fichero, "r")
#         mostrar = file.read()
#         print(mostrar)
#         file.close()
#     except FileNotFoundError:
#         print("El fichero no existe")

# numero()

# Ejercicio 3

# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt 
# con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# import os

# def numero():
#     n = int(input("digite un numero entre 1 y 10: ")) 
#     m = int(input("que linea desea consultar: ")) 
#     fichero = ("tabla-" + str(n) + ".txt")
#     try:
#         file = open(fichero, "r")
#         mostrar = file.readlines()
#         print(mostrar[m-1])
#         file.close()
#     except FileNotFoundError:
#         print("El fichero no existe")

# numero()


# Ejercicio 4

# Escribir un programa que acceda a un fichero de internet mediante su url y 
# muestre por pantalla el número de palabras que contiene.

# from urllib import request

# url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
# file = request.urlopen(url)
# num = file.read()

# print(len(num.split()))

# Ejercicio 5

# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de 
# la Unión Europea (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
# pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.
##################################
# from urllib import request

# url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"

# def PIB(pais):
#     file = request.urlopen(url)
#     lectura = file.readlines()
#     print(lectura[0])

# PIB("d")
###################################
# Ejercicio 6

# Escribir un programa para gestionar un listín telefónico con los nombres y 
# los teléfonos de los clientes de una empresa. El programa incorporar funciones crear el fichero 
# con el listín si no existe, para consultar el teléfono de un cliente, 
# añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente.
#  El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y 
# su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

# import os

# def numero():
#     consult = input("que desea hacer: (consultar // crear) ")
#     if consult == "Consultar":
#         nombre = input("digite el nombre del cliente: ")
#         file = open("listin.txt", "r")
#         archivo = file.readlines()

#         print(archivo)

# numero()

# Ejercicio 7

# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:
#  Nombre (nombre de la empresa), 
# Final (precio de la acción al cierre de bolsa),
# Máximo (precio máximo de la acción durante la jornada), 
# Mínimo (precio mínimo de la acción durante la jornada), 
# Volumen (Volumen al cierre de bolsa),
# Efectivo (capitalización al cierre en miles de euros).

#     Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.

#     Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.








# Ejercicio 8

# El fichero calificaciones.csv contiene las calificaciones de un curso. 
# Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. 
# Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso 
# (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

#     Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

#     Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

#     Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.



print("hasta la proxima..")
print("gracias por estar :3")