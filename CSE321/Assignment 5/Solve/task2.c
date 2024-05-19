//same everything as previous code, just took an array named safe and placed the value whenever it finished it tasks

#include <stdio.h>
#include <stdbool.h>

void subtract_matrix(int rows, int cols, int mat_a[][cols], int mat_b[][cols], int mat_res[][cols])
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            mat_res[i][j] = mat_a[i][j] - mat_b[i][j];
        }
    }
}

bool is_less_than_or_equals(int length, int array_a[], int array_b[])
{
    for (int i = 0; i < length; i++)
    {
        if (array_a[i] > array_b[i])
        {
            return false;
        }
    }
    return true;
}

void add_array_values(int length, int array_a[], int array_b[], int array_res[])
{
    for (int i = 0; i < length; i++)
    {
        array_res[i] = array_a[i] + array_b[i];
    }
}

int main()
{
    int n = 6;                        // Number of processes
    int m = 4;                        // Number of resources
    int alloc[6][4] = {{0, 1, 0, 3},  // P0	// Allocation Matrix
                       {2, 0, 0, 3},  // P1
                       {3, 0, 2, 0},  // P2
                       {2, 1, 1, 5},  // P3
                       {0, 0, 2, 2},  // P4
                       {1, 2, 3, 1}}; // P5

    int max[6][4] = {{6, 4, 3, 4},  // P0	// MAX Matrix
                     {3, 2, 2, 4},  // P1
                     {9, 1, 2, 6},  // P2
                     {2, 2, 2, 8},  // P3
                     {4, 3, 3, 7},  // P4
                     {6, 2, 6, 5}}; // P5

    int avail[4] = {2, 2, 2, 1}; // Available resources

    int need[n][m];
    subtract_matrix(n, m, max, alloc, need);

    bool finished[n];
    for (int i = 0; i < n; i++)
    {
        finished[i] = false;
    }

    int safe[n]; //initializing this array to keep track which process is finishing first

    int count = 0;
    while (count < n)
    {
        bool found = false;
        for (int p = 0; p < n; p++)
        {
            if (finished[p] == false && is_less_than_or_equals(m, need[p], avail))
            {
                add_array_values(m, avail, alloc[p], avail);
                finished[p] = true;
                safe[count] = p; //after finishing the process, adding the process number here
                found = true;
                count++;
            }
        }

        if (found == false)
        {
            printf("Deadlock Ahead\n");
            return 0;
        }
    }

    printf("Safe Sequence is: "); //printing safe sequence

    for (int i = 0; i < n; i++)
    {
        printf("P%d ", safe[i]);
    }
    printf("\n");
    return 0;
}