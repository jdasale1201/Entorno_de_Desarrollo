#include <stdio.h>
int main(void) {
	int n;
	printf("Introduce tu nota: ");
	scanf_s("%d", &n);
	if (n < 0 || n > 10) {
		printf("La nota debe estar entre 0 y 10");
	}
	else if (n < 5) {
		printf("Insuficiente");
	}
	else if(n < 6){
		printf("Suficiente");
	}
	else if (n < 7) {
		printf("Bien");
	}
	else if(n < 9){
		printf("Notable");
	}
	else {
		printf("Sobresaliente");
	}
	return 0;
}