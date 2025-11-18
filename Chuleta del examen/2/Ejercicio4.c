#include <stdio.h>

int main(void) {
	int n;
	printf("Introduce un numero entero: ");
	scanf_s("%d", &n);
	if (n % 2 == 0) {
		printf("Es un numero par");
	}
	else {
		printf("Es un numero impar");
	}
	return 0;
}