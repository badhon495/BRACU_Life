#include<stdio.h>

//struct is a user defined data type. it can hold multiple data types. it is similar to class in python
struct breakfast{
    int quantity;
    int unit_price;
};

int main(){
    struct breakfast paratha, vegetable, mineral_water;
    
    printf("Quantity Of Paratha: ");
    scanf("%d", &paratha.quantity);
    printf("Unit Price: ");
    scanf("%d", &paratha.unit_price);
    printf("Quantity Of Vegetables: ");
    scanf("%d", &vegetable.quantity);
    printf("Unit Price: ");
    scanf("%d", &vegetable.unit_price);
    printf("Quantity Of Mineral Water: ");
    scanf("%d", &mineral_water.quantity);
    printf("Unit Price: ");
    scanf("%d", &mineral_water.unit_price);

//i could have created a function to calculate the total bill.
    int total_bill = (paratha.quantity * paratha.unit_price) + (vegetable.quantity * vegetable.unit_price) + (mineral_water.quantity * mineral_water.unit_price);

    int number_of_people;
    printf("Number of People: ");
    scanf("%d", &number_of_people);
    
    float individual_bill = total_bill / number_of_people;
    printf("Individual people will pay: %.2f tk\n", individual_bill);
    return 0;
}