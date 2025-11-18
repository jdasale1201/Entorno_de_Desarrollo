#include <iostream>
#include <vector>  // Necesario para usar std::vector

using namespace std;

// ------------------------------------------------------
// Función que calcula la media de los elementos de un vector
// Parámetro: const vector<double>& v  → se pasa por referencia constante
// Devuelve: la media (double)
// ------------------------------------------------------
double calcularMedia(const vector<double>& v) {
    if (v.empty())  // Si el vector está vacío, devolvemos 0
        return 0.0;

    double suma = 0.0;
    for (double num : v) {  // Recorremos todos los elementos del vector
        suma += num;
    }

    return suma / v.size();  // Media = suma / número de elementos
}

// ------------------------------------------------------
// Programa principal
// ------------------------------------------------------
int main() {
    int n;
    cout << "¿Cuántos números quieres introducir? ";
    cin >> n;

    vector<double> numeros;

    // Leemos los valores
    for (int i = 0; i < n; ++i) {
        double valor;
        cout << "Introduce el número " << i + 1 << ": ";
        cin >> valor;
        numeros.push_back(valor);  // Añadimos al vector
    }

    // Calculamos la media usando la función
    double media = calcularMedia(numeros);

    cout << "\nLa media de los " << n << " números es: " << media << endl;

    return 0;
}
