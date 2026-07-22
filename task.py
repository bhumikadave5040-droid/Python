#wap to print sum of nos. from 23 to 58
sum=0
for i in range(23,59):
    sum=sum+i
print(sum)

#wap to print table of no by using 
n=int(input("enter the no:"))
for i in range(1,11):
    result=n*i
    print(n ,"*" ,i ,"=" ,result)

#even no from 501 to 103 in reverse order       
for i in range(501,102,-1):
    if i%2==0:
        print(i, end=" ")

#give me 5 factors
n=5
for i in range(1,6):

    if n%i==0:
        print(i, end=" ")

# give 7 factorial
n=7
fact=1
for i in range(1,8):
    fact=fact*i
print(fact)
