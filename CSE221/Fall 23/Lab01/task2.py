#Task 2

def bubbleSort(List, n):
  for i in range(n-1):
    flag = False
    for j in range(n-i-1):
      if List[j] > List[j+1]:
        flag = True
        List[j], List[j+1] = List[j+1], List[j]
    if flag == False:
      break
  return List


if __name__ == '__main__':
  with open('input2.txt', 'r') as fileIn:
    with open('output2.txt', 'w') as fileOut:
      lines = fileIn.readlines()
      n = int(lines[0])
      List = list(map(int, lines[1].split()))
      fileOut.write(" ".join([str(x) for x in bubbleSort(List, n)]))


"""
Explanation:

The complexity of bubble sort is O(n^2). 
The quadratic complexity is caused by the two nested for loops, which iterate regardless of the input data pattern. 
As a result, the complexity of bubble sort is the same whether the situation is best, worst, or average.
The best-case scenario for bubble sort occurs when the array is already sorted in the required order. 
To handle this case, I took a flag variable which is initially False. 
Whenever a swap occurs it becomes True. 
If no swapping occurs in the first run, the array is already sorted and we can break the loop. 
Henceforth, the best-case bubble sort running time would be linear θ(n).

"""