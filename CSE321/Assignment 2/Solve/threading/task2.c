#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *threads(void *num)
{
    int i;
    for (i = 0; i < 5; i++)
    {
        // typecasting the void pointer to an int pointer. then dereferencing it to get the value.
        printf("Thread %d prints %d\n", *(int *)num, *(int *)num * 5 + i + 1);
    }
    return NULL;
}

int main()
{
    pthread_t number[5];
    int i;
    for (i = 0; i < 6; i++)
    {
        // &number[i] will store the p_thread id in the array. threads is the function that will be called by the thread. &i is the argument that will be passed to the function.
        pthread_create(&number[i], NULL, threads, &i);
        // pthread_join is used to wait for the thread to terminate. passing NULL cause we don't need the return value of the thread.
        pthread_join(number[i], NULL);
    }
    return 0;
}
