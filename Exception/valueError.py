print("start")
try:
    ip=int(input("enter the no"))
    print(ip)
except ValueError as e:
    print(e)
print("program end")