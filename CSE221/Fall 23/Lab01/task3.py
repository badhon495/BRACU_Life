#Task 3

def selectionSort(resultList):
  for i in range(len(resultList)):
    max = i
    for j in range(i+1, len(resultList)):
      if resultList[j].split()[3] > resultList[max].split()[3]:
        max = j
      elif resultList[j].split()[3] == resultList[max].split()[3]:
        if resultList[j].split()[1] < resultList[max].split()[1]:
          max = j
    resultList[i], resultList[max] = resultList[max], resultList[i]

def rankStudents(id, marks):
  resultList = [f"ID: {id[i]} Mark: {marks[i]}" for i in range(len(id))]
  selectionSort(resultList)
  return resultList


if __name__ == '__main__':
  with open("input3.txt", "r") as fileIn:
    with open("output3.txt", "w") as fileOut:
      n = fileIn.readline()
      id = [int(i) for i in fileIn.readline().split()]
      marks = [int(i) for i in fileIn.readline().split()]
      fileOut.write("\n".join([str(x) for x in rankStudents(id, marks)]))