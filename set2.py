set1={12,35,8,25,5}
set2={25,6,35,15,8}

all=(set1|set2)

sum=0
for i in all:
    if i%5==0:
      print(i,end=" ")
    if i%2==0:
       sum+=i
print()
print(sum)

common=set1&set2
print(common)

sum=0
for i in common:
   sum+=i
print(sum,sum**2,(sum**2)**3)

non_repeated_element=set1^set2
print(non_repeated_element)
mul=1
for i in non_repeated_element:
   mul*=i
print(mul)


    
