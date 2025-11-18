#include <iostream>
using namespace std;

int main(void) {
    int numero, cuadrado;
    cout << "Introduce un numero: ";
    cin >> numero;
    cuadrado = numero * numero;
    cout << "El cuadrado de " << numero << " es " << cuadrado << endl;
    return 0;
}