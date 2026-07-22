py={"ram","sita","komal","ramu"}
jv={"ram","pavan","gita"}
fd={"gita","komal","payal","ram"}
#total count of each
all=py|jv|fd
print(len(all))

#name of student who are attending java and python and fd
print(all)

#only java 
print("java students:",jv)

#only python
print("python students:",py)

#name of student who are not attending java and python

print("not attending java and python:",all-(jv|py))

#count of student who attends 3 batch at a time 
#1
print(fd-(jv|py)|py-(jv|fd)|jv-(py|fd))

#2
for stud in all:
    count=0
    if stud in py:
        count+=1
    if stud in jv:
        count+=1
    if stud in fd:
        count+=1
    if count==1:
        print(stud)


