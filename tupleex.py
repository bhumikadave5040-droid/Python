x=(90,"hi",("red",[10,20],[100,200]))
for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==list:
                for k in j:
                    print(k)
                continue
            print(j)
        continue
    print(i)