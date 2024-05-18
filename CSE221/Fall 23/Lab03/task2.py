# Task 2
def MAXIMUM(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high ) // 2
    left = MAXIMUM(arr, low, mid)
    right = MAXIMUM(arr, mid + 1, high)
    return max(left, right)


if __name__ == "__main__":
    with open("input2.txt", "r") as file_in:
        lines = file_in.readlines()
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))

    with open("output2.txt", "w") as file_out:
      file_out.write(str(MAXIMUM(arr, 0, n - 1)))


'''
Explanation:

This algorithm the complexing, where N is the lists length, is O(NLogN). 
This is due to the lists repeated division into halves and comparison at each level of the highest value from each half.
The recursion has logN levels. Since, we perform a fixed amount of work at each level, the overall time complexity is 0(NLogN).
'''