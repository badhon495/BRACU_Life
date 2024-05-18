try :
    def quicksort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quicksort(A, p, q - 1)
            quicksort(A, q + 1, r)


    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1


    with open("input3.txt", "r") as inp_file:
        with open("output3.txt", "w") as out_file:
            store= inp_file.readlines()
            a = store[0]
            b = store[1]
            a = int(a.strip())
            b = b.split()
            for i in range(len(b)):
                b[i] = int(b[i].strip())

            quicksort(b, 0, a - 1)
            for i in b:
                out_file.write(f"{i} ")






except Exception:
  pass