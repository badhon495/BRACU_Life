#include <pthread.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

// just defining some constants
#define MAX 10
#define BUFLEN 6
#define NUMTHREAD 2

// changed int to void. did not had to do that but it was throwing warning.
void *consumer(void *id);
void *producer(void *id);

// creating array which will only contian the characters
char buffer[BUFLEN]; // editing
char source[BUFLEN]; // readonly
int pCount = 0; // editing
int cCount = 0; // editing
int buflen;

pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER; // protect shared data. which is pCount and cCount

pthread_cond_t nonEmpty = PTHREAD_COND_INITIALIZER;      // checking a condition. which is buffer is not empty

pthread_cond_t full = PTHREAD_COND_INITIALIZER;          // checking a condition. which is buffer is not full


// creating array of thread ids
int thread_id[NUMTHREAD] = {0, 1};
int i = 0;
int j = 0;

int main()
{
    int i;
    // creating array of threads
    pthread_t thread[NUMTHREAD];

    // copying the string to varibale named source and storing its length in buflen
    strcpy(source, "abcdef");
    buflen = strlen(source);

    // sending first thread to producer function and second to consumer function. to run it concurrently we created two threads at the same time.
    pthread_create(&thread[0], NULL, producer, (void *)&thread_id[0]);
    pthread_create(&thread[1], NULL, consumer, (void *)&thread_id[1]);

    // joining the threads
    pthread_join(thread[0], NULL);
    pthread_join(thread[1], NULL);

    return 0;
}

void *producer(void *arg)
{
    // casting the void pointer to int pointer and dereferencing it and storing it in id variable. here we are getting 0 as producer id.
    int *id = (int *)arg;
    
    //producer will run 10 times
    for (int i = 0; i < MAX; i++)
    {
        pthread_mutex_lock(&count_mutex); // locking the mutex
        
        while (pCount == BUFLEN) // checking if the buffer is full or not
        {
            pthread_cond_wait(&full, &count_mutex); // waiting for the buffer to be empty
        }
        buffer[pCount] = source[i % BUFLEN]; // storing the character in the buffer
        
        printf("%d produced %c by Thread %d\n", i, buffer[pCount], *id);
        pCount++; // increasing the pCount
        
        pthread_cond_signal(&nonEmpty); // sending signal to the consumer that buffer is not empty
        
        pthread_mutex_unlock(&count_mutex); // unlocking the mutex
        
        sleep(1); // slowing down the producer
    }
    return NULL;
}

void *consumer(void *arg)
{

    int *id = (int *)arg; // getting the consumer id. here we are getting 1 as consumer id.
   
    for (int i = 0; i < MAX; i++) // consumer will run 10 times
    {
        pthread_mutex_lock(&count_mutex); //while consuming we have to lock the mutex
       
       while (pCount == 0)  // checking if the buffer is empty or not
        {
            pthread_cond_wait(&nonEmpty, &count_mutex);
        }

        printf("%d consumed %c by Thread %d\n", i, buffer[0], *id); // printing the character
        
        for (int j = 0; j < pCount - 1; j++)
        {
            buffer[j] = buffer[j + 1]; // shifting the characters to the left
        }

        pCount--; // decreasing the pCount

        pthread_cond_signal(&full); // sending signal to the producer that buffer is not full
        
        pthread_mutex_unlock(&count_mutex); // unlocking the mutex
        
        sleep(1); // slowing down the consumer
    }
    return NULL;
}