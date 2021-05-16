# Ejercicio 1

# Corregir los errores sintácticos del siguiente programa:

# contraseña = input('Introduce la contraseña: ")
# if contraseña in ['sesamo'):
#   print('Pasa')
# else
#   print('No pasa')

#corregido

# contraseña = input('Introduce la contraseña: ')
# if contraseña in ('sesamo'):
#     print('Pasa')
# else:
#     print('No pasa')




# Ejercicio 2

# Detectar y corregir los errores del siguiente programa que aplica el iva a una factura:

# base = input('Introduce la base imponible de la factura: ')
# print(aplica_iva(base, iva))

# def aplica_iva(base, iva = 21):
#     base = base * iva   
#     return base 

#corregido

# base = int(input('Introduce la base imponible de la factura: '))
# iva = 21

# def aplica_iva(base, iva):
#     base = base * iva   
#     return base 

# print(aplica_iva(base, iva))


# Ejercicio 3

# Detectar y corregir los errores del siguiente programa que calcula el 
# producto escalar de dos vectores:

# u = (1, 2, 3)
# v = (4, 5, 6)

# def producto_escalar(u, v):
#     for i in u:
#         u[i+1] *= v[i+1]
#     return sum(u)

# print(producto_escalar(u, v))

#corregido

# u = (1, 2, 3)
# v = (4, 5, 6)

# def producto_escalar(u, v):
#     z = 0
#     for i in range(3):
#         z = z + (u[i] * v[i])
#     return z

# print(producto_escalar(u, v))



# Ejercicio 4

# Detectar y corregir los errores del siguiente programa que devuelve y 
# elimina el teléfono de un listín telefónico a través del nombre del usuario:

# listin = {'Juan':123456789, 'Pedro':987654321}

# def elimina(listin, usuario):
#     del listin[usuario]
#     return listin[usuario]

# print(elimina(listin, 'Pablo'))

#corregido

# listin = {'Juan':123456789, 'Pedro':987654321, 'Pablo':232332313}

# def elimina(listin, usuario):
#     del listin[usuario]
#     return listin

# print(elimina(listin, 'Juan'))


# Ejercicio 5

# Detectar y corregir los errores del siguiente programa que multiplica dos matrices:

# a = ((1, 2, 3),
#      (3, 2, 1))
# b = ((1, 2),
#      (3, 4),
#      (5, 6))

# def producto(a, b):
#     producto = []
#     for i in range(len(b)):
#         fila = []
#         for j in range(len(a[0])):
#             suma = 0
#             for k in range(len(a[0]+1)):
#                 suma += a[i][k] * b[k+1][j]
#             fila[j] = suma
#         producto[i] = tuple(fila)
#     return tuple(producto)

# print(producto(a, b))

#corregido

# a = ((1, 2, 3),
#     (3, 2, 1))
# b = ((1, 2),
#     (3, 4),
#     (5, 6))

# def producto(a, b):
#     suma = [[0,0],[0,0]]
#     for i in range(len(a)):#3
#         for j in range(len(b[0])):#3
#             for k in range(len(b)):
#                 suma[i][j] += a[i][k] * b[k][j]
#                 print(suma[i])
#     return tuple(suma)

# print(producto(a, b))

print("gracias por estar :3")