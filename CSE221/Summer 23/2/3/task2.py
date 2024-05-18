def max_sum(A):
    max_sum = float('-inf')
    max_value = float('-inf')

    for i in range(len(A)):
        max_sum = max(max_sum, max_value + A[i] ** 2)
        max_value = max(max_value, A[i])

    return max_sum

try :
    with open("input2.txt", "r") as inp_file:
        with open("output2.txt", "w") as out_file:
            store= inp_file.readlines()
            arr = store[1]
            arr = arr.split()
            for i in range(len(arr)):
                arr[i] = int(arr[i].strip())
            x = max_sum(arr)
            out_file.write(str(x))

except Exception:
  pass