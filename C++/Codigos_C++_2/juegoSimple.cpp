// DemoPersonajes.cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Personaje {
private:
    string nombre;
    int flechas;
    int vidas;

public:
    // Por defecto: 10 flechas y 10 vidas
    Personaje(const string& n, int f = 10, int v = 10)
        : nombre(n), flechas(f), vidas(v) {}

    const string& getNombre() const { return nombre; }
    int getFlechas() const { return flechas; }
    int getVidas()   const { return vidas; }

    // Acciones
    bool disparar() {
        if (flechas > 0) { 
            --flechas; 
            return true; }
        return false;
    }
    void recibirImpacto() { 
        if (vidas > 0)
         --vidas; 
        }
    void medicina() { 
        vidas += 2;
     }

    void imprimir() const {
        cout << nombre << " | Flechas: " << flechas << " | Vidas: " << vidas << '\n';
    }
};

// Función de utilidad para listar todos los personajes
void listar(const vector<Personaje>& lista) {
    cout << "\n=== ESTADO DE LOS PERSONAJES ===\n";
    for (const auto& p: lista) 
       p.imprimir();
    cout << "================================\n";
}

int main() {
    // 1) Crear 4 personajes y meterlos en una lista (vector)
    vector<Personaje> personajes;
    personajes.emplace_back("Arquero");
    personajes.emplace_back("Hobbit1");
    personajes.emplace_back("Hobbit2");
    personajes.emplace_back("Hobbit3");

    // 2) Acciones:
    // - Uno dispara (Arquero)
    if (personajes[0].disparar()) {
        cout << personajes[0].getNombre() << " dispara (pierde 1 flecha)\n";
    } else {
        cout << personajes[0].getNombre() << " no tiene flechas para disparar\n";
    }

    // - Otro recibe un impacto (Hobbit1, distinto del que disparó)
    personajes[1].recibirImpacto();
    cout << personajes[1].getNombre() << " recibe un impacto (-1 vida)\n";

    // - Otro toma medicina (Hobbit2)
    personajes[2].medicina();
    cout << personajes[2].getNombre() << " toma medicina (+2 vidas)\n";

    // 3) Listar todos los personajes
    listar(personajes);

    return 0;
}
