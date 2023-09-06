class MRU:
    def __init__(self,posicion_inicial,velocidad_inicial):
        self.posicion = posicion_inicial
        self.velocidad = velocidad_inicial

    def calcular_posicion(self,tiempo):
        nueva_posicion = self.posicion + self.velocidad * tiempo
        return nueva_posicion
    
velocidad_inicial = float(input("ingresa la velocidad inicial(m/s): "))
posicion_inicial = float(input("ingresar la posicion inicial(m): "))
tiempo = float(input("ingresar el tiempo(s): "))

objeto_mru = MRU(posicion_inicial, velocidad_inicial)
nueva_posicion = objeto_mru.calcular_posicion(tiempo)

print(f"la nueva posicion del objeto despues de {tiempo} segundos es {nueva_posicion} metros")