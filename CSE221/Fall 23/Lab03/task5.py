# Task 5
def QUICK_SORT(A, low, high):
    if low <= high:
        q = PARTITION(A, low, high)
        QUICK_SORT(A, low, q - 1)
        QUICK_SORT(A, q + 1, high)
    return A

def PARTITION(A, low, high):
    x = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1


if __name__ == '__main__':
    with open('input5.txt', 'r') as file_in:
        lines = file_in.readlines()
        N = int(lines[0])
        arr = list(map(int, lines[1].split()))

    with open("output5.txt", "w") as file_out:
        file_out.write(" ".join([str(i) for i in QUICK_SORT(arr, 0, N-1)]))


'''
Explanation:

Just wrote the entire pseudo code in python :"D
This sort works by taking a list and creating a partition. The partition then picks a value to create a pivot 
It then moves all values lower then it to the left side and all values greater than it to the right.
It then creates sub-lists from each side of the partition and preforms the same operation on them until sorted.
While one of the most efficient it can be horribly inefficient if a poor pivot is chosen
'''