#include <stdio.h>
#include <string.h>

struct team
{
    char name[20];
    int id;
    int goal[5];
    int total;
};

int main()
{
    struct team t[3];
    int i, j, k, min = 1000, index;
    for (i = 0; i < 3; i++)
    {
        printf("name%d: ", i + 1);
        scanf("%s", t[i].name);
        printf("id %d: ", i + 1);
        scanf("%d", &t[i].id);
        printf("player goal %d: ", i + 1);
        for (j = 0; j < 3; j++)
        {
            scanf("%d", &t[i].goal[j]);
        }
    }
    for (i = 0; i < 3; i++) {
        int total_score = 0;
        for (j = 0; j < 5; j++) {
            total_score += t[i].goal[j];
        }
        if (total_score < min) {
            min = total_score;
            index = i;
        }
    }
    printf("Team %s scored lowest goals.", t[index].name);
    return 0;
}


