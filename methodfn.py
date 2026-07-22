x=[1,2,3]
print(x)
x.extend([4,5,6])
print(x)

y=[10,20,30]
y.insert(1,15)
print(y)

z=[100,200,300]
z.remove(200)
print(z)

z.pop(0)
print(z)

z.clear()
print(z)

print(x.count(2))
print(x.index(3))
print(len(x))
y=x.copy()
print(y)
print(max(x))
print(min(x))
print(sorted(x))
print(sorted(x,reverse=True))