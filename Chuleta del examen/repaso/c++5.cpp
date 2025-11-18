#include <iostream>
using namespace std;
int main(){
    float farenheit, celsius;
    cout << "Introduce la temperatura en celsius: ";
    cin >> celsius;
    farenheit = (celsius * 9/5)+ 32;
    cout << "Equivale a " << farenheit << "grados farenheit." << endl;
    return 0;
}