#include <stdio.h>
#include <stdlib.h>

int addition(int a, int b)
{
    return a + b;
}

int subtraction(int a, int b)
{
    return a - b;
}

int multiplication(int a, int b)
{
    return a * b;
}

int main(void)
{
    int first_num, second_num;
    char operator;

    printf("First Number: ");
    scanf("%d", &first_num);

    printf("Second Number: ");
    scanf("%d", &second_num);

    printf("Operator: ");
    scanf(" %c", &operator);

    if (first_num > second_num)
    {
        printf("Result: %d\n", subtraction(first_num, second_num));
    }
    else if (first_num < second_num)
    {
        printf("Result is: %d\n", addition(first_num, second_num));
    }
    else
    {
        printf("Result is: %d\n", multiplication(first_num, second_num));
    }

    return 0;
}


