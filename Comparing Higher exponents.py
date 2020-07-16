import math
base1,power1=map(int,input().split())
base2,power2=map(int,input().split())

def log(base,power):
    return power*math.log(base)

if log(base1,power1)>log(base2,power2):
    print("{},{} is greater".format(base1,power1))
elif log(base1,power1)<log(base2,power2):
    print("{} , {} is lower than {} , {}".format(base1,power1,base2,power2))
else:
    print("Equal")
