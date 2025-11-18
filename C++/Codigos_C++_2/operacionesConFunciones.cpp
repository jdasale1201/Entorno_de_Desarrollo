#include <iostream>
using namespace std;

// Declaración de funciones

void mensaje(){

    cout<<"Hola buenas tardes Cadiz\n"<<"Que tengais buena tarde\n";
}


double sumarDAM(double a, double b) {
   
   
   // cout<<"Hola buenas tardes\n"; 
    return a + b; 
}
double restar(double a, double b)
{ 
  return a - b;
}
double multiplicar(double a, double b)  { return a * b; }
double dividir(double a, double b)     
 { 
    return a / b;
 } // comprobar en main

int main() {
    double x, y;
    mensaje();4
    cout << "Introduce el primer numero: ";
    cin >> x;
    cout << "Introduce el segundo numero: ";
    cin >> y;

    cout << "\nResultados:\n";
    cout << "Suma: " << sumarDAM(x, y) << "\n";
    cout << "Resta: " << restar(x, y) << "\n";
    cout << "Multiplicacion: " << multiplicar(x, y) << "\n";

    if (y != 0)
        cout << "Division: " << dividir(x, y) << "\n";
    else
        cout << "Division: no se puede dividir entre 0\n";

    return 0;
}
