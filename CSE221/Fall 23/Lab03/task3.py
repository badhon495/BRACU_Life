# Task 3
def countInversion(arr):

    def MERGE_SORT(A, low, high):
        inv_count = 0
        if low < high:
            mid = (low + high) // 2
            inv_count += MERGE_SORT(A, low, mid)
            inv_count += MERGE_SORT(A, mid + 1, high)
            inv_count += MERGE(A, low, mid, high)
        return inv_count

    def MERGE(A, low, mid, high):
        i = low
        j = mid + 1
        k = low
        temp = [None] * len(A)
        inv_count = 0
        while i <= mid and j <= high:
            if A[i] <= A[j]:
                temp[k] = A[i]
                k += 1
                i += 1
            else:
                temp[k] = A[j]
                inv_count += (mid - i + 1)
                k += 1
                j += 1

        while i <= mid:
            temp[k] = A[i]
            k += 1
            i += 1

        while j <= high:
            temp[k] = arr[j]
            k += 1
            j += 1

        for k in range(low, high + 1):
            A[k] = temp[k]

        return inv_count

    return MERGE_SORT(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    with open("input3.txt", "r") as file_in:
        lines = file_in.readlines()
        arr = list(map(int, lines[1].split()))

    with open("output3.txt", "w") as file_out:
        x = countInversion(arr)
        file_out.write(str(x))


'''
Explanation:

I've modified the merge sort algorithm to increment the inversion count each time an unsorted element is encountered. 
It recursively count the left and right side and also count after the merge of left and right. At the end, it returns the inv_count.
Since, it's merge sort, therefore, it maintains i<j and the code is taking O(NlogN) time while executing.   
'''