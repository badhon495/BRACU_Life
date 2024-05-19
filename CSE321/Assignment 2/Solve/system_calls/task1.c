#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

//taking input from user. here argc is the number of arguments and argv is the array of arguments. here two arguments are passed. so argc will be two. and in argv, argv[0] is the name of this file and arv[1] is the name of the file to be opened.
int main(int argc, char* argv[])
{
    int fd;
    char buffer[100];
    //opening the file in read, write and append mode. if the file does not exist, it will be created with the giving all the permissions.
    char* filename = argv[1];
    fd = open(filename, O_RDWR | O_APPEND | O_CREAT, 0777);
    if(fd == -1)
    {
        printf("Error opening file\n");
        exit(1);
    }

    printf("Enter a string: ");
    fgets(buffer, 100, stdin);
    //checking if the user entered -1 with the help of strcmp function. if the user entered -1, the loop will break and the file will be closed.
    while(strcmp(buffer, "-1\n") != 0)
    {
        write(fd, buffer, strlen(buffer));
        printf("Enter a string: ");
        fgets(buffer, 100, stdin);
    }
    close(fd);
    return 0;
}