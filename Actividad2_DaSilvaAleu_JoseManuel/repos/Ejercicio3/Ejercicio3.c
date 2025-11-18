#include <stdio.h>
int main(void){

	int a, b;

	printf("Introduce el primer entero: ");
	scanf_s("%d", &a);

	printf("Introduce segundo entero: ");
	scanf_s("%d", &b);

	int suma = a + b;
	int resta = a - b;
	int producto = a * b;
	
	if (b != 0) {
		int cociente_entero = a / b;
		int resto = a % b;
		double cociente_real = a / b;

		printf("La suma es %d\n", suma);
		printf("La resta es %d\n", resta);
		printf("El producto es %d\n", producto);
		printf("Cociente entero es %d\n", cociente_entero);
		printf("El resto es %d\n", resto);
		printf("Cociente real es %lf", cociente_real);
	}
	else {
		printf("Error, no se puede dividir entre 0.\n");
	}
	return 0;
}

