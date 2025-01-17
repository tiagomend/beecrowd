#include <stdio.h>

double average_one()
{
    double a, b;
    double weight_of_a = 3.5, weight_of_b = 7.5;
    double media;

    // Lê os valores de entrada
    scanf("%lf", &a);
    scanf("%lf", &b);

    // Calcula a média ponderada
    media = (a * weight_of_a + b * weight_of_b) / (weight_of_a + weight_of_b);

    // Retorna o valor da média
    return media;
}

int main()
{
    double result = average_one();
    // Exibe o resultado formatado
    printf("MEDIA = %.5f\n", result);
    return 0;
}
