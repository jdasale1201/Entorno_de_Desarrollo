#include <stdio.h>
int main(void) {
	float n, suma = 0;
	printf("Introduce un numero: ");
	scanf_s("%f", &n);
	while (n != 0) {
		if (n > 0) {
			suma += n;
		}
		else {
			printf("Solo numeros positivos\n");
		}
		printf("Introduce otro numero(0 para terminar)\n");
		scanf_s("%f", &n);
	}
	printf("La suma total es: %.2f\n", suma);
	return 0;
}
