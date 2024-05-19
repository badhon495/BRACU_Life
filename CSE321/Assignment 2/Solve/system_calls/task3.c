#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
int count = 0;
int main()
{
    pid_t a, b, c;
    a = fork();
    b = fork();
    c = fork();
    if (a == 0)
    {
        count++;
        //checking if the process is odd or even
        if (getpid() % 2 != 0)
        {
            fork();
            count++;
        }
    }
    if (b == 0)
    {
        count++;
        if (getpid() % 2 != 0)
        {
            fork();
            count++;
        }
    }
    if (c == 0)
    {
        count++;
        if (getpid() % 2 != 0)
        {
            fork();
            count++;
        }
    }
    printf("Total processes created: %d\n", count);
    return 0;
}