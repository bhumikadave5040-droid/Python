n=6
sum=0
for i in range(1,5):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number") 
else:    print("not a perfect number")  