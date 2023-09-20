class area:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura / 2
        return area
    
base = float(input("ingrese el valor de la base: "))
altura = float(input("ingrese el valor de la altura: "))

mi_rectangulo = area(base,altura)

nueva_area = mi_rectangulo.calcular_area()


print(f"el area de la figura es {nueva_area} unidaades cuadradas.")



    





        


        


    
        

        
        

