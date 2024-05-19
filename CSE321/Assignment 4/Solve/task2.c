#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

// defining some constants
#define MaxCrops 5
#define warehouseSize 5

sem_t empty; // for sending signal to the farmer that warehouse is empty

sem_t full; // for sending signal to the shop owner that warehouse is full

int in = 0; // only accessed by farmer
int out = 0; // only accessed by shop owner

char crops[5] = {'R', 'W', 'P', 'S', 'M'}; //readonly

char warehouse[5] = {'N', 'N', 'N', 'N', 'N'}; //editing

pthread_mutex_t mutex; // defining mutex

void *Farmer(void *far)
{
    int *farNo = (int *)far; // casting the void pointer to int pointer and dereferencing it and storing it in farNo variable. here we are getting 0 as farmar id.

    for (int i = 0; i < MaxCrops; i++) // running the loop 5 times
    {
        sem_wait(&empty); // checking if the warehouse is empty
        
        pthread_mutex_lock(&mutex); // locking the mutex
        
        warehouse[in] = crops[i]; // inserting the crop in the warehouse

        printf("Farmer %d: Insert crops %c at %d\n", *farNo, crops[i], in);

        in = (in + 1) % warehouseSize; // increasing the in variable and moding it with warehouseSize to make sure it is not going out of bound

        pthread_mutex_unlock(&mutex); // unlocking the mutex

        sem_post(&full); // sending signal to the shop owner that warehouse is full
    }

    // after inserting all the crops printing the updated warehouse
    printf("Farmer%d: ", *farNo + 1); //farmar id
    
    //running loop to print NNNNN
    for (int j = 0; j < warehouseSize; j++)
    {
        printf("%c", warehouse[j]);
    }
    printf("\n");
    pthread_exit(NULL);
}


void *ShopOwner(void *sho)
{
    int *shoNo = (int *)sho; // casting the void pointer to int pointer and dereferencing it and storing it in shoNo variable. here we are getting 0 as shop owner id.

    for (int i = 0; i < MaxCrops; i++) // running the loop 5 times
    {
        sem_wait(&full); // checking if the warehouse is full

        pthread_mutex_lock(&mutex); // locking the mutex

        char crop = warehouse[out]; // getting the crop from the warehouse

        warehouse[out] = 'N'; // removing the crop from the warehouse
        
        printf("Shop owner %d: Remove crops %c from %d\n", *shoNo, crop, out);
        
        out = (out + 1) % warehouseSize; // increasing the out variable and moding it with warehouseSize to make sure it is not going out of bound
        
        pthread_mutex_unlock(&mutex);
        sem_post(&empty); // sending signal to the farmer that warehouse is empty
    }
    
    printf("ShopOwner%d: ", *shoNo + 1);
    for (int j = 0; j < warehouseSize; j++) // printing the updated warehouse NNNNN
    {
        printf("%c", warehouse[j]);
    }
    printf("\n");

    pthread_exit(NULL);
}



int main()
{
    pthread_t farmers[5], shopOwners[5]; // creating array of threads

    pthread_mutex_init(&mutex, NULL); // initializing the mutex

    sem_init(&empty, 0, warehouseSize);//when the warehouse is full then farmer will wait

    sem_init(&full, 0, 0); // when the warehouse is empty then shop owner will wait

    int a[5] = {1, 2, 3, 4, 5}; // array of farmer and shop owner id

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&farmers[i], NULL, Farmer, &a[i]);
        pthread_create(&shopOwners[i], NULL, ShopOwner, &a[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        pthread_join(farmers[i], NULL);
        pthread_join(shopOwners[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty); // 
    sem_destroy(&full);

    return 0;
}
