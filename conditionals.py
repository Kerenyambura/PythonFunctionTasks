Maths = int(input("Enter Math Marks: "))
English = int(input("Enter English Marks: "))
Kisw = int(input("Enter Kiswahili Marks: "))
Science = int(input("Enter Science Marks: "))
SS = int(input("Enter S/SRE Marks: "))

totalMarks = Maths + English + Kisw + Science + SS
average = totalMarks/5

if average >= 80 and average <= 100:
    print("Grade is A")
elif average >= 75 and average <= 79:
    print("Grade is A-")
elif average >= 65 and average <= 69:
    print("Grade is B+")
elif average >= 60 and average <= 64:
    print("Grade is B")
elif average >= 55 and average <= 59:
    print("Grade is B-")
elif average >= 50 and average <= 54:
    print("Grade is C+")
elif average >= 45 and average <= 49:
    print("Grade is C-")
elif average >= 40 and average <= 44:
    print("Grade is D+")
elif average >= 35 and average <= 39:
    print("Grade is D")
elif average >= 30 and average <= 34:
    print("Grade is D-")
elif average >= 0 and average <= 29:
    print("Grade is E")
else:
    print("Invalid Grade")

print(totalMarks)
print(average)


