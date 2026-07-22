x=[[1,2,3],[4,5,6],"hello",[7,8,9],"hi",]
print(x)
for i in x:
    if type(i)==list:
     for j in i:
        print(j)
     continue
    print(i)