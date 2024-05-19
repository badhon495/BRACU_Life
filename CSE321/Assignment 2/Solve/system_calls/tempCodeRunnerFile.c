#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int n = argc - 1;
    int arr[n];
    for (int i = 0; i < n; i++) {
        arr[i] = atoi(argv[i+1]);
    }
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (arr[i] < arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("The sorted array in descending order is:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
   
    printf("\n");
    return 0;
}
