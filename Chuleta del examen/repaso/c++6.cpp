#include <iostream>
using namespace std;
int sumaRango(int a, int b){
    int suma =0;
    for (int i=a; i<=b;i=i+1){
        suma = suma + i;
    }
    return suma;
}
int main(){
    int inicio, fin;

    cout << "Introduce numero inicial: ";
    cin >> inicio;
    cout << "Introduce numero final: ";
    cin >> fin;
    cout << "La suma de " << inicio << "hasta" << fin << "es :"<< sumaRango(inicio, fin) << endl;
    return 0;
}