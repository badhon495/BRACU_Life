#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

int main()
{
    int fd = open("a.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    char buf[100];
    sprintf(buf, "Hello from %d\n", getpid());
    write(fd, buf, strlen(buf));
    sleep(1);
    close(fd);


    return 0;
}