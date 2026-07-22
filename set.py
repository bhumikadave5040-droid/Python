#loop
x={10,20,30,40,10,40}

print(x)
for item in x:
    print(item)

x.add(90)
print(x)

x.discard(30)
print(x)

a={10,20}
a.update([10,20,30])
print(a)