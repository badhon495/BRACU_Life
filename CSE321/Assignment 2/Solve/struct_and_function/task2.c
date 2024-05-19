#include <stdio.h>
#include <stdbool.h>

//checking every numbers sum of divisors. if it is equal to the number, it is a perfect number
int isPerfect(int number){
    int sum = 0;
    for(int i = 1; i < number; i++){
        if(number % i == 0){
            sum += i;
        }
    }
    if(sum == number){
        return 1;
    }
    return 0;
}

int main(){
    int start, end;
    scanf("%d", &start);
    scanf("%d", &end);
    for(int i = start; i <= end; i++){
        if(isPerfect(i)){
            printf("%d\n", i);
        }
    }
    return 0;
}