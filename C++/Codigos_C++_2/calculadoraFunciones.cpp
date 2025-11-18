// CalculadoraFunciones.cpp
#include <iostream>
#include <iomanip>  //Para establecer formatos y precision
#include <cmath>     // fmod para resto en doubles
using namespace std;

// ---- Operaciones básicas que devuelven el resultado ----
double sumar(double a, double b)        { return a + b; }
double restar(double a, double b)       { return a - b; }
double multiplicar(double a, double b)  { return a * b; }

// ---- División: devuelve "cociente" y "resto" por referencia ----
// Devuelve true si la división es válida (b != 0), false si no se puede dividir.
bool dividir(double a, double b, double& cociente, double& resto) {
    if (b == 0.0) return false;
    cociente = a / b;
    // Para doubles, el "resto" se calcula con fmod (resto = a - b*entero? no exacto con reales)
    resto = fmod(a, b);
    return true;
}

int main() {
    cout << fixed << setprecision(2); // Formato con 2 decimales

    double x, y;
    cout << "Introduce el primer numero (double): ";
    cin >> x;
    cout << "Introduce el segundo numero (double): ";
    cin >> y;

    cout << "\n--- Resultados ---\n";
    cout << "Suma:            " << sumar(x, y) << '\n';
    cout << "Resta:           " << restar(x, y) << '\n';
    cout << "Multiplicacion:  " << multiplicar(x, y) << '\n';

    double coc = 0.0, res = 0.0;
    if (dividir(x, y, coc, res)) {
        cout << "Division:        " << coc << '\n';
        cout << "Resto (fmod):    " << res << '\n';
    } else {
        cout << "Division:        no se puede dividir entre 0\n";
    }

    return 0;
}
