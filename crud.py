student=[[101,"bhumika",99.5],[102,"sneha",98.5],[103,"priya",97.5]]

while True:
    print("student management system\n1. add student\n2. display student\n3.update student\n4. delete student\n5.Topper student\n6. exit")

    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            ip=int(input("how many students you want to add:"))
            for i in range(ip):
                id=int(input("Enter the ID of the student:"))
                name=input("Enter the name of the student:")
                marks=float(input("Enter the marks of the student:"))
                student.append([id,name,marks])
        case 2:
            for i in student:
                print(f"{i[0]}-->{i[1]}-->{i[2]}")
        case 3:
            id=int(input("Enter the ID of the student you want to update:"))
            for i in student:
                if i[0]==id:
                    name=input("Enter the new name of the student:")
                    marks=float(input("Enter the new marks of the student:"))
                    i[1]=name
                    i[2]=marks
                    print("student updated successfully")
                    break
            else:
                print("student not found")
            
        case 4:
            id=int(input("Enter the ID of the student you want to delete:"))
            for i in student:
                if i[0]==id:
                    student.remove(i)
                    print("student deleted successfully")
                    break
            else:
                print("student not found")
            
        case 5:
            max=0
            for i in student:
                if i[2]>max:
                    max=i[2]
                    name=i[1]
            print(f"Topper {name} has marks: {max}")
        case 6:
            print("THAnk you")
            break
        case _: 
            print("invalid choice") 
            