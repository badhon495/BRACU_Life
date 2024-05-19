#include <stdio.h>
#include <stdlib.h>

struct process
{
    int pid, at, bt, ct, tat, wt, r_bt, priority;
};

void sort(struct process p[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - i - 1; j++)
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
        printf("Enter the priority of process %d: ", i + 1);
        scanf("%d", &p[i].priority);
        p[i].pid = i + 1;
        p[i].r_bt = p[i].bt;
    }

    sort(p, total_p);
    int time = 0;
    int count = 0;
    int min = 1000;
    int index = -1;

    while (count < total_p)
    {
        for (i = 0; i < total_p; i++)
        {
            if (p[i].at > time)
            {
                break;
            }
            else if (p[i].priority < min && p[i].r_bt > 0)
            {
                min = p[i].priority;
                index = i;
            }
        }
        if (index == -1)
        {
            time++;
            continue;
        }
        else
        {
            p[index].r_bt--;
            time++;
            if (p[index].r_bt == 0)
            {
                p[index].ct = time;
                count++;
                min = 1000;
                index = -1;
            }
        }
    }
    
    for (i = 0; i < total_p; i++)
    {
        p[i].tat = p[i].ct - p[i].at;
        p[i].wt = p[i].tat - p[i].bt;
    }
    printf("PID\tAT\tBT\tCT\tTAT\tWT\tPriority\n");
    
    for (i = 0; i < total_p; i++)
    {
        printf("%d\t%d\t%d\t%d\t%d\t%d\t%d\n", p[i].pid, p[i].at, p[i].bt, p[i].ct, p[i].tat, p[i].wt, p[i].priority);
    }
    return 0;
}