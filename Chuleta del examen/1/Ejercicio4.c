#include <stdio.h>

int main(void) {
    int numero;
    int suma = 0;

    printf("Introduce numeros mayores que 0 (introduce 0 para terminar):\n");

    scanf("%d", &numero);

    while (numero > 0) {
        suma += numero;
        scanf("%d", &numero);
    }

    printf("La suma de los numeros introducidos es: %d\n", suma);

    return 0;
}