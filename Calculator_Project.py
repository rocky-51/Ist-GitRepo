#   func for getting greater number
def great_num(a,b):
    if(a>b):
        return a,b
    else:
        return b,a

#   function for addition    
def sum():
    n=int(input("Enter the number of terms:"))
    s=0
    for i in range(1,n+1):
        i=int(input())
        s+=i
    return s

#   function for subtraction
def diff():
    n1=input()
    n2=input()
    newn1,newn2=great_num(n1,n2)
    return int(newn1)-int(newn2)
    
#   function for multiplication
def multi():
    n=int(input("Enter the number of terms:"))
    multi=1
    for i in range(1,n+1):
        i=int(input(),)
        multi*=i
    return multi

#   function for division
def div():
    try:        #try block for handling ZeroDivisionError
        n1=int(input())
        n2=int(input())
        equalto=input("Press = ")
        if(equalto=='='):
            print("Quotient= ",n1/n2,"\nRemainder= ",n1%n2)
    except ZeroDivisionError:
        print("Doesn't Divide by Zero!!")
        
#   output display
print("CALCULATOR")
print("-------------------")
print("h    std calc")
print("AC   <-  +/-    /")     
print("7    8   9      x\n4    5   6      -\n1    2   3      +\n%    0   .      =")
print("-------------------")
y=input("Press Y or y to open the calculator: ")
if(y=='Y' or y=='y'):
    op=input("\nPress the key operation on keyboard:")
    if(op=='+'):    #conditon for adding
        s=sum()
        equalto=input("Press = ")
        if(equalto=='='):
            print("\nSum= ",s)
    elif(op=='-'):  #condition for subtracting
        d=diff()
        equalto=input("Press = ")
        if(equalto=='='):
            print("\nDifference:",d)
    elif(op=='x'):  #condition for multiplication
        m=multi()
        equalto=input("Press = ")
        if(equalto=='='):
            print("\nProduct= ",m)
    elif(op=='/'):  #condition for division
        div()
    elif(op=='AC'):
        pass
    elif(op=='std calc'):
        print("-----------------------------------------------------")
        print("1/x    x^2        x^3        y^x   AC   <-  +/-    /")     
        print("x!     x^(1/2)    y^(1/x)    lg    7    8   9      x\nsin    cos        tan        ln    4    5   6      -")
        print("cosec  sec        cot        e^x   1    2   3      +")
        print("\t\t\t\t   %    0   .      =")
        print("-----------------------------------------------------")
        
                
