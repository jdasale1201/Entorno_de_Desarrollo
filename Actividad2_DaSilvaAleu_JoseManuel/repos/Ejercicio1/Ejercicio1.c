#include <stdio.h>

int main(void) {
	int numero = 34;
	float numero_decimal = 6.2;
	double decimal_largo = 8.123456;
	char letra = 'J';

	printf("Numero entero (int): %d\n", numero);
	printf("Numero decimal (float): %f\n", numero_decimal);
	printf("Decimal largo (double): %lf\n", decimal_largo);
	printf("Letra /char): %c\n", letra);

	return 0;
}