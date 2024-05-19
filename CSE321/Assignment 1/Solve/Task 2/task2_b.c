#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *input_file, *output_file;
    char i;

    input_file = fopen("task2_b_input.txt", "r");
    output_file = fopen("task2_b_output.txt", "w");

    if (input_file == NULL)
    {
        exit(1);
    }

    while ((i = fgetc(input_file)) != EOF)
    {
        if (i == ' ')
        {
            fputc(i, output_file);
            while ((i = fgetc(input_file)) == ' ')
            {
                continue;
            }
        }
        fputc(i, output_file);
    }

    fclose(input_file);
    fclose(output_file);

    return 0;
}