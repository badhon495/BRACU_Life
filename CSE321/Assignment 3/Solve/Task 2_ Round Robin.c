#include <stdio.h>
#include <stdlib.h>

struct process
{
    int pid, bt, ct, tat, wt, r_bt;
};

int main()
{
    int total_p;
    printf("Enter the number of processes: ");
    scanf("%d", &total_p);
    struct process p[total_p];
    
    int i;
    for (i = 0; i < total_p; i++)
    {
        printf("Enter the burst time for process %d: ", i + 1);
        scanf("%d", &p[i].bt);
        p[i].pid = i + 1;
        p[i].r_bt = p[i].bt;
    }
    
    int tq;
    printf("Enter the time quantum: ");
    scanf("%d", &tq);
    
    int time = 0;
    int count = 0;
    int j;
    while (count != total_p)
    {
        for (i = 0; i < total_p; i++)
        {
            if (p[i].r_bt == 0)
            {
                continue;
            }
            else if (p[i].r_bt > tq)
            {
                p[i].r_bt = p[i].r_bt - tq;
                time = time + tq;
            }
            else
            {
                time = time + p[i].r_bt;
                p[i].r_bt = 0;
                p[i].ct = time;
                count++;
            }
        }
    }
    
    for (i = 0; i < total_p; i++)
    {
        p[i].tat = p[i].ct;
        p[i].wt = p[i].tat - p[i].bt;
    }
    printf("PID\tBT\tCT\tTAT\tWT \n");

    for (i = 0; i < total_p; i++)
    {
        printf("%d\t%d\t%d\t%d\t%d\n", p[i].pid, p[i].bt, p[i].ct, p[i].tat, p[i].wt);
    }
    return 0;
}
