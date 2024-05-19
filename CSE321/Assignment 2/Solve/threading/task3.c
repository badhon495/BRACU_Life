#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

int asciiSum(char *str)
{
    int sum = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        sum += str[i];
    }
    return sum;
}

void *thread(void *str)
{
    // allocating memory for the result
    int *result = malloc(sizeof(int));
    int sum = asciiSum(str);
    // dereferencing the void pointer and storing the result in the allocated memory
    *result = sum;
    // returning the pointer to the allocated memory
    pthread_exit(result);
}

int main()
{
    char str1[100], str2[100], str3[100];

    printf("Enter first string: ");
    fgets(str1, 100, stdin);
    printf("Enter second string: ");
    fgets(str2, 100, stdin);
    printf("Enter third string: ");
    fgets(str3, 100, stdin);

    pthread_t thread1, thread2, thread3;
    int *result1, *result2, *result3;

    // passing the address of the string to the thread function and storing it in the thread1 variable.
    pthread_create(&thread1, NULL, thread, str1);
    pthread_create(&thread2, NULL, thread, str2);
    pthread_create(&thread3, NULL, thread, str3);

    // here first pointer used to get the memory address of the returned (result) pointer and second is to store the memory address to this functions result1 variable.
    pthread_join(thread1, (void **)&result1);
    pthread_join(thread2, (void **)&result2);
    pthread_join(thread3, (void **)&result3);

    // checking if all the three strings have the same ascii sum
    if (*result1 == *result2 && *result2 == *result3)
    {
        printf("Youreka\n");
    }
    else if (*result1 == *result2 || *result2 == *result3 || *result1 == *result3)
    {
        printf("Miracle\n");
    }
    else
    {
        printf("Hasta la vista\n");
    }

    free(result1);
    free(result2);
    free(result3);
    return 0;
}
