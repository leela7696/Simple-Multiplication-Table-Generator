#This title reflects the functionality of the code, which generates a multiplication table for a given number 

import time
T=eval(input("Enter the Number: "))
for x in range (1,11):
    print(T,"X",x,"=",T*x)
print()
time.sleep(2)
print('End of an application')