#include <stdio.h>
int main(void) {
	float n[10] = { 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10 };
	float suma = 0.0;
	float minimo = n[0];
	float maximo = n[0];
	for (int i = 0; i < 10; i++) {
		suma += n[i];
		if (n[i] < minimo) {
			minimo = n[i];
		}
		if (n[i] > maximo) {
			maximo = n[i];
		}
	}
	float media = suma / 10;
	printf("La suma es %.2f\n", suma);
	printf("La media es %.2f\n", media);
	printf("El minimo es %.2f\n", minimo);
	printf("El maximo es %2.f\n", maximo);

	return 0;
}