#include <stdio.h>

int main() {
    float n1, n2, n3, media;
    printf("Pon tus tres notas: ");
    scanf("%f %f %f", &n1, &n2, &n3);
    // Validar que las notas estén entre 0 y 10
    if (n1 < 0 || n1 > 10 || n2 < 0 || n2 > 10 || n3 < 0 || n3 > 10) {
        printf("Las notas deben estar entre 0 y 10.\n");
    } else {
        media = (n1 + n2 + n3) / 3;
        printf("Tu media es: %.2f\n", media);
    }
    return 0;
}
