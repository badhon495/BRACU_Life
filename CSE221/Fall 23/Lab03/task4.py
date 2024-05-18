# Task 4
def MAX_SUM(A):
    max_sum = float('-inf')
    max_value = float('-inf')
    for i in range(len(A)):
        max_sum = max(max_sum, max_value + A[i] ** 2)
        max_value = max(max_value, A[i])
    return max_sum


if __name__ == "__main__":
    with open("input4.txt", "r") as file_in:
        lines = file_in.readlines()
        arr = lines[1]
        arr = arr.split()

    with open("output4.txt", "w") as file_out:
        for i in range(len(arr)):
            arr[i] = int(arr[i].strip())
        x = MAX_SUM(arr)
        file_out.write(str(x))


'''
Explanation:

I aimed to achieve an O(N) time complexity for this task.
That's why, I assigned two variables: one to denote the maximum sum and another for the maximum value.
The reason for tracking the maximum value is that we directly add it to calculate the max_sum.
'''