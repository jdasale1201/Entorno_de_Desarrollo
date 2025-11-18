#include <stdio.h>

int main(void) {
    int numero;

    printf("Introduce un numero del 1 al 10: ");
    scanf("%d", &numero);

        if (numero < 1) {
            printf("Debe ser un numero mayor o igual a 1\n");
    } else if (numero > 10) {
            printf("Debe ser un numero mayor o igual a 10\n");
    
    } else {
    for (int i = 1; i <= 10; i = i + 1) {
        printf("%d x %d = %d\n", numero, i, numero * i);
    }
}

    return 0;
}