#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // substracting 1 from argc because the first argument is the name of the program
    int n = argc - 1;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        // converting the string to integer using atoi. i+1 because the first argument is the name of the program and i am starting from 0
        arr[i] = atoi(argv[i + 1]);
    }
    // bubble sort
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] < arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("The sorted array in descending order is:\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");
    return 0;
}
