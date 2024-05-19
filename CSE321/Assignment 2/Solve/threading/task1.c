#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// onlyprint in a pointer to a function that takes a void pointer and returns a void pointer. it is needed becuase of the pthread_create function.
void *onlyPrint(void *num)
{
    // here (int *) num casting the void pointer to an int pointer. then *(int *) dereferencing it to get the value.
    printf("Thread-%d running\n", *(int *)num);
    printf("Thread-%d closed\n", *(int *)num);
    return NULL;
}

int main()
{
    pthread_t number[5];
    int i;
    for (i = 1; i < 6; i++)
    {
        // here &number[i] will store the p_thread id in the array. onlyPrint is the function that will be called by the thread. &i is the argument that will be passed to the function.
        pthread_create(&number[i], NULL, onlyPrint, &i);
        // pthread_join is used to wait for the thread to terminate. passing NULL cause we don't need the return value of the thread.
        pthread_join(number[i], NULL);
    }
    return 0;
}