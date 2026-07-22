def info(name,age,marks):
    return f"name:{name}\nage:{age}\nmarks:{marks}"
name=input("enter your name")
age=int(input("enter your age"))
marks=float(input("enter your marks"))

print(info(name,age,marks))