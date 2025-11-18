#include <iostream>
#include <string>
#include <vector>

using namespace std;
class Pokemon {
public:
    string nombre;
    int vidas;
    int ubicacionX;
    int ubicacionY;
    string color;

    Pokemon(string n, int v, int x, int y, string  c){
        nombre = n;
        vidas = v;
        ubicacionX = x;
        ubicacionY = y;
        color = c;
    }

    void gritar(){
        cout << nombre << " dice: !Viva el IES Rafael Alberti¡" << endl;
    }
    void moverse(int direccionX, int direccionY){
        ubicacionX = ubicacionX + direccionX;
        ubicacionY = ubicacionY + direccionY;
        cout << nombre << "Se ha movido un poco a " << ubicacionX << "," << ubicacionY;
    }
    void imprimirdatos(){
        cout << "Nombre:" << nombre << endl;
        cout << "vidas:" << vidas << endl;
        cout << "Ubicacion: (" << ubicacionX << "," << ubicacionY << ")" << endl;
        cout << "Color: " << color << endl;
    }
    void jamacuco(){
        if(vidas > 0){
            vidas--;
            cout << nombre << "ha sufrido un jamacuco y tiene " << vidas << "restantes" <<endl;
        }else{
            cout << nombre << "ya no tiene vidas." << endl;
        }
    }
};
int main(){
    vector<Pokemon> listaPokemonsGaditanos;

    listaPokemonsGaditanos.push_back(Pokemon("Pikachu", 7, 2, 3, "amarillo"));
    listaPokemonsGaditanos.push_back(Pokemon("Charmander", 6, -1, 0, "rojo"));
    listaPokemonsGaditanos.push_back(Pokemon("Psyduck", 5, 10, -2, "amarillo"));
    listaPokemonsGaditanos.push_back(Pokemon("Bulbasaur", 8, 4, 4, "verde"));

    cout << "=== Pokemons de color amarillo ===" << endl;
    for (auto &p : listaPokemonsGaditanos) {
        if (p.color == "amarillo") {
            p.imprimirdatos();
        }
}
cout << endl << "=== Pikachu grita ===" << endl;
    listaPokemonsGaditanos[0].gritar();

    cout << endl << "=== Bulbasaur se mueve (+6, -7) ===" << endl;
    listaPokemonsGaditanos[3].moverse(6, -7);

    cout << endl << "=== A Charmander le da un jamacuco ===" << endl;
    listaPokemonsGaditanos[1].jamacuco();

    cout << endl << "=== Listado final de todos los Pokemons ===" << endl;
    for (auto &p : listaPokemonsGaditanos) {
        p.imprimirdatos();
    }

    return 0;
}