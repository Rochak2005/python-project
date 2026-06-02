Name = input("Student name : ")
print("Student : ", Name)

m1 = int(input("Enter marks of Maths:  "))
m2 = int(input("Enter marks of Hindi:  "))
m3 = int(input("Enter marks of Punjabi:  "))
m4 = int(input("Enter marks of English:  "))
m5 = int(input("Enter marks of Science:  "))

Totel = m1 + m2 + m3 + m4 + m5
Percentage = (Totel / 500)* 100
print(F"Toele: {Totel}/ 500")
print(F"Percentage : {Percentage}%")
 
if Percentage >= 90:
    grade = 'A'
elif Percentage >= 80:
    grade = 'B'
elif Percentage >= 70:
    grade = 'C' 
elif Percentage >= 60:       
    grade = 'D'
else:
    grade = 'F'
print(F"Grade: {grade}" )

print("=============================")
print("        REPORT CARD        ")
print("=============================")
print(F"Name : {Name}")
print(F"Totel : {Totel}")
print(F"Percentage : {Percentage} ")
print(F"Grade : {grade}")



