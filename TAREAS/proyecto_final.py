import numpy as np
import matplotlib.pyplot as plt

class Onda:
    def __init__(self, amplitud, frecuencia, fase):
        self.amplitud = amplitud
        self.frecuencia = frecuencia
        self.fase = fase

    def calcular_onda(self, tiempo):
        return self.amplitud * np.sin(2 * np.pi * self.frecuencia * tiempo + self.fase)



# Parámetros de las ondas
amplitud_1 = eval(input("ingrese una amplitud para el movimiento en x: "))
while amplitud_1<0:
    try:
        amplitud_1 = eval(input("ingrese una amplitud positiva:"))
    except ValueError:
        print("ingrese un numero positivo")
    


frecuencia_1 = eval(input("ingrese una frecuencia para el movimiento en x: "))
while frecuencia_1<0:
    try:
        frecuencia_1 = eval(input("ingrese una amplitud positiva:"))
    except ValueError:
        print("ingrese un numero positivo")

fase_1 = eval(input("ingrese una fase para el movimiento en x: "))


amplitud_2 = eval(input("ingrese una amplitud para el movimiento en y: "))
while amplitud_2<0:
    try:
        famplitud_2 = eval(input("ingrese una amplitud positiva:"))
    except ValueError:
        print("ingrese un numero positivo")

frecuencia_2 = eval(input("ingrese la frecuencia para el movimiento en y: "))
while frecuencia_2<0:
    try:
        frecuencia_2 = eval(input("ingrese una amplitud positiva:"))
    except ValueError:
        print("ingrese un numero positivo")
fase_2 = eval(input("ingrese una fase para el movimiento en y: "))

# Direcciones perpendiculares
direccion_x = Onda(amplitud_1, frecuencia_1, fase_1)
direccion_y = Onda(amplitud_2, frecuencia_2, fase_2)

# Generar valores de tiempo
tiempo = np.linspace(0, 2 * np.pi, 1000)

# Calcular los desplazamientos para cada dirección
desplazamiento_x = direccion_x.calcular_onda(tiempo)
desplazamiento_y = direccion_y.calcular_onda(tiempo)

# Graficar la superposición de las ondas en direcciones perpendiculares
plt.figure(figsize=(10, 10))
plt.plot(desplazamiento_x, desplazamiento_y, label='Superposición de ondas en direcciones perpendiculares', color='red')
plt.title('Superposición de Dos Ondas en Direcciones Perpendiculares')
plt.xlabel('Desplazamiento en X')
plt.ylabel('Desplazamiento en Y')
plt.legend(loc='lower right')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()




