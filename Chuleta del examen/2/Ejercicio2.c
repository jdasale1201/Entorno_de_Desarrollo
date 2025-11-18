#include <stdio.h>
int main(void) {
	
	int edad;
	double nota;
	char inicial;

	printf("Introduce tu edad: ");
	scanf_s("%d", &edad);

	printf("Introduce tu nota media: ");
	scanf_s("%lf", &nota);

	printf("Introduce tu inicial: ");
	scanf_s(" %c", &inicial, 1);

	printf("Tienes %d años, tu nota media es de %.2lf y tu inicial es %c.\n", edad, nota, inicial);
	
	return 0;
}