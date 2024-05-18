try :
    with open("input4.txt", "r") as inp_file:
        with open("output4.txt", "w") as out_file:
            lines = inp_file.readlines()
            schedules = []
            for line in lines[1:]:
                parts = line.strip().split(' will departure for ')
                name = parts[0]
                place_departure_time = parts[1].split(' at ')
                schedules.append((name, place_departure_time))
            for i in range(len(schedules)-1):
                for j in range(len(schedules)-1-i):
                    if schedules[j][0]>schedules[j + 1][0] or (schedules[j][0]==schedules[j + 1][0] and schedules[j][1][1]<schedules[j + 1][1][1]):
                        schedules[j],schedules[j + 1]=schedules[j + 1],schedules[j]                   

            for line in schedules:
                out_file.write(f'{line[0]} will departure for {line[1][0]} at {line[1][1]}\n')
except Exception:
  pass