
def combine():
    res=0
    res=int(input("enter 1st first"))
    while(True):
        op=input("enter op(+,-,*,%,=)")
        if op=="=":
          print("final op",res)
          break
        num2=int(input("enter your num2"))
        if op=="+":
            res+=num2
        elif op=="-":
            res-=num2
        elif op=="*":
            res*=num2
        elif op=="/":
            res/=num2
        else:
            print("invalid op")
            break
            

while(True):
    print("1ADD\n2.Combine\n3.Exit")
    choice=int(input("enter your choice"))
    match choice:
        case 1:
            pass
        case 2:
            combine()
        case 3:
            print("exit")
            break
        case _:
            print("invalid")