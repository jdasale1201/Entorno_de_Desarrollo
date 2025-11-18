#include <iostream>
using namespace std;

// ==== FUNCIONES ====
float sumar(float a, float b) {
    return a + b;
}

float restar(float a, float b) {
    return a - b;
}

float multiplicar(float a, float b) {
    return a * b;
}

float dividir(float a, float b) {
    if (b == 0) {
        cout << "Error: no se puede dividir entre 0." << endl;
        return 0;
    }
    return a / b;
}

// ==== PROGRAMA PRINCIPAL ====
int main() {
    int opcion;
    float num1, num2;

    do {
        cout << "\n===== CALCULADORA BASICA =====" << endl;
        cout << "1. Sumar" << endl;
        cout << "2. Restar" << endl;
        cout << "3. Multiplicar" << endl;
        cout << "4. Dividir" << endl;
        cout << "5. Salir" << endl;
        cout << "Elige una opcion: ";
        cin >> opcion;

        if (opcion >= 1 && opcion <= 4) {
            cout << "Introduce el primer numero: ";
            cin >> num1;
            cout << "Introduce el segundo numero: ";
            cin >> num2;
        }

        switch (opcion) {
            case 1:
                cout << "Resultado: " << sumar(num1, num2) << endl;
                break;
            case 2:
                cout << "Resultado: " << restar(num1, num2) << endl;
                break;
            case 3:
                cout << "Resultado: " << multiplicar(num1, num2) << endl;
                break;
            case 4:
                cout << "Resultado: " << dividir(num1, num2) << endl;
                break;
            case 5:
                cout << "Saliendo de la calculadora..." << endl;
                break;
            default:
                cout << "Opcion no valida. Intenta de nuevo." << endl;
        }

    } while (opcion != 5);

    return 0;
}