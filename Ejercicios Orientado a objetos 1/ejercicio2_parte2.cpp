#include <iostream>

class Rectangulo{
private:
    float longitud;
    float ancho;

public:
    Rectangulo(float l, float a){
        longitud=l;
        ancho=a;
    }


    float calcularArea(){
        float area = longitud * ancho;
        return area; 
    } 

    float calcularPerimetro(){
        float perimetro = (2*longitud)+(2*ancho);
        return perimetro;
    }

    void cambiarLongitud() {
        std::cout << "Ingresa la nueva longitud: ";
        std::cin >> longitud;
    }

    void cambiarAncho(){
        std::cout << "Ingresa el nuevo ancho: ";
        std::cin >> ancho;
    }
};

int main() {
    Rectangulo rectangulo(5,6);

    std::cout <<"Area: "<< rectangulo.calcularArea()<< std::endl;
    std::cout <<"Perimetro: "<< rectangulo.calcularPerimetro()<< std::endl;

    rectangulo.cambiarLongitud();
    rectangulo.cambiarAncho();

    std::cout <<"Nueva Area: "<< rectangulo.calcularArea()<< std::endl;
    std::cout <<"Nuevo Perimetro: " << rectangulo.calcularPerimetro()<< std::endl;
    return 0;

}
