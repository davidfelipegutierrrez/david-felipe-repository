def decorador(funcion):
    def nueva_funcion(x,y):
        print("es par?")
        c = funcion(x,y)
        print("si, es par")
        return c
    return nueva_funcion

@decorador
def suma(x,y):
    print(2+4)
    return x + y

suma(2,4)