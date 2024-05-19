#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    // pid_t create a variable that can store process id
    pid_t pid, pid2;
    pid = fork();
    if (pid == 0)
    {
        pid2 = fork();
        if (pid2 == 0)
        {
            printf("I am grandchild\n");
        }
        else
        {   //using wait to wait for the child process to finish
            wait(NULL);
            printf("I am child\n");
        }
    }
    else
    {
        wait(NULL);
        printf("I am parent\n");
    }
    return 0;
}