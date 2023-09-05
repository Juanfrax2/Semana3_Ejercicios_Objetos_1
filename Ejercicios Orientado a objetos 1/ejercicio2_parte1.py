class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud=longitud
        self.ancho=ancho

    def calcularArea(self, longitud,ancho):
        area = longitud * ancho
        return area

    def calcularPerimetro(self, longitud,ancho):
        perimetro = (2*longitud)+(2*ancho)
        return perimetro
    
    def cambiarLongitud(self):
        self.longitud = float(input("Ingresa nueva longitud: "))
        
    def cambiarAncho(self):
        self.ancho = float(input("Ingresa nuevo ancho: "))
        print(f"Nueva Área: {rectangulo.calcularArea(self.longitud,self.ancho)}\nNuevo Perímetro: {rectangulo.calcularPerimetro(self.longitud,self.ancho)} ")

rectangulo = Rectangulo(5,6)  
print(rectangulo.calcularArea(5,6))
print(rectangulo.calcularPerimetro(5,6))
rectangulo.cambiarLongitud()
rectangulo.cambiarAncho() 
