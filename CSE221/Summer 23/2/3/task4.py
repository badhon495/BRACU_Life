def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def kthSmallest(arr, low, high, k):
    if k > 0 and k <= high - low + 1:
        pos = partition(arr, low, high)
        if pos - low == k - 1:
            return arr[pos]
        elif pos - low > k - 1:
            return kthSmallest(arr, low, pos-1, k)
        else:
            return kthSmallest(arr, pos+1, high, k-pos+low-1)
    return None

try :
    with open("input4.txt", "r") as inp_file:
        with open("output4.txt", "w") as out_file:
            store= inp_file.readlines()
            high= int(store[0][0])-1
            loop = int(store[2][0])
            arr = store[1].split()
            for i in range(len(arr)):
                arr[i] = int(arr[i].strip())
            for i in range(loop):
                k= int(store[i+3].strip())
                out_file.write(str(kthSmallest(arr, 0, high, k))+"\n")
                
except Exception:
    pass