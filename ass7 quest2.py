num=int(input("enter number" ))


sum=0
for i in range(2,num):
    if (num%i==0):
        sum+=i
if (sum==num):
    print("%d perfect numbr" %num)
else:
    print("not a perfect no" %num)
    
