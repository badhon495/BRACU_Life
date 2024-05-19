#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    pid_t pid = fork();

    if (pid < 0)
    {
        perror("Fork failed");
        exit(1);
        // passing the arguments to the sort program. made mistake that i had to make sure i compile the sort.c or oddeven.c file first
    }
    else if (pid == 0)
    {
        // using execvp because i want to pass the arguments to the sort program
        execvp("./sort", argv);
    }
    else
    {
        wait(NULL);
        execvp("./oddeven", argv);
    }

    return 0;
}
