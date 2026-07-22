student=[[101,"bhumika",99.5],[102,"sneha",98.5],[103,"priya",97.5]]
print(student)
max=0
for i in student:
    if i[2]>max:
        max=i[2]
print("max topper is:",max)