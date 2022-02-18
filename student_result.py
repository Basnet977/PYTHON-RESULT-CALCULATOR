num = int(input("Enter number of students : "))

increment = 1

student_marks = []

while increment<= num:
    print(f"======First Student: {increment}======")
    for x in range(1):
        phi = int(input("Enter PHILOSOPHY marks :"))
        eng = int(input("Enter ENGLISH marks: "))
        sci = int(input("Enter SCIENCE marks : "))
        math = int(input("Enter MATHS marks : "))
        comp = int(input("Enter COMPUTER marks : "))
        soc = int(input("Enter SOCIAL marks : "))
        student_mark= [phi,eng,sci,math,comp,soc]
        student_marks.append(student_mark)
    increment+=1

total_marks = []

for smark in student_marks:
    tot_marks=0
    for mark in smark:
        tot_marks += mark

    total_marks.append(tot_marks)

x = 1
for total in total_marks:
    percentage = total/5
    division = ''

    if percentage>35 and percentage<45:
        division += "third"
    elif percentage>45 and percentage<60 :
        division+= "second"
    elif percentage>60 and percentage<75:
        division+="first"
    elif percentage>75 and percentage<100:
        division+= "top"
    else :
        division+="sorry"

    print(f"===========Student result : {x} ============")
    print(f"""total : {total} 
    percentage : {percentage}
    division :  {division}""")