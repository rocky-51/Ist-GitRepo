questions=['1) What is the maximum possible length of an identifier?\na) 16\nb) 32\nc) 64\nd) None of these above',
'2) Who developed the Python language?\na) Zim Den\nb) Guido van Rossum\nc) Niene Stom\nd) Wick van Rossum',
'3) In which year was the Python language developed?\na) 1995\nb) 1972\nc) 1981\nd) 1989',
'4) In which language is Python written?\na) English\nb) PHP\nc) C\nd) All of the above',
'5) Which one of the following is the correct extension of the Python file?\na) .py\nb) .python\nc) .p\nd) None of these',
'6) In which year was the Python 3.0 version developed?\na) 2008\nb) 2000\nc) 2010\nd) 2005',
'7) What do we use to define a block of code in Python language?\na) Key\nb) Brackets\nc) Indentation\nd) None of these',
'8) Which character is used in Python to make a single line comment?\na) /\nb) //\nc) #\nd) !',
'9) Which of the following statements is correct regarding the object-oriented programming concept in Python?\na) Classes are real-world entities while objects are not real\nb) Objects are real-world entities while classes are not real\nc) Both objects and classes are real-world entities\nd) All of the above',
'10) Which of the following statements is correct in this python code?\n1. class Name: 2. def __init__(javatpoint): 3. javajavatpoint = java 4. name1=Name("ABC") 5. name2=name1 \na) It will throw the error as multiple references to the same object is not possible\nb) id(name1) and id(name2) will have same value\nc) Both name1 and name2 will have reference to two different objects of class Name\nd) All of the above',
'11) What is the method inside the class in python language?\na) Object\nb) Function\nc) Attribute\nd) Argument',
'12) Which of the following declarations is incorrect?\na) _x = 2\nb) __x = 3\nc) __xyz__ = 5\nd) None of these',
'13) Why does the name of local variables start with an underscore discouraged?\na) To identify the variable\nb) It confuses the interpreter\nc) It indicates a private variable of a class\nd) None of these',
'14) Which of the following is not a keyword in Python language?\na) val\nb) raise\nc) try\nd) with',
'15) Which of the following statements is correct for variable names in Python language?\na) All variable names must begin with an underscore.\nb) Unlimited length\nc) The variable name length is a maximum of 2.\nd) All of the above',
'16) Which of the following declarations is incorrect in python language?\na) xyzp = 5,000,000\nb) x y z p = 5000 6000 7000 8000\nc) x,y,z,p = 5000, 6000, 7000, 8000\nd) x_y_z_p = 5,000,000']
answers=['d','b','d','c','a','a','c','c','b','b','b','d','c','a','b','b']
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
money=0
print("\t\t\t\tDHANVRIKSHA")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t70000000\t\t\t\t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t10000000\t\t\t\t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t5000000\t\t\t\t    \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t2500000\t\t\t\t    \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t1250000\t\t\t\t    \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t640000\t\t\t\t     \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t320000\t\t\t\t     \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t160000\t\t\t\t     \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t80000\t\t\t\t      \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t40000\t\t\t\t      \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t20000\t\t\t\t      \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t10000\t\t\t\t      \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t5000\t\t\t\t       \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t3000\t\t\t\t       \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t2000\t\t\t\t       \t    |")
print("----------------------------------------------------------------------------")
print("|\t\t\t\t1000\t\t\t\t       \t    |")
print("----------------------------------------------------------------------------\n")
for ques in range(0,16):
    print(questions[ques])
    reply=input("Enter Your Answer: ")
    print("\n")
    if(reply==answers[ques]):
        money=levels[ques]
        print("You Won {} rupees\n".format(money))
    elif(reply=='quit'):
        print("Congrats You Received {}\n".format(money))
        break
    elif(reply=='q'):
        print("Congrats You Received {}\n".format(money))
        break
    else:
        if(ques>=4 and ques<9):
            money=10000
        elif(ques>=9):
            money=320000
        else:
            money=0
        break
print("YOU RECEIVE {} RUPEES IN YOUR ACCOUNT!!".format(money))


