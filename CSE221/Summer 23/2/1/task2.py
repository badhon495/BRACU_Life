try:
    with open("input2.txt","r") as inp_file:
      with open("output2.txt","w") as out_file:
        store=inp_file.readline()
        n = int(store)
        swapped = True
        list1=list(map(int,inp_file.readline().split()))
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if list1[j] > list1[j+1]:
                    list1[j], list1[j+1] = list1[j+1], list1[j]
                    swapped = True
                if swapped == False:
                  break
        out_file.write(' '.join(map(str, list1)))
except Exception:
    pass

"""
Explanation:

The best-case scenario for bubble sort occurs when the input array is already sorted in the required order. To handle this case, 
we introduce a flag variable swapped that keeps track of whether any swap was made in the current iteration. If no swaps were made in the current iteration, 
it means that the array is already sorted, and we can break out of the loop. If a swap was made in the current iteration, it means that the array is still not sorted, 
and we need to continue with the next iteration. By doing this, we avoid checking the elements that are already in their correct positions, 
reducing the number of operations performed. The worst-case scenario still remains the same with a time complexity of θ(n2). 
But this optimization leads to a time complexity of θ(n) for the best-case scenario. 
"""