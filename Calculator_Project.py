def great_num(a,b):
    if(a>b):
        return a,b
    else:
        return b,a
    
def sum():
    n=int(input("Enter the number of terms:"))
    s=0
    for i in range(1,n+1):
        i=int(input())
        s+=i
    return s
def multi():
    n=int(input("Enter the number of terms:"))
    multi=1
    for i in range(1,n+1):
        i=int(input())
        multi*=i
    return multi
print("AC   <-  +/-    /")     
print("7    8   9   x\n4    5   6   -\n1    2   3   +\n%    0   .   =")
y=input("Press Y or y to open the calculator: ")
if(y=='Y' or y=='y'):
    op=input("Press the key operation on keyboard:")
    if(op=='+'):
        s=sum()
        equalto=input("Press = ")
        if(equalto=='='):
            print("\nSum= ",s)
    elif(op=='-'):
        n1=input()
        n2=input()
        newn1,newn2=great_num(n1,n2)
        equalto=input("Press = ")
        if(equalto=='='):
            print("\nDifference:",(int(newn1)-int(newn2)))
    elif(op=='x'):
        m=multi()
        equalto=input("Press = ")
        if(equalto=='='):
            print("\nProduct= ",m)
    elif(op=='/'):
        try:
            n1=int(input())
            n2=int(input())
            equalto=input("Press = ")
            if(equalto=='='):
                print("Quotient= ",n1/n2,"\nRemainder= ",n1%n2)
        except ZeroDivisionError:
            print("Doesn't Divide by Zero!!")

                