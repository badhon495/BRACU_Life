#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int i, j, flag = 0;
    char *input_word = malloc(10 * sizeof(char));

    // char *input_word;
    printf("Enter a Word: ");
    scanf("%s", input_word);

    int length = strlen(input_word);

    for (i = 0, j = length - 1; i < length / 2; i++, j--)
    {
        if (*(input_word+ i) != *(input_word+ j))
        {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
    {
        printf("Not Palindrome\n");
    }
    else
    {
        printf("Palindrome\n");
    }

    return 0;
}
