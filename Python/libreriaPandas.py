# Ejercicio 1

# Escribir un programa que pregunte al usuario por las ventas de un rango de años y 
# muestre por pantalla una serie con los datos de las ventas indexada por los años, 
# antes y después de aplicarles un descuento del 10%.

# import pandas as pd

# diccionario = {}
# diccionario2 = {}
# descuento = 10.00
# anos = input("rango de años separado por guion (ejemplo: 2010-2020): ")
# rango = int((anos.split("-"))[1]) - int((anos.split("-"))[0])
# menor = int((anos.split("-"))[0])

# for x in range(rango+1):
#     sout = menor + x
#     print("ingrese las ventas para",sout,": ")
#     diccionario[sout] = int(input(""))
#     diccionario2[sout] = diccionario[sout]*float(1-(descuento/100))

# def des(dicc,dicc2):
#     print("Antes del descuento: ")
#     print(pd.Series(dicc))
#     print("Despues del descuento de ",descuento," % : ")
#     print(pd.Series(dicc2))

# des(diccionario,diccionario2)


# Ejercicio 2

# Escribir una función que reciba una diccionario con las notas de los alumnos
# en curso en un examen y
# devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

# import pandas as pd
# import math

# diccionario = {}
# diccionario2 = {}

# while True:
#     data = input("nombre y nota del alumno separado por puntos ( ejemplo Jose:5 ): ")
#     if data == "salir":
#         break
#     else:
#         datadiv = (data.split(":"))
#         diccionario[datadiv[0]] = int(datadiv[1])

# def desv(diccio,media):
#     n = 0
#     for x in diccio:
#         n = n + ((int(diccio[x]))-(int(media)))**2
#     n = n/len(diccio)
#     return math.sqrt(n)

# def notas(dicc):
#     diccionario2["minima"] = round(min(dicc.values()),2)
#     diccionario2["max"] = round(max(dicc.values()),2)
#     nota = 0
#     for n,d in dicc.items():
#         nota += d
#     diccionario2["media"] = round(nota/len(dicc),2)
#     diccionario2["desviación Tipica"] = round(desv(dicc,diccionario2["media"]),2)
#     print(pd.Series(diccionario2))

# notas(diccionario)


# Ejercicio 3

# Escribir una función que reciba una diccionario con las notas de los 
# alumnos en curso en un examen y 
# devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

# import pandas as pd
# import operator

# aceptacion = 4
# diccionario = {}

# while True:
#     data = input("nombre y nota del alumno separado por puntos ( ejemplo Jose:5 ): ")
#     if data == "salir":
#         break
#     else:
#         datadiv = (data.split(":"))
#         diccionario[datadiv[0]] = int(datadiv[1])

# def aprovados(dicc,acept):
#     diccionario2 = {}
#     for x in dicc:
#         if dicc[x] >= acept:
#             diccionario2[x]=dicc[x]
#     diccionario2 = dict(sorted(diccionario2.items(), key=operator.itemgetter(1),reverse=True))
#     return(pd.Series(diccionario2))
    

# print(aprovados(diccionario,aceptacion))

# Ejercicio 4

# Escribir programa que genere y muestre por pantalla un 
# DataFrame con los datos de la tabla siguiente:
# Mes 	Ventas 	Gastos
# Enero 	30500 	22000
# Febrero 	35600 	23400
# Marzo 	28300 	18100
# Abril 	33900 	20700

# import pandas as pd

# data = {"Mes":["Enero","Febrero","Marzo","Abril"],
#         "Ventas":[30500,35600,28300,33900],
#         "Gastos":[22000,23400,18100,20700]}

# data = pd.DataFrame(data)
# print(data)

# Ejercicio 5

# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, 
# una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

# import pandas as pd

# data = pd.DataFrame({"Mes":["Enero","Febrero","Marzo","Abril"],
#         "Ventas":[30500,35600,28300,33900],
#         "Gastos":[22000,23400,18100,20700]})

# meses = {"Febrero","Abril","Enero"}

