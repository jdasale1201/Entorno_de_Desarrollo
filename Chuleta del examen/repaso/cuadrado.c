#include <stdio.h>
int cuadrado(int a){
    return a * a;
}
int main(){
    int numero;

    printf("Introduce un numero del 1 al 10: ");
    scanf("%d", &numero);
    if (numero < 1 || numero > 10) {
		printf("El numero debe estar entre 1 y 10.\n");
	}
	else { int resultado = cuadrado(numero);
        printf("Cuadrados del 1 a %d", numero);
        for(int i= 1; i <= numero; i = i+1){
            int a = cuadrado(i);
            printf("Los cuadrados hasta %d son: %d\n",i ,a);
        }
    }
    return 0;
}