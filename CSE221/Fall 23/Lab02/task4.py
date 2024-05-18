#Task 4
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def maxTasks(tasks, m):
    mergeSort(tasks)
    count = 0
    result = [0]*m
    for task in tasks:
        for i in range(m):
            if result[i] <= task[0]:
                result[i] = task[1]
                count += 1
                break
    return count


if __name__ == '__main__':
    with open('input4.txt', 'r') as file:
        lines = file.readlines()
        n, m = map(int, lines[0].strip().split())
        tasks = [tuple(map(int, line.strip().split())) for line in lines[1:]]

    with open("output4.txt", "w") as fileout:
        fileout.write(f"{maxTasks(tasks, m)}\n")


'''
Explanation:
To find the maximum number of jobs that M persons can finish, we require a greedy algorithm. 
The mergeSort() function to first arrange the tasks according to their end times. 
Then, it starts a list named "result" to store the end times of tasks allocated to people and a count to keep track of tasks that have been completed.
The maxTasks() function loops over the sorted tasks, checking each one for availability for each person (up to M) if their finish time is less than or equal to the task start time. 
If someone is available, they are given the assignment, and their end time is changed to match with the task's finish time.
'''