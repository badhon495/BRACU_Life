#include <stdio.h>
#include <string.h>

int main(void)
{
    char email[100];
    int i, j, k;

    printf("Enter email address: ");
    scanf("%s", email);

    for (i = 0; i < strlen(email); i++)
    {
        if (email[i] == '@')
        {
            j = i;
            break;
        }
    }

    k = j+1;

    if (email[k] == 'k')
        {
           printf("Email address is outdated\n");
        }
    else
        {
            printf("Email address is okay\n");
        }

    return 0;
}