# def balance(frames,listado):
#     frames["balance"] = frames.Ventas - frames.Gastos
#     return frames[frames.Mes.isin(listado)].balance.sum()

# print(balance(data,meses),"para los meses de",meses)

# Ejercicio 6

# El fichero cotizacion.csv contiene las cotizaciones de las empresas del 
# IBEX35 con las siguientes 
# columnas: nombre (nombre de la empresa), 
# Final (precio de la acción al cierre de bolsa), 
# Máximo (precio máximo de la acción durante la jornada), 
# Mínimo (precio mínimo de la acción durante 
# la jornada), volumen (Volumen al cierre de bolsa), 
# Efectivo (capitalización al cierre en miles de euros).
# Construir una función que construya un DataFrame a partir del un fichero 
# con el formato anterior
# y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.

# import pandas as pd

# data = pd.read_csv ('./cotizacion.csv')

# def frame(archivo):
#     datos = {"0":("Maximo","Minimo","Media")}
#     for x in range(1,6):
#         lista = []
#         med = 0
#         for n in range(3):
#             lista.append(archivo.loc[n][x])
#             med = med + archivo.loc[n][x]
#         datos[x] = max(lista),min(lista),med/3
#     print(pd.DataFrame(archivo))
#     print('----------------------------------------------------------')
#     print(pd.DataFrame(datos))

# frame(data)

# Ejercicio 7

# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. 
# Escribir un programa con los siguientes requisitos:

# import pandas as pd
# import statistics

# titanic = pd.read_csv("./train.csv", sep=',',  comment='#')
# filas = titanic.shape[0]
# columnas = titanic.shape[1]

# #     Generar un DataFrame con los datos del fichero. -----
# def Frame():
#     print(pd.DataFrame(titanic))
    
# #     Mostrar por pantalla las dimensiones del DataFrame, ----
# def FilasColumns():
#     print("El numero de filas es:",filas)
#     print("El numero de columnas es:",columnas)

# #     el número de datos que contiene, los nombres de sus columnas y filas,---
# def DimensionFrame():
#     print("El archivo trae",(filas * columnas),"datos")

# def NombreColumns():
#     print("nombre de las columnas: ")
#     for x in range(len(titanic.columns)):
#         print(titanic.columns[x])

# #     los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas ----
# def ColumnsTypes():
#     print("""tipos de datos por columnas: 
# """, titanic.dtypes)

# def PrimerasYUltimas10():
#     print("primeras 10 filas", titanic.head(10))
#     print("ultimas 10 filas", titanic.tail(10))

# #     Mostrar por pantalla los datos del pasajero con identificador 148.
# def Pasanger148(): 
#     pasanger = titanic[titanic["PassengerId"] == 1]
#     print(pasanger)

# #     Mostrar por pantalla las filas pares del DataFrame.
# def filasPares():
#     for x in range(filas):
#         if x%2 == 0:
#             print(titanic[titanic["PassengerId"] == x+1])

# #     Mostrar por pantalla los nombres de las personas que iban 
# #     en primera clase ordenadas alfabéticamente.
# def primeraClase():
#     lista = titanic[titanic["Pclass"] == 1]
#     nombres = lista["Name"]
#     print(nombres.sort_values())

# #     Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
# def porcentaje():
#     vivos = len(titanic[titanic["Survived"] == 1])
#     noVivos = len(titanic[titanic["Survived"] == 0])
#     print("Sobrevivio un ", round((vivos/filas)*100,2) , "%")
#     print("No sobrevivio un ", round((noVivos/filas)*100,2) , "%")

# #     Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
# def vivieronClase():
#     survive = titanic[titanic["Survived"] == 1]
#     clase1 = len(survive[survive["Pclass"] == 1])
#     clase1T = len(titanic[titanic["Pclass"] == 1])
#     clase2 = len(survive[survive["Pclass"] == 2])
#     clase2T = len(titanic[titanic["Pclass"] == 2])
#     clase3 = len(survive[survive["Pclass"] == 3])
#     clase3T = len(titanic[titanic["Pclass"] == 3])
#     print("Sobrevivio un", round((clase1/clase1T)*100,2) , "% de primera clase")
#     print("Sobrevivio un", round((clase2/clase2T)*100,2) , "% de segunda clase")
#     print("Sobrevivio un", round((clase3/clase3T)*100,2) , "% de tercera clase")

