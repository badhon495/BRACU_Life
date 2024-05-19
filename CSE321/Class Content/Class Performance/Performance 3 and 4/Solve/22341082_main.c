#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <stdlib.h>

int main()
{
    pid_t pid = fork();
    if (pid == 0)
    {
        execl("./a.out", "a.out", NULL);
    }
    else
    {
        wait(NULL);
        FILE *fp = fopen("a.txt", "r");
        char buf[100];
        while (fgets(buf, 100, fp) != NULL)
        {
            printf("%s", buf);
        }
        close(fp);
    }
    return 0;
}