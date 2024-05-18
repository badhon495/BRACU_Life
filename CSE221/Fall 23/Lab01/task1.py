#Task 1a

def EvenOdd(lines):
  output = str()
  for i in lines[1:]:
    i = i.strip()
    if int(i)%2 == 0:
      output += (f"{i} is an Even number.\n")
    else:
      output += (f"{i} is an Odd number.\n")
  return output


#Task 1b

def Calculate(lines):
  output = str()
  for i in lines[1:]:
    L = i.split()
    if L[2] == "+":
      output += (f"The result of {L[1]} {L[2]} {L[3]} is {int(L[1]) + int(L[3])}\n")
    elif L[2] == "-":
      output += (f"The result of {L[1]} {L[2]} {L[3]} is {int(L[1]) - int(L[3])}\n")
    elif L[2] == "*":
      output += (f"The result of {L[1]} {L[2]} {L[3]} is {int(L[1]) * int(L[3])}\n")
    elif L[2] == "/":
      output += (f"The result of {L[1]} {L[2]} {L[3]} is {int(L[1]) / int(L[3])}\n")
  return output


if __name__ == '__main__':
  #Tester code: Task 1a
  with open('input1a.txt', 'r') as fileIn:
    with open('output1a.txt', 'w') as fileOut:
      lines = fileIn.readlines()
      fileOut.write("\n".join([x for x in EvenOdd(lines).splitlines()]))


  #Tester code: Task 1b
  with open('input1b.txt', 'r') as fileIn:
    with open('output1b.txt', 'w') as fileOut:
      lines = fileIn.readlines()
      fileOut.write("\n".join([x for x in Calculate(lines).splitlines()]))