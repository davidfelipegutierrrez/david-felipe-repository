# inicio = int(input("ingrese el inicio de la suma:"))
# fin = int(input("ingrese donde termina la suma: "))
# def suma_de_numerosconsecutivos(inicio,fin):
#     if inicio == fin:
#         return inicio
#     else:
#         return inicio + suma_de_numerosconsecutivos(inicio+1,fin)

# resultado = suma_de_numerosconsecutivos(inicio,fin)  
# print(resultado)

X = int(input("ingrese un numero: "))
def suma (x):
    if x == 0:
        return 0
    else:
        return x + suma(x-1)
resultado = suma(X)
print(resultado)
