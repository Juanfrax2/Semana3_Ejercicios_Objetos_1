class Circulo:
    def __init__(self,radio):
        self.radio=radio


    def calcularArea(self,radio):
        area = int(3.14 *(radio)**2)
        return area
    
    def calcularPerimetro(self,radio):
        perimetro =(2*(3.14))*radio
        return perimetro

    def cambiarRadio(self):
        radio = float(input("Ingrese nuevo radio: "))
        print (f"Nueva Área: {self.calcularArea(radio)}\nNuevo Perímetro: {self.calcularPerimetro(radio)}")

circulo = Circulo(10)

print(circulo.calcularArea(10))
print(circulo.calcularPerimetro(10))
circulo.cambiarRadio()