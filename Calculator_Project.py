from math import * 

#   func for getting greater number
def great_num(a,b):
    if(a>b):
        return a,b
    else:
        return b,a

#   function for Result
def equalto(a):
    equalto=input("Press = ")
    if(equalto=='='):
        print("\nResult= ",a)

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

history={'Addition':[],'Subtraction':[],'Multiplication':[],'Division':[],'Standard Calc':[]}
feedback=[]
#   function for division
def div():
    try:        #try block for handling ZeroDivisionError
        n1=int(input())
        n2=int(input())
        equalto=input("Press = ")
        if(equalto=='='):
            print("Quotient= ",n1/n2,"\nRemainder= ",n1%n2)
        history['Division'].append(n1/n2)
    except ZeroDivisionError:
        print("Doesn't Divide by Zero!!")

#   function for factorial
def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f

y=input("Press Y or y to open the calculator: ")
if(y=='Y' or y=='y'):
    i=1
    while(i>0):
        #   output display
        print("\nCALCULATOR")
        print("-------------------")
        print("h")
        print("AC   std  calc    /")     
        print("7    8   9      x\n4    5   6      -\n1    2   3      +\n%    0   .      =")
        print("-------------------")
        op=input("\nPress the key for the operation on keyboard:")

        if(op=='+'):    #conditon for adding
            s=sum()
            history['Addition'].append(s)
            equalto(s)

        elif(op=='-'):  #condition for subtracting
            d=diff()
            equalto(d)
            history['Subtraction'].append(d)
  
        elif(op=='x'):  #condition for multiplication
            m=multi()
            equalto(m)
            history['Multiplication'].append(s)
        
        elif(op=='/'):  #condition for division
            div()

        elif(op=='%'):
            x=input()
            per=x/100
            
        elif(op=='std calc'):
            print("-----------------------------------")
            print("1/x    x^2        x^3        y^x")     
            print("x!     x^(1/2)    y^(1/x)    lg\nsin    cos        tan        ln")
            print("cosec  sec        cot        e^x\nESC")
            print("-----------------------------------")
            i=5
            while(i>1):
                std_op=input("\nInput the expression for the operation:")

                if(std_op=='1/x'):  #condition for reciprocal
                    try:        #try block for handling ZeroDivisionError
                        x=int(input())
                        equalto(1/x)
                        history['Standard Calc'].append(1/x)
                    except ZeroDivisionError:
                        print("Doesn't Divide by Zero!!")
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
        
                elif(std_op=='x^2'):    #condition for square
                    x=int(input())
                    equalto(pow(x,2))
                    history['Standard Calc'].append(pow(x,2))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='x^3'):    #condition for cube
                    x=int(input())
                    equalto(pow(x,3))
                    history['Standard Calc'].append(pow(x,3))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='y^x'):    #condition for y^x
                    x=int(input("Enter x "))
                    y=int(input("Enter y "))
                    equalto(pow(y,x))
                    history['Standard Calc'].append(pow(y,x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='x!'):    #condition for factorial
                    x=int(input())
                    f=fact(x)
                    equalto(f)
                    history['Standard Calc'].append(f)
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='x^(1/2)'):    #condition for square root
                    x=int(input())
                    equalto(sqrt(x))
                    history['Standard Calc'].append(sqrt(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='y^x'):    #condition for y^x
                    x=int(input("Enter x "))
                    y=int(input("Enter y "))
                    equalto(pow(y,1/x))
                    history['Standard Calc'].append(pow(y,1/x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='lg'):    #condition for logarithimic
                    x=int(input())
                    equalto(log(x))
                    history['Standard Calc'].append(log(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='ln'):    #condition for natural log
                    x=int(input())
                    equalto(log1p(x))
                    history['Standard Calc'].append(log1p(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='sin'):    #condition for sin
                    x=int(input())
                    equalto(sin(x))
                    history['Standard Calc'].append(sin(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='cos'):    #condition for cos
                    x=int(input())
                    equalto(cos(x))
                    history['Standard Calc'].append(cos(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='tan'):    #condition for tan
                    x=int(input())
                    equalto(tan(x))
                    history['Standard Calc'].append(tan(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='cosec'):  #condition for cosec
                    x=int(input())
                    equalto(cosec(x))
                    history['Standard Calc'].append(cosec(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='sec'):    #condition for sec
                    x=int(input())
                    equalto(sec(x))
                    history['Standard Calc'].append(sec(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='cot'):    #condition for cot
                    x=int(input())
                    equalto(cot(x))
                    history['Standard Calc'].append(cot(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
            
                elif(std_op=='e^x'):    #condition for exponential
                    x=int(input())
                    equalto(exp(x))
                    history['Standard Calc'].append(exp(x))
                    esc=input("Enter 'ESC' or 'esc' to escape and 'con' or 'CON' to continue:")
                    if(esc=='esc' or esc=='ESC'):
                        break
                else:
                    print("Input Correct Expression")
                    
        elif(op=='h'):  #condition for history
            print("History:\n")
            for key,value in history.items():
                print(key,'\t',value)

        elif(op=='AC'): #condition for closing the calculator
            fd=input("\nGive Your Feedback:")
            feedback.append(fd)
            print("\nThanks for your feedback")
            for i in feedback:
                print(i)
            break

        else:
            print("Press Correct key!!")

else:
    print("Press Y!!")

            
        
