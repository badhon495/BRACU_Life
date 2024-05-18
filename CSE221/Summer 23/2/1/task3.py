try :
    with open("input3.txt", "r") as inp_file:
        with open("output3.txt", "w") as out_file:
            store = inp_file.readline()
            id = [int(i) for i in inp_file.readline().split()]
            mark = [int(i) for i in inp_file.readline().split()]
            result = []
            for i in range(len(id)):
                result += [f"ID: {id[i]} Mark: {mark[i]}"]
            for j in range(len(result)):
                max = j
                for k in range(j+1, len(result)):
                    if result[k].split()[3] > result[max].split()[3]:
                        max = k
                    elif result[k].split()[3] == result[max].split()[3]:
                        if result[k].split()[1] < result[max].split()[1]:
                            max = k
                result[j], result[max] = result[max], result[j]
            for line in result:
                out_file.write(f"{line}\n")
except Exception:
  pass