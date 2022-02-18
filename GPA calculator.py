#age = int(input("enter your age:"))
#f age>=18 and age<=40 :
#  print("you can party")
#else :
#    print("you can not party")

result=[]

name = str(input("enter your name: "))
x = float(input("enter your SOCIAL marks: "))
if x>100:
    exit("invalid")
y = float(input("enter your MATHS marks: "))
if y>100:
    exit("invalid")
z = float(input("enter your English marks: "))
if z>100:
    exit("invalid")
a = float(input("enter your SCIENCE marks: "))
if a>100:
    exit("invalid")
b = float(input("enter your COMPUTER marks:"))
if b>100:
    exit("invalid")
marks= x+y+z+a+b
percentage = (marks / 500.0) * 100
print(f"your percentage={percentage}%")
if percentage==0 and percentage<=10:
    print("Your Gpa is E")
elif percentage>=10 and percentage<=20:
    print("Your Gpa is D")
elif percentage>=20 and percentage<+30:
    print("Your Gpa is D+")
elif percentage>=30 and percentage<=40:
    print("Your Gpa is C")
elif percentage>=40 and percentage<=60:
    print("Your Gpa is C+")
elif percentage>=60 and percentage<=70:
    print("Your Gpa is B")
elif percentage>=70 and percentage<=80:
    print("Your Gpa is B+")
elif percentage>=80 and percentage<=90:
    print("Your Gpa is A")
if percentage>=90 and percentage<=100:
    print("Your Gpa is A+")




