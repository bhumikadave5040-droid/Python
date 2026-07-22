


def prime_num():
    n=int(input("enter the no:"))
    
    if n<=1:
        print("not prime")
        return
    i=2
    while i<n:
        if n%i==0:
            print("not prime")
            return
        i+=1
    print("prime number")
def tables():
    no=int(input("enter the no."))
    i=1
    while i<=10:
        result=no*i
        print(result)
        i+=1
def no_print():
    i=1
    while i<=10:
        print(i)
    i+=1
def fibonacci():
    num=int(input("enter the no:"))
    a=0
    b=1
    i=1 #1 #2
    while i<=num:  #1<=5 #2<=5 #3<=5 #4<=5 #5<=5 #6<=5
        print(a) #0 #1 #1 #2 #3
        temp= a+b  #1 #2 #3 #5 #8
        a=b #1 #2 #3 #5
        b=temp #1 #2 #3 #5 #8
        i+=1 #2 #3 #4 #5 #6

def palimdrome():
    no=int(input("enter the no:"))
   

    

    print("\n1.prime number")
    print("\n2.Tables")
    print("\n3.Number print 1 to 10")
    print("\n4.fibonacci")
    print("\n5.Palindrome")
    print("\n6.Exit")



choice=int(input("enter your choice"))
match choice:
    case 1: prime_num()
    case 2: tables()
    case 3:no_print()
    case 4: fibonacci()
    case 5: palimdrome()
    case 6: 
        print("exit")
        
    case _: print("invalid choice")     


    

