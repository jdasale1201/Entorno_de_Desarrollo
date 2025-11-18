#include <stdio.h>

double sumar(double a, double b, double c){
    return a + b + c;
}

double resta(double a, double b, double c){
    return a - b - c;
}

double multiplicar(double a, double b, double c){
    return a * b * c;
}
int main(){
    double n1, n2, n3;

    printf("Ingrese 3 numeros decimales: ");
    scanf("%lf %lf %lf", &n1, &n2, &n3);

    printf("Resultados: \n");
    printf("La suma es: %.2lf\n", sumar(n1, n2, n3));
    printf("La resta es: %.2lf\n", resta(n1, n2, n3));
    printf("La multiplicacion es: %.2lf", multiplicar(n1, n2, n3));
    return 0;
}