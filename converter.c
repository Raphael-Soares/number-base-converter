#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int to_decimal(char number[20], int base) {
    int decimal = 0;
    int length = strlen(number);

    // Inicializa 'i' corretamente
    for (int i = 0; i < length; i++) {
        int value;
        if (number[i] >= '0' && number[i] <= '9') {
            value = number[i] - '0';
        } else if (number[i] >= 'A' && number[i] <= 'F') {
            value = number[i] - 'A' + 10;
        } else if (number[i] >= 'a' && number[i] <= 'f') {
            value = number[i] - 'a' + 10;
        } else {
            printf("Número inválido para a base %d.\n", base);
            exit(1);
        }
        decimal = decimal * base + value;
    }

    return decimal;
}

char* to_base(int decimal, int base) {
    char digits[] = "0123456789ABCDEF";
    char result[64]; // Array temporário para armazenar o resultado
    int index = 0;

    // Verifica se o número decimal é 0
    if (decimal == 0) {
        char* zero = (char*)malloc(2 * sizeof(char));
        strcpy(zero, "0");
        return zero;
    }

    // Converte o número para a base
    while (decimal > 0) {
        result[index++] = digits[decimal % base];
        decimal /= base;
    }

    // Adiciona o terminador nulo à string
    result[index] = '\0';

    // Inverte o resultado
    char* final_result = (char*)malloc((index + 1) * sizeof(char));
    for (int i = 0; i < index; i++) {
        final_result[i] = result[index - i - 1];
    }
    final_result[index] = '\0'; // Adiciona o terminador nulo

    return final_result;
}

int main() {
    int base_inicial;
    int base_final;
    char numero[20];

    printf("De qual base deseja converter?\n");
    scanf("%d", &base_inicial);

    printf("Para qual base deseja converter?\n");
    scanf("%d", &base_final);

    printf("Qual número deseja converter?\n");
    scanf("%s", numero);  // Corrigido para ler string com %s

    if (base_inicial == 10) {
        int decimal = atoi(numero);  // Converte a string para inteiro
        char* resultado = to_base(decimal, base_final);
        printf("Resultado: %s\n", resultado);
        free(resultado);  // Libera a memória alocada
    } else {
        int resultado_decimal = to_decimal(numero, base_inicial);
        char* resultado = to_base(resultado_decimal, base_final);
        printf("Resultado: %s\n", resultado);
        free(resultado);  // Libera a memória alocada
    }

    return 0;
}

