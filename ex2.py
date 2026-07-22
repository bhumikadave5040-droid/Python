student=[1,"ram",35.2,2,"shyam",45.5,3,"hari",67.8]

for i in range(len(student)):
    if i%3==0:
        print(student[i])

for i in range(len(student)):
    if i%3==0:
        print(student[i+1])

for i in range(len(student)):
    if i%3==0:
        print(student[i+2])

for i in range(len(student)):
    if i%3==0:
        print(student[i],student[i+1],student[i+2])
        print("-----------------")