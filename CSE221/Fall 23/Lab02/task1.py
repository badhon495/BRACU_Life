#Task 1a (Quadratic)
def findSum(N, S, arr):
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == S:
                return f"{i+1} {j+1}"
    return "IMPOSSIBLE"

#Task 1b (Linear)
def findSumLinearly(N, S, arr):
    hash = dict()
    for i in range(N):
        key = S - arr[i]
        if key in hash:
            return f"{hash[key]} {i+1}"
        hash[key] = i+1
    return "IMPOSSIBLE"


if __name__ == '__main__':
    #Tester code: Task 1a
    with open('input1a.txt', 'r') as filein:
        lines = filein.readlines()
        N, S = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))

    with open('output1a.txt', 'w') as fileout:
        fileout.write(findSum(N, S, arr))

    #Tester code: Task 1b
    with open('input1b.txt', 'r') as filein:
        lines = filein.readlines()
        N, S = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))

    with open('output1b.txt', 'w') as fileout:
        fileout.write(findSumLinearly(N, S, arr))


'''
Explanation:

Task 1a: The code defines a function findSum() that takes the length of the list (N), the target sum (S), and the list of integers (arr) as inputs. 
It iterates through each pair of distinct positions in the list using nested loops. 
If the sum of the numbers at the current pair of positions is equal to the target sum, it returns the positions. 
If no such pair is found, it returns "IMPOSSIBLE." Lastly, with selection sort, the time complexity of this solution is O(N²).

Task 1b: The code keeps track of the numbers it has come across so far using a dictionary (hash). 
It cycles through the list of numbers and computes the complement for each number (S minus the current number). 
The presence of the complement in the dictionary indicates that we have discovered two integers that add up to S. 
The complement's location and the current number are then returned. We return "Impossible" if the loop ends up being intractable. 
Because we only iterate through the list of integers once, the time complexity of this solution is O(N).
'''