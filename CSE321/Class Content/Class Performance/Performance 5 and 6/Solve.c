#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int arr[5] = {1, 2, 3, 4, 5};
int max, min, avg;

void *maxF(void *arg)
{
    int i;
    max = arr[0];
    for (i = 1; i < 5; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    printf("Maximum %d\n", max);
}

void *minF(void *arg)
{
    int i;
    min = arr[0];
    for (i = 1; i < 5; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }
    printf("Minimum %d\n", min);
}

void *avgF(void *arg)
{
    int i;
    avg = 0;
    for (i = 0; i < 5; i++)
    {
        avg += arr[i];
    }
    avg /= 5;
    printf("Average %d\n", avg);
}

int main()
{
    pthread_t t1, t2, t3;
    pthread_create(&t1, NULL, maxF, NULL);
    pthread_create(&t2, NULL, minF, NULL);
    pthread_create(&t3, NULL, avgF, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);
    return 0;
}

