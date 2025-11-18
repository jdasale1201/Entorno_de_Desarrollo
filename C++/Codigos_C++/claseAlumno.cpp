#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Clase muy simple: Alumno
class Alumno {
public:
    string nombre;
    string apellidos;
    int    edad;

    // Constructor
    Alumno(const string& nom, const string& ape, int ed)
        : nombre(nom), apellidos(ape), edad(ed) {}

    // Método para imprimir datos
    void imprimir() const {
        cout << nombre << " " << apellidos << " (" << edad << " años)\n";
    }
};

int main() {
    // Creamos varios alumnos
    Alumno a1("Ana",   "Lopez",   18);
    Alumno a2("Luis",  "Martinez",19);
    Alumno a3("Sara",  "Gomez",   20);

    // Los metemos en una lista (vector)
    vector<Alumno> clase { a1, a2, a3 };

    // Recorremos e imprimimos
    cout << "Listado de alumnos:\n";
    for (const Alumno& alum : clase) {
        alum.imprimir();
    }

    return 0;
}
