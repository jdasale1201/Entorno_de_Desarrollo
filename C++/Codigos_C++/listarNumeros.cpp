#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Lista de números (puedes cambiarla o pedirlos al usuario)
    vector<int> numeros {3, 7, 10, 21, 42};

    cout << "Listado de numeros:\n";
    for (int n : numeros) {            // for-each (C++11+)
        cout << n << "\n";
    }

    return 0;
}
