#include <stdio.h>

int main(void) {
    char nombre[100];

    printf("Introduce tu nombre: ");
    scanf("%99s", nombre);

    for (int i = 0; i < 20; i = i + 1) {
        printf("%s\n", nombre);
    }

    return 0;
}