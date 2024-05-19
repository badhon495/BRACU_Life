#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <stdbool.h>

void* block1(void* arg)
{
        for(int i = 1; i <= 5; i++)
        {
                //sleep(1);
                printf("%d. I am Thread-1.\n", i);
        }
        return NULL;
}

void* block2(void* arg)
{
        for(int i = 1; i <= 10; i++)
        {
                //sleep(1);
                printf("%d. I am Thread-2.\n", i);
        }
}

void default_thread()
{
        for(int i = 1; i <= 5; i++)
        {
                sleep(1);
                printf("%d. I am Default Thread.\n", i);
        }
}
//Introduction to thread
int main_1()
{
        pthread_t thread1;

        /* Attribute-1: pointer to an unsigned integer value that returns the thread id of the thread created
        Attribute-2: pointer to a structure that is used to define thread attributes like detached state, scheduling policy, stack address, etc. Set to NULL for default thread attributes.
        Attribute-3: pointer to a subroutine that is executed by the thread. The return type and parameter type of the subroutine must be of type void *. The function has a single attribute but if multiple values need to be passed to the function, a struct must be used.
        Attribute-4: pointer to void that contains the arguments to the function defined in the earlier argument
        */

        pthread_create(&thread1, NULL, block1, NULL);
        default_thread();


        /*pthread_join does two things:
        1. Wait for the termination of a thread.
        2. Clean up any resources associated with the thread.
        */
        pthread_join(thread1, NULL);

	return 0;
}

//Introduction to multithread
int main_2()
{
        pthread_t thread1, thread2;

        pthread_create(&thread1, NULL, block1, NULL);
        pthread_create(&thread2, NULL, block2, NULL);

        pthread_join(thread1, NULL);
        pthread_join(thread2, NULL);

	return 0;
}


/*===========================================================================================*/

// Creating multiple threads using loop without parallel execution

int var = 0;
void* block3(void* arg)
{
	var++;
}

int main_3()
{
	pthread_t thread [3];
	for (int i = 0; i < 3; i++)
	{
		pthread_create(&thread[i], NULL, block3, NULL);
		pthread_join(thread[i], NULL);
		printf("Thread: %d has started running.\n", i);
		printf("Thread: %d has ended.\n", i);
	}

	printf("The threads have all ended and var is: %d.\n", var);
}


/*===========================================================================================*/


// Creating multiple threads using loop with parallel execution


int main_4()
{
	pthread_t thread [3];
	for (int i = 0; i < 3; i++)
	{
		pthread_create(&thread[i], NULL, block3, NULL);
		printf("Thread: %d has started running.\n", i);
	}

	for (int i = 0; i < 3; i++)
	{
		pthread_join(thread[i], NULL);
		printf("Thread: %d has ended.\n", i);
	}

	printf("The threads have all ended and var is: %d.\n", var);
}


/*===========================================================================================*/


//Revising processes and child processes
int checker = 0;

int main_5()
{
        int hold = fork(); //Creates a child process and hold = 0 for the child

        if(hold == 0)
        {
        	checker++;
                printf("I am the child. My name is %d. My parent is: %d.\n", getpid(), getppid());
                printf("I have been assigned checker no.: %d.\n", checker);
        }

        if (hold != 0)
        {
        	printf("I will pause till my child is done.\n");
        	wait(NULL);
                printf("I am the parent. My name is %d.\n", getpid());
                printf("I have been assigned checker no.: %d.\n", checker);
        }
        printf("Final stage: My process ID is: %d.\n", getpid());
        printf("Checker no: %d signing off.\n", checker);
}


/*===========================================================================================*/


//Checking process IDs inside multiple threads
void* block4(void* arg)
{
	printf("This is thread-1. My process ID is: %d.\n", getpid());
}

void* block5(void* arg)
{
	printf("This is thread-2. My process ID is: %d.\n", getpid());
}

int main_6()
{
	pthread_t thread1,  thread2;

        pthread_create(&thread1, NULL, block4, NULL);
        pthread_create(&thread2, NULL, block5, NULL);

        pthread_join(thread1, NULL);
        pthread_join(thread2, NULL);

        printf("The threads have exited. The default process ID is: %d.\n", getpid());

	return 0;
}


/*===========================================================================================*/


//Checking variables inside multiple threads
int t_checker = 0;

void* block6(void* arg)
{
	t_checker++;
	printf("The value of Thread-1 Checker is: %d.\n", t_checker);
}

void* block7(void* arg)
{
	sleep(1);
	printf("The value of Thread-2 Checker is: %d.\n", t_checker);
}

int main_7()
{
        pthread_t thread1,  thread2;

        pthread_create(&thread1, NULL, block6, NULL);
        pthread_create(&thread2, NULL, block7, NULL);

        pthread_join(thread1, NULL);
        pthread_join(thread2, NULL);

	return 0;
}


/*===========================================================================================*/


//Passing arguments to threads

int arr [2] = {10, 20};

void* adder(void* arg)
{
	int *index = arg;
	int sum = index[0] + index[1];
	printf("I am Thread: 1 performing addition.\n") ;
	sleep(1);
	printf("The sum is: %d.\n", sum);
}

void* subtracter(void* arg)
{
	int *index = arg;
	int diff = index[1] - index[0];
	printf("I am Thread: 2 performing subtraction.\n");
	printf("The difference is: %d.\n", diff);
}


int main_9()
{
	pthread_t thread1, thread2;

	pthread_create(&thread1, NULL, adder, (void* )arr);
	pthread_create(&thread2, NULL, subtracter, (void* )arr);

	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);
}

/*===========================================================================================*/


//Get return value from a thread

void* block9(int *n)
{

	printf("Entered the Thread.\n");
	if(*n % 2 == 0)
	{
		pthread_exit("Odd");
	}
	else
	{
		pthread_exit("Even");
	}
}

int num = 10;
void* thread_return;

int main_10()
{
	pthread_t thread1;

	pthread_create(&thread1, NULL, (void*)block9, &num); //try without (void*)
	pthread_join(thread1, &thread_return);

	printf("Thread returned: %s\n", (char*)thread_return);

	return 0;
}


/*===========================================================================================*/


