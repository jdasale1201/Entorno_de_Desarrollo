// PersonajesMenu.cpp
#include <iostream>
#include <vector>
#include <string>
#include <limits>
using namespace std;

class Personaje {
private:
    string nombre;
    int flechas;
    int vidas;

public:
    // Constructor: por defecto 10 flechas y 10 vidas
    Personaje(const string& n, int f = 10, int v = 10)
        : nombre(n), flechas(f), vidas(v) {}

    const string& getNombre() const { return nombre; }
    int getFlechas() const { return flechas; }
    int getVidas()   const { return vidas; }

    // Disparar: resta 1 flecha si hay
    bool disparar() {
        if (flechas > 0) {
            --flechas;
            return true;
        }
        return false;
    }

    // Recibir impacto: resta 1 vida (no baja de 0)
    void recibirImpacto() {
        if (vidas > 0) --vidas;
    }

    // Medicina: suma 2 vidas
    void medicina() {
        vidas += 2;
    }

    // Imprimir estado
    void imprimir() const {
        cout << "- " << nombre
            << " | Flechas: " << flechas
            << " | Vidas: "   << vidas << '\n';
    }
};

// Utilidad: limpiar entrada si hay errores
void limpiarEntrada() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

// Listar con índices
void listar(const vector<Personaje>& v) {
    cout << "\n=== ESTADO DE LOS PERSONAJES ===\n";
    for (size_t i = 0; i < v.size(); ++i) {
        cout << i << ") ";
        v[i].imprimir();
    }
    cout << "================================\n\n";
}

// Pedir índice de personaje
int pedirIndice(const vector<Personaje>& v, const string& prompt) {
    int idx = -1;
    while (true) {
        cout << prompt;
        if (cin >> idx && idx >= 0 && idx < static_cast<int>(v.size())) {
            return idx;
        }
        cout << "Indice no valido. Intenta de nuevo.\n";
        limpiarEntrada();
    }
}

int main() {
    // Creamos los personajes y los metemos en un vector
    vector<Personaje> personajes;
    personajes.emplace_back("Arquero");
    personajes.emplace_back("Hobbit1");
    personajes.emplace_back("Hobbit2");
    personajes.emplace_back("Hobbit3");

    int opcion = -1;

    do {
        cout << "================ MENU ================\n";
        cout << "1) Disparar (elige quien dispara y quien recibe)\n";
        cout << "2) Medicina (elige quien toma medicina)\n";
        cout << "3) Listar estado de todos\n";
        cout << "0) Salir\n";
        cout << "Elige opcion: ";
        if (!(cin >> opcion)) {
            cout << "Entrada no valida.\n";
            limpiarEntrada();
            continue;
        }

        switch (opcion) {
        case 1: { // Disparar
            listar(personajes);

            int idxAtacante = pedirIndice(personajes, "Quien dispara (indice): ");
            int idxObjetivo  = pedirIndice(personajes, "Quien recibe (indice): ");

            if (idxAtacante == idxObjetivo) {
                cout << "No tiene sentido dispararse a si mismo. Operacion cancelada.\n\n";
                break;
            }

            if (personajes[idxAtacante].disparar()) {
                personajes[idxObjetivo].recibirImpacto();
                cout << personajes[idxAtacante].getNombre() << " dispara a "
                     << personajes[idxObjetivo].getNombre() << "!\n";
            } else {
                cout << personajes[idxAtacante].getNombre()
                     << " no tiene flechas para disparar.\n";
            }
            cout << '\n';
            break;
        }
        case 2: { // Medicina
            listar(personajes);
            int idx = pedirIndice(personajes, "Quien toma la medicina (indice): ");
            personajes[idx].medicina();
            cout << personajes[idx].getNombre() << " toma medicina (+2 vidas).\n\n";
            break;
        }
        case 3: // Listar
            listar(personajes);
            break;

        case 0:
            cout << "Saliendo...\n";
            break;

        default:
            cout << "Opcion no valida.\n\n";
            break;
        }

    } while (opcion != 0);

    return 0;
}
