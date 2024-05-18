#1(a)
try :
  with open("input1a.txt","r") as inp_file:
    with open("output1a.txt","w") as out_file:
      store=inp_file.readlines()
      for i in store[1:]:
          i=i.strip()
          if int(i)%2==0:
            out_file.write(f"{i} is an Even number.\n")
          else:
            out_file.write(f"{i} is an Odd number.\n")
except Exception:
  pass

#1(b)
try:
  with open("input1b.txt","r") as inp_file:
    with open("output1b.txt","w") as out_file:
      store=inp_file.readlines()
      for i in store[1:]:
        list1=i.split()
        if list1[2]=="+":
          out_file.write(f"The result of {list1[1]} {list1[2]} {list1[3]} is {int(list1[1])+int(list1[3])}\n")
        elif list1[2]=="-":
          out_file.write(f"The result of {list1[1]} {list1[2]} {list1[3]} is {int(list1[1])-int(list1[3])}\n")
        elif list1[2]=="*":
          out_file.write(f"The result of {list1[1]} {list1[2]} {list1[3]} is {int(list1[1])*int(list1[3])}\n")
        elif list1[2]=="/":
          out_file.write(f"The result of {list1[1]} {list1[2]} {list1[3]} is {int(list1[1])/int(list1[3])}\n")
except Exception:
  pass