#Task 4

def bubbleSort(schedule):
  for i in range(len(schedule)-1):
    flag = False
    for j in range(len(schedule)-1-i):
      if schedule[j][0] > schedule[j+1][0] or (schedule[j][0] == schedule[j+1][0] and schedule[j][1][1] < schedule[j+1][1][1]):
        flag = True
        schedule[j], schedule[j+1] = schedule[j+1], schedule[j]
    if flag == False:
      break

def jumanjiRailway(lines):
  schedule = list()
  for line in lines[1:]:
    part = line.strip().split(' will departure for ')
    name = part[0]
    time = part[1].split(' at ')
    schedule.append((name, time))
    bubbleSort(schedule)
  return [f'{line[0]} will departure for {line[1][0]} at {line[1][1]}\n' for line in schedule]


if __name__ == '__main__':
  with open("input4.txt", "r") as fileIn:
    with open("output4.txt", "w") as fileOut:
      lines = fileIn.readlines()
      fileOut.write(''.join([str(x) for x in jumanjiRailway(lines)]))