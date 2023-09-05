#include <iostream>
#include <cmath>

class Circulo {
private:
    float radio;
public:
    Circulo(float r){
        radio=r;
    }
    float calcularArea(){
        float area = 3.14 * pow(radio,2);
        return area;
    }
    float calcularPerimetro(){
        float perimetro = (2*3.14)*radio;
        return perimetro;

    }
    void cambiarRadio(){
        float nuevoRadio;
        std::cout <<"Ingrese nuevo radio: ";
        std::cin >> nuevoRadio;
        std::cout << "Nueva Area: " << calcularArea()<< "\nNuevo Perimetro: " << calcularPerimetro() << std::endl;
    }
};

int main () {
    Circulo circulo(10);

    std::cout << circulo.calcularArea() << std::endl;
    std::cout << circulo.calcularPerimetro() << std::endl;
    circulo.cambiarRadio();

    return 0;     
}
