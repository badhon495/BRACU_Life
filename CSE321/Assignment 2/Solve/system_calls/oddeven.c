#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int n = argc - 1;
    int arr[n];
    for (int i = 0; i < n; i++) {
        arr[i] = atoi(argv[i+1]);
    }
    printf("Odd numbers: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\nEven numbers: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\n");
    return 0;
}
