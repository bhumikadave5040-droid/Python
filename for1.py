sv=int(input("enter the  sv no:"))
ev=int(input("enter the  ev no:"))

for i in range(sv,ev+1):
    if i%5==0 and i%7==0:
        print(i, end=" ")     
        
           