#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
// not calling wait in the parent process. so the parent process will print output before the child process and the child process will be adopted by init process.
int main()
{
    pid_t pid = fork();

    if (pid == 0)
    {
        printf("2. Child process ID: %d\n", getpid());
        pid_t pid1 = fork();
        if (pid1 == 0)
        {
            printf("3. Grand Child process ID: %d\n", getpid());
            exit(0);
        }

        pid_t pid2 = fork();
        if (pid2 == 0)
        {
            printf("4. Grand Child process ID: %d\n", getpid());
            exit(0);
        }

        pid_t pid3 = fork();
        if (pid3 == 0)
        {
            printf("5. Grand Child process ID: %d\n", getpid());
            exit(0);
        }
    }
    else
    {
        printf("1. Parent process ID: %d\n", getpid());
    }
    return 0;
}