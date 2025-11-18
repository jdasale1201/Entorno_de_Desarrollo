// MenuPersonajes.cpp
#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <algorithm>

using namespace std;

class Personaje {
private:
    string nombre;
    int flechas;
    int vidas;

public:
    Personaje(const string& n, int f = 10, int v = 10)
        : nombre(n), flechas(f), vidas(v) {}

    const string& getNombre() const { return nombre; }
    int getFlechas() const { return flechas; }
    int getVidas()   const { return vidas; }

    bool disparar() {
        if (flechas > 0) { --flechas; return true; }
        return false;
    }
    void recibirImpacto() { if (vidas > 0) --vidas; }
    void medicina() { vidas += 2; }

    void imprimir() const {
        cout << nombre << " | Flechas: " << flechas << " | Vidas: " << vidas;
    }
};

/* ==================== utilidades de entrada ==================== */
void limpiarEntrada() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

string pedirLinea(const string& prompt) {
    cout << prompt;
    string s;
    getline(cin >> ws, s); // ws consume espacios y saltos previos
    return s;
}

int pedirEntero(const string& prompt) {
    int x;
    while (true) {
        cout << prompt;
        if (cin >> x) { limpiarEntrada(); return x; }
        cout << "Entrada no valida. Intenta de nuevo.\n";
        limpiarEntrada();
    }
}

/* ==================== operaciones sobre el vector ==================== */
void listar(const vector<Personaje>& v) {
    if (v.empty()) { cout << "No hay personajes.\n\n"; return; }
    cout << "\n=== LISTA DE PERSONAJES ===\n";
    for (size_t i = 0; i < v.size(); ++i) {
        cout << i << ") ";
        v[i].imprimir();
        cout << '\n';
    }
    cout << "===========================\n\n";
}

int buscarPorNombre(const vector<Personaje>& v, const string& nombre) {
    for (size_t i = 0; i < v.size(); ++i) {
        if (v[i].getNombre() == nombre) return static_cast<int>(i);
    }
    return -1;
}

int pedirIndicePersonaje(const vector<Personaje>& v, const string& prompt) {
    if (v.empty()) { cout << "No hay personajes.\n"; return -1; }
    int idx;
    while (true) {
        idx = pedirEntero(prompt);
        if (idx >= 0 && idx < static_cast<int>(v.size())) return idx;
        cout << "Indice invalido. Rango: 0.." << (int)v.size()-1 << "\n";
    }
}

/* ==================== acciones del menu ==================== */
void accionCrear(vector<Personaje>& v) {
    string nombre = pedirLinea("Nombre del nuevo personaje: ");
    if (nombre.empty()) { cout << "Nombre vacio. Cancelado.\n\n"; return; }

    if (buscarPorNombre(v, nombre) != -1) {
        cout << "Ya existe un personaje con ese nombre.\n\n";
        return;
    }
    v.emplace_back(nombre); // por defecto 10 flechas y 10 vidas
    cout << "Creado: ";
    v.back().imprimir();
    cout << "\n\n";
}

void accionDisparar(vector<Personaje>& v) {
    if (v.size() < 2) { cout << "Se necesitan al menos 2 personajes.\n\n"; return; }
    listar(v);
    int iAtacante = pedirIndicePersonaje(v, "Indice del atacante: ");
    int iObjetivo = pedirIndicePersonaje(v, "Indice del objetivo: ");
    if (iAtacante == -1 || iObjetivo == -1) return;
    if (iAtacante == iObjetivo) { cout << "No puedes dispararte a ti mismo.\n\n"; return; }

    if (v[iAtacante].disparar()) {
        v[iObjetivo].recibirImpacto();
        cout << v[iAtacante].getNombre() << " dispara a " << v[iObjetivo].getNombre() << ".\n";
    } else {
        cout << v[iAtacante].getNombre() << " no tiene flechas.\n";
    }
    cout << '\n';
}

void accionMedicina(vector<Personaje>& v) {
    if (v.empty()) { cout << "No hay personajes.\n\n"; return; }
    listar(v);
    int idx = pedirIndicePersonaje(v, "Indice del personaje que toma medicina: ");
    if (idx == -1) return;
    v[idx].medicina();
    cout << v[idx].getNombre() << " toma medicina (+2 vidas).\n\n";
}

void accionListar(const vector<Personaje>& v) {
    listar(v);
}

void accionEncontrar(const vector<Personaje>& v) {
    if (v.empty()) { cout << "No hay personajes.\n\n"; return; }
    string nombre = pedirLinea("Nombre a buscar: ");
    int idx = buscarPorNombre(v, nombre);
    if (idx == -1) {
        cout << "No se encontro el personaje \"" << nombre << "\".\n\n";
    } else {
        cout << "Encontrado en indice " << idx << ": ";
        v[idx].imprimir();
        cout << "\n\n";
    }
}

/* ==================== menu principal ==================== */
int mostrarMenuYLeerOpcion() {
    cout << "============== MENU ==============\n"
         << "1) Crear personaje\n"
         << "2) Disparar flecha\n"
         << "3) Tomar medicina\n"
         << "4) Listar personajes\n"
         << "5) Encontrar personaje\n"
         << "6) Salir\n"
         << "==================================\n";
    return pedirEntero("Elige opcion: ");
}

int main() {
    vector<Personaje> personajes;

    // Si quieres partir con algunos por defecto, descomenta:
    // personajes.emplace_back("Arquero");
    // personajes.emplace_back("Hobbit1");
    // personajes.emplace_back("Hobbit2");
    // personajes.emplace_back("Hobbit3");

    while (true) {
        int op = mostrarMenuYLeerOpcion();
        cout << '\n';
        switch (op) {
            case 1: accionCrear(personajes);      break;
            case 2: accionDisparar(personajes);   break;
            case 3: accionMedicina(personajes);   break;
            case 4: accionListar(personajes);     break;
            case 5: accionEncontrar(personajes);  break;
            case 6: cout << "Hasta luego!\n"; return 0;
            default: cout << "Opcion invalida.\n\n"; break;
        }
    }
}
