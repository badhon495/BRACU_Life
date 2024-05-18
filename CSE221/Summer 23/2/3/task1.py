
def count_inversions(arr):
    def merge_sort(arr, temp_arr, left, right):
        inv_count = 0

        if left < right:
            mid = (left + right) // 2

            inv_count += merge_sort(arr, temp_arr, left, mid)
            inv_count += merge_sort(arr, temp_arr, mid + 1, right)
            inv_count += merge(arr, temp_arr, left, mid, right)

        return inv_count

    def merge(arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                k += 1
                j += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1

        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1

        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]

        return inv_count

    n = len(arr)
    temp_arr = [0] * n
    return merge_sort(arr, temp_arr, 0, n - 1)

try :
    with open("input1.txt", "r") as inp_file:
        with open("output1.txt", "w") as out_file:
            store= inp_file.readlines()
            arr = store[1]
            arr = arr.split()
            for i in range(len(arr)):
                arr[i] = int(arr[i].strip())
            x = count_inversions(arr)
            out_file.write(str(x))

except Exception:
  pass