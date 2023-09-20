# class MRU:
#     def __init__(self,posicion_inicial,velocidad_inicial):
#         self.posicion = posicion_inicial
#         self.velocidad = velocidad_inicial

#     def calcular_posicion(self,tiempo):
#         nueva_posicion = self.posicion + self.velocidad * tiempo
#         return nueva_posicion
    
# velocidad_inicial = float(input("ingresa la velocidad inicial(m/s): "))
# posicion_inicial = float(input("ingresar la posicion inicial(m): "))
# tiempo = float(input("ingresar el tiempo(s): "))

# objeto_mru = MRU(posicion_inicial, velocidad_inicial)
# nueva_posicion = objeto_mru.calcular_posicion(tiempo)

# print(f"la nueva posicion del objeto despues de {tiempo} segundos es {nueva_posicion} metros")

# def f(x):
#     return 2*x
# y = f(int(input("ingrese un valor: ")))
# print(y) 

# def funcion(y):
#     return 6*y + 2**y
# x = funcion(int(input("ingrese un valor: ")))
# print(x)

# def di_hola(nombre):
#     print("hola", nombre)
# di_hola("david")

# def mi_decorador(funcion):
#     def nueva_funcion(a, b):
#         print("Se va a llamar")
#         c = funcion(a, b)
#         print("Se ha llamado")
#         return c
#     return nueva_funcion

# @mi_decorador
# def suma(a, b):
#     print("Entra en funcion suma")
#     return a + b

# suma(5,8)

def decorador(funcion):
    def nueva_funcion(x,y):
        print("es par?")
        c = funcion(x,y)
        print("si es par")
        return c
    return nueva_funcion

@decorador
def suma(x,y):
    print(2+4)
    return x + y

suma(2,4)