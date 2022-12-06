import math
print("___________________WELCOME TO OUR SCIENTIFIC CALCULATOR______________________")
print("ENTER")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.MOD")
print("6.SQUARE ROOT")
print("7.POWER")
print("8.SINE")
print("9.COSINE")
print("10.TANGENT")
print("11.DEGREE TO RADIAN")
print("12.RADIAN TO DEGREE")
print("*****************************************************")
z=int(input("ENTER NUMBERS FROM 1 TO 12 TO PERFORM OPERATIONS: "))
y="yes"
pi=22/7
if z==1:
    a=float(input("enter the 1st number:"))
    b=float(input("enter the 2nd number:"))
    result=a+b
if z==2:
    a=float(input("enter the 1st number:"))
    b=float(input("enter the 2nd number:"))
    result=a-b
if z==3:
    a=float(input("enter the 1st number:"))
    b=float(input("enter  2nd number:"))
    result=a*b
if z==4:
    a=float(input("enter the 1st number:"))
    b=float(input("enter the 2nd number:"))
    result=a/b
if z==5:
    a=float(input("enter the 1st number:"))
    b=float(input("enter the 2nd number:"))
    result=a%b
if z==6:
    a=float(input("enter the 1st number:"))
    b=float(input("enter the 2nd number:"))
    result=math.sqrt(a,2)
if z==7:
    a=float(input("enter the 1st number:"))
    b=float(input("enter the 2nd number:"))
    result=math.pow(a,b)
if z==8:
    a=float(input("enter the 1st number:"))
    result=math.sin(a)
if z==9:
    a=float(input("enter the 1st number:"))
    result=math.cos(a)
if z==10:
    a=float(input("enter the 1st number:"))
    result=math.tan(a)
if z==11:
    a=float(input("enter the 1st number:"))
    result=a*(pi/180)
if z==12:
    a=float(input("enter the 1st number:"))
    result=a*(180/pi)
print("result:",result)
y=input("Do you want to operate again \"yes\" or \"no\"? ")
while y=="Yes" or y=="YES" or y=="yes":
    print("ENTER")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.MOD")
    print("6.SQUARE ROOT")
    print("7.POWER")
    print("8.SINE")
    print("9.COSINE")
    print("10.TANGENT")
    print("11.DEGREE TO RADIAN")
    print("12.RADIAN TO DEGREE")
    print(".............................................................")
    z=int(input("ENTER NUMBERS FROM 1 TO 12 TO PERFORM OPERATIONS:"))
    print(".............................................................")
    if z==1:
        a=float(input("enter the number:"))
        result=result+a
    if z==2:
        a=float(input("enter the number:"))
        result=result-a
    if z==3:
        a=float(input("enter the number:"))
        result=result*a
    if z==4:
        a=float(input("enter the number:"))
        result=result/a
    if z==5:
        a=float(input("enter the number:"))
        result=result%a
    if z==6:
        result=math.sqrt(result,2)
    if z==7:
        a=float(input("enter the number:"))
        result=math.pow(result,a)
    if z==8:
        result=math.sin(result)
    if z==9:
        result=math.cos(result)
    if z==10:
        result=math.tan(result)
    if z==11:
        result=result*(pi/180)
    if z==12:
        result=result*(180/pi)
    print("result=",result)
    print("______________________________________________________________________________")
    y=input("Do you want to operate again \"yes\" or \"no\"? ")
    print("______________________________________________________________________________")
print("------------------Thank You for using Our Scientific Calculator-------------------")
