#include <stdio.h>
int main(void) {
	int n;
	printf("Introduce un numero: ");
	scanf_s("%d", &n);

	if (n < 1 || n > 10) {
		printf("El numero debe estar entre 1 y 10");
	}
	else {
		printf("Tabla de cuadrados hasta %d.\n");
		for (int i = 1; i <= n; i++) {
			printf("%d^2 = %d\n", i, i * i);
		}
	}
	return 0;
}