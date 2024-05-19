#include <stdio.h>
#include <stdbool.h>

void subtract_matrix(int rows, int cols, int mat_a[][cols], int mat_b[][cols], int mat_res[][cols]) // substracting allcoation from max and puting those values in need.
{
    for (int i = 0; i < rows; i++) // changing row
    {
        for (int j = 0; j < cols; j++) // changing colum
        {
            mat_res[i][j] = mat_a[i][j] - mat_b[i][j];
        }
    }
}

bool is_less_than_or_equals(int length, int array_a[], int array_b[]) // compairing between need and available. if need becomes bigger than the available then it will return false
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

void add_array_values(int length, int array_a[], int array_b[], int array_res[]) //
{
    for (int i = 0; i < length; i++)
    {
        array_res[i] = array_a[i] + array_b[i];
    }
}

int main()
{
    int n = 5;                        // Number of processes
    int m = 4;                        // Number of resources
    int alloc[5][4] = {{0, 1, 0, 3},  // P0	// Allocation Matrix
                       {2, 0, 0, 0},  // P1
                       {3, 0, 2, 0},  // P2
                       {2, 1, 1, 5},  // P3
                       {0, 0, 2, 2}}; // P4

    int max[5][4] = {{6, 4, 3, 4},  // P0	// MAX Matrix
                     {3, 2, 2, 1},  // P1
                     {9, 1, 2, 6},  // P2
                     {2, 2, 2, 8},  // P3
                     {4, 3, 3, 7}}; // P4

    int avail[4] = {3, 3, 2, 1}; // Available resources

    int need[n][m];
    subtract_matrix(n, m, max, alloc, need); // calculating need

    bool finish[n]; // array to track if the process finished or not
    for (int i = 0; i < n; i++)
    {
        finish[i] = false;
    }

    int count = 0; // increasing count whenever a process finished
    while (count < n)
    {
        bool found = false;
        for (int p = 0; p < n; p++)
        {
            if (finish[p] == false && is_less_than_or_equals(m, need[p], avail)) // checking if the process is already finished and need is less than available
            {
                add_array_values(m, avail, alloc[p], avail); // adding the alocated resource to available
                finish[p] = true;                            // flaging it as finished
                found = true;                                // making found true, as it will tell that some process did finished
                count++;
            }
        }

        if (found == false) // if the whole for loop runs and no process finished then this condition wll be true which make this a deadlock
        {
            printf("Deadlock Ahead\n");
            return 0;
        }
    }

    printf("Safe here\n"); // if everything goes well it will print
    return 0;
}