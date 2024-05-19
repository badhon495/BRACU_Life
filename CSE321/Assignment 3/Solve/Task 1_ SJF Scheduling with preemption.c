#include <stdio.h>
#include <stdlib.h>

struct process
{
    int pid, at, bt, ct, tat, wt, r_bt;
};

void sort(struct process p[], int total_p)
{
    int i, j;
    for (i = 0; i < total_p - 1; i++)
        for (j = 0; j < total_p - i - 1; j++)
            if (p[j].at > p[j + 1].at)
            {
                struct process temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
}

int main()
{
    int total_p;
    printf("Enter the number of processes: ");
    scanf("%d", &total_p);
    struct process p[total_p];
    
    int i;
    for (i = 0; i < total_p; i++)
    {
        printf("Enter the arrival time of process %d: ", i + 1);
        scanf("%d", &p[i].at);
        printf("Enter the burst time of process %d: ", i + 1);
        scanf("%d", &p[i].bt);
        p[i].pid = i + 1;
        p[i].r_bt = p[i].bt;
    }
    
    // p is processes array and total_p is total number of processes
    sort(p, total_p);

    int time = 0;
    int count = 0;
    int min = 1000;
    int index = -1;
    while (count < total_p)
    {
        for (i = 0; i < total_p; i++)
        {
            if (p[i].at <= time && p[i].r_bt < min && p[i].r_bt > 0)
            {
                min = p[i].r_bt;
                index = i;
            }
        }
        if (index != -1)
        {
            p[index].r_bt--;
            if (p[index].r_bt == 0)
            {
                count++;
                p[index].ct = time + 1;
                p[index].tat = p[index].ct - p[index].at;
                p[index].wt = p[index].tat - p[index].bt;
                min = 1000;
                index = -1;
            }
        }
        time++;
    }
    
    printf("PID\tAT\tBT\tCT\tTAT\tWT\n");
    for (i = 0; i < total_p; i++)
    {
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", p[i].pid, p[i].at, p[i].bt, p[i].ct, p[i].tat, p[i].wt);
    }
    return 0;
}
