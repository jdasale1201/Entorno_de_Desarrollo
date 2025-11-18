#include <iostream>
using namespace std;

int main() {
    double num1, num2; // Se usan double por si el usuario introduce decimales

    cout << "Introduce el primer número: ";
    cin >> num1;

    cout << "Introduce el segundo número: ";
    cin >> num2;

    // Cálculos
    double suma = num1 + num2;
    double resta = num1 - num2;
    double multiplicacion = num1 * num2;

    cout << endl; // Salto de línea
    cout << "Suma: " << suma << endl;
    cout << "Resta: " << resta << endl;
    cout << "Multiplicación: " << multiplicacion << endl;

    // Comprobamos que no se divida entre 0
    if (num2 != 0)
        cout << "División: " << (num1 / num2) << endl;
    else
        cout << "No se puede dividir entre 0." << endl;

    return 0;
}
