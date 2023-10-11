"""#ejercicio 1"""
# lista = [1,2,3,4,5]
# lista_portres = map(lambda x: 3*x, lista)
# print(list(lista_portres))

"""ejercicio 2"""
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista3 = [7, 8, 9]


# suma_lista = [sum(x) for x in zip(lista1, lista2, lista3)]

# print(suma_lista)  
"""ejercio 3"""
# lista = ["hola", "mundo"]
# cadenas = [list(lista) for lista in lista]
# print(cadenas)

"""ejercicio 4"""
# def potencia(base,longitud):
#     return[base**i for i in range (longitud)]
# base = int(input("ingrese la base: "))

# longitud = int(input("ingrese las potencias que desea: "))
# lista_de_potencias = potencia(base,longitud)
# print("lista_de_potencias:",lista_de_potencias)

"""ejercicio 5"""
# lista = [4,5,6,2,3,9,1,10,23]
# lista_ordenada = sorted(lista)
# print(lista_ordenada)

"""ejercicio 6"""
# def procesar_secuencia(secuencia):
    
#     mayusculas = secuencia.upper()
#     minusculas = secuencia.lower()

    
#     letras_unicas = ''.join(sorted(set(secuencia), key=secuencia.index))

#     return mayusculas, minusculas, letras_unicas

# # Secuencia determinada
# secuencia = "Hello World"

# # Procesar la secuencia
# mayusculas, minusculas, letras_unicas = procesar_secuencia(secuencia)
# print("Secuencia en mayúsculas:", mayusculas)
# print("Secuencia en minúsculas:", minusculas)
# print("Secuencia con letras únicas:", letras_unicas)

"""ejercicio 7"""
# def suma(lista):
#     suma = sum(lista)
#     return suma

# lista1 = [1,2,3,4,5]
# lista2 = [3,4,5,6,7]
# suma_lista1 = suma(lista1)
# suma_lista2 = suma(lista2)
# diferencia = abs(suma_lista2 - suma_lista1)

# print("la diferencia es: ",diferencia)

"""ejercicio 8"""

# enteros = ['12','1','13','45']
# cadenas = [list(enteros) for enteros in enteros]
# print(cadenas)

"""ejercicio 9"""
# tupla = ('4','5','1','22')
# indices = [0,2,3]
# nueva_lista = [int(tupla[i]) for i in indices]
# print(nueva_lista)

'''ejercicio 10'''
# def serie_fibonacci(n):
#     a,b = 0,1
#     while a<=n:
#         yield a
#         a,b = b,a+b

# def potencia(n):
#     return[x**2 for x in serie_fibonacci(n)]

# n = int(input("ingrese el valor maximo: "))

# cuadrado_fibonacci = potencia(n)
# print(cuadrado_fibonacci)

'''ejercicio 11'''

# matriz = [[1,2,3],
#           [2,3,4],
#           [1,2,3]]

# suma_elementos = sum(sum(fila) for fila in matriz)
# print(suma_elementos)

'''ejercicio 12'''

