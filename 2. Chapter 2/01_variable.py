num1=int(input("please enter mark1:"))
num2=int(input("please enter mark2:"))
num3=int(input("please enter mark3:"))
num4=int(input("please enter mark4:"))
num5=int(input("please enter mark5:"))

total_marks=num1+num2+num3+num4+num5
average_mark=total_marks/5

print("total marks are :",total_marks)
print("average marks are :",average_mark)

if average_mark >= 90:
     print("excelent")

elif average_mark>=60 and average_mark<=89:
    print("first")

elif average_mark>=40 and average_mark<=59 :
    print("second")
else:
    print("failed")

