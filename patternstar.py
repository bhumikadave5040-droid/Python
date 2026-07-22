n=int(input("enter the no"))
i=1
while i<=n:
    j=1
    while j<=n:
        print("*",end=" ")
        j+=1
    print()
    i+=1
print()
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
        

