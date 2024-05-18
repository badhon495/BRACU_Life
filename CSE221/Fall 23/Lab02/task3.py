#Task 3
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

def intervalScheduling(schedule):
    mergeSort(schedule)
    result = list()
    end_time = 0
    for S, E in schedule:
        if S >= end_time:
            result.append((S, E))
            end_time = E
    return result


if __name__ == '__main__':
  with open("input3.txt", "r") as filein:
      lines = filein.readlines()
      n = int(lines[0])
      data = [list(map(int, line.strip().split())) for line in lines[1:]]

  schedules = intervalScheduling(data)
  with open("output3.txt", "w") as fileout:
      fileout.write(f"{str(len(schedules))}\n")
      for i in schedules:
          fileout.write(f"{i[0]} {i[1]}\n")


'''
Explanation:

A list of intervals is first read by the code from a file. The intervals are then sorted using the merge sort method according to their end times. 
Then, in order to maximize the number of tasks done, it repeatedly iterates through the sorted intervals, choosing tasks with non-overlapping time frames.
The function returns this list, which represents the most tasks that may be finished without overlapping in their timeframes, with the selected intervals stored in the result list.
'''