# #     Eliminar del DataFrame los pasajeros con edad desconocida.
# def passangerAgeDefined():
#     return titanic[titanic["Age"] >= 0]

# #     Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.

# def femaleMeanAge():
#     female = titanic[titanic["Sex"] == "female"]
#     clase1 = female[female["Pclass"] == 1]
#     ageClase1 = clase1["Age"].mean()
#     clase2 = female[female["Pclass"] == 2]
#     ageClase2 = clase2["Age"].mean()
#     clase3 = female[female["Pclass"] == 3]
#     ageClase3 = clase3["Age"].mean()
#     print("La edad media de las pasajeras de Clase 1 es",ageClase1)
#     print("La edad media de las pasajeras de Clase 2 es",ageClase2)
#     print("La edad media de las pasajeras de Clase 3 es",ageClase3)

# #     Añadir
# #  una nueva columna booleana para ver si el pasajero era menor de edad o no.
# def mayoriaDeEdad():
#     newTitanic = passangerAgeDefined().assign(Mayoria=False)
#     for x in newTitanic.index:
#         if newTitanic["Age"][x] >= 18:
#             newTitanic["Mayoria"][x] = True
#     return newTitanic

# #     Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron 
# #     en cada clase.

# def AliveMinMaxAge():
#     ages = mayoriaDeEdad()
#     mayor = ages[ages["Mayoria"] == True]
#     mayorAlive = mayor[mayor["Survived"] == 1]
#     menor = ages[ages["Mayoria"] == False]
#     menorAlive = menor[menor["Survived"] == 1]
#     #clase 1
#     mayorAliveClase1 = mayorAlive[mayorAlive["Pclass"] == 1]
#     menorAliveClase1 = menorAlive[menorAlive["Pclass"] == 1]
#     print("Sobrevivio un",round((len(mayorAliveClase1)/len(mayor))*100,2) , "% de los pasajeros mayores de edad de Clase 1")
#     print("Sobrevivio un",round((len(menorAliveClase1)/len(menor))*100,2) , "% de los pasajeros menores de edad de Clase 1")
#     #clase 2
#     mayorAliveClase2 = mayorAlive[mayorAlive["Pclass"] == 2]
#     menorAliveClase2 = menorAlive[menorAlive["Pclass"] == 2]
#     print("Sobrevivio un",round((len(mayorAliveClase2)/len(mayor))*100,2) , "% de los pasajeros mayores de edad de Clase 2")
#     print("Sobrevivio un",round((len(menorAliveClase2)/len(menor))*100,2) , "% de los pasajeros menores de edad de Clase 2")
#     #clase 3
#     mayorAliveClase3 = mayorAlive[mayorAlive["Pclass"] == 3]
#     menorAliveClase3 = menorAlive[menorAlive["Pclass"] == 3]
#     print("Sobrevivio un",round((len(mayorAliveClase3)/len(mayor))*100,2) , "% de los pasajeros mayores de edad de Clase 3")
#     print("Sobrevivio un",round((len(menorAliveClase3)/len(menor))*100,2) , "% de los pasajeros menores de edad de Clase 3")


print("gracias por estar <3")

# Ejercicio 8

# Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, 
#contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 
# 2016, 2017, 2018 y 2019 respectivamente. Escribir un programa cMon los siguientes requisitos:

#     Generar un DataFrame con los datos de los cuatro ficheros.
#     Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
#     Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
#     Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
#     Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones, contaminantes y fecha.
#     Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
#     Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
#     Mostrar un resumen descriptivo (mímino, máximo, media, etc) para cada contaminante.
#     Mostrar un resumen descriptivo para cada contaminente por distritos.
#     Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estadión indicada.
#     Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
#     Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.
