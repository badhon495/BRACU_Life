#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    char password[50];
    int digit_flag = 0, upper_flag = 0, lower_flag = 0, special_flag = 0;
    int broken_rules_counter, i = 0;

    printf("Enter password: ");
    fgets(password, 50, stdin);

    while (password[i] != '\0')
    {
        if (password[i] >= 'a' && password[i] <= 'z')
        {
            lower_flag = 1;
        }
        else if (password[i] >= 'A' && password[i] <= 'Z')
        {
            upper_flag = 1;
        }
        else if (password[i] >= '0' && password[i] <= '9')
        {
            digit_flag = 1;
        }
        else if (password[i] == '_' || password[i] == '$' || password[i] == '#' || password[i] == '@')
        {
            special_flag = 1;
        }
        i++;
    }

    broken_rules_counter = 4 - (digit_flag + lower_flag + upper_flag + special_flag);

    if (broken_rules_counter == 0)
    {
        printf("OK\n");
    }

    else
    {
        if (upper_flag == 0)
        {
            printf("Uppercase character missing");
            broken_rules_counter--;

            if (broken_rules_counter != 0)
            {
                printf(", ");
            }
        }

        if (lower_flag == 0)
        {
            printf("Lowercase character missing");
            broken_rules_counter--;

            if (broken_rules_counter != 0)
            {
                printf(", ");
            }
        }

        if (digit_flag == 0)
        {
            printf("Digit missing");
            broken_rules_counter--;

            if (broken_rules_counter != 0)
            {
                printf(", ");
            }
        }

        if (special_flag == 0)
        {
            printf("Special character missing");
            broken_rules_counter--;

            if (broken_rules_counter != 0)
            {
                printf(", ");
            }
        }
    }
    printf("\n");
    return 0;
}
