#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK_01


def isPalindrome(x):
    
    if x[1]=='': 
        return False 
    n=len(x[1])
    for i in range(n//2):
        if x[1][i] != x[1][n-1-i]:
            return False
    return True        


file=open('input.txt')
lst=file.readlines()
file2=open('output.txt', 'w')
file3=open('records.txt', 'w')
even_count=0
odd_count=0
none_count=0
pal_count=0
not_pal=0

for pair in lst:
    x=pair.strip().split(' ')
    #print(x)
    if '.' in x[0]:
        par=None
        none_count+=1
    elif int(x[0])%2==0:
        par='even'
        even_count+=1
    elif int(x[0])%2!=0:
        par='odd'
        odd_count+=1

    temp=isPalindrome(x) #calling the function
    
    if temp==True:
        pal='is'
        pal_count+=1
    else: pal= 'is not'
        
    if par==None:
            file2.write(f'{x[0]} cannot have parity and {x[1]} {pal} a palindrome\n')
    else: file2.write(f'{x[0]} has {par} parity and {x[1]} {pal} a palindrome\n')
        
T=len(lst)
file3.write(f'Percentage of odd parity: {int(odd_count/T*100)}%\n') 
file3.write(f'Percentage of even parity: {int(even_count/T*100)}%\n') 
file3.write(f'Percentage of no parity: {int(none_count/T*100)}%\n') 
file3.write(f'Percentage of palindrome: {int(pal_count/T*100)}%\n')
file3.write(f'Percentage of non-palindrome: {int((T-pal_count)/T*100)}%')

file2.close()
file3.close()

file=open('input.txt')
file2=open('output.txt')
file3=open('records.txt')        
print(file.read())
print(file2.read()) 
print(file3.read())

file.close()
file2.close()
file3.close()

