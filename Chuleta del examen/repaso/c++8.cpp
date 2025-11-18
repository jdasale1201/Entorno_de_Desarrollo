#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(){
    vector<string> alumnos;
    string nombres;
    int cantidad;
    cout << "Cuantos alumnos quieres meter:? ";
    cin >> cantidad;
    cin.ignore();

    for(int i = 0; i < cantidad; i=i+1){
        cout << "Introduce el nombre del alumno" << i + 1 << ":";
        getline(cin, nombres);
        alumnos.push_back(nombres);
    }
    cout << "\nLista de alumnjos registrados: \n";
    for (int i = 0; i < alumnos.size(); i= i + 1){
        cout << i + 1 << "." << alumnos[i] << endl;
    }
    return 0;
}