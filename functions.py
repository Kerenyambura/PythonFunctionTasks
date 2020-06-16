"""Maths = int(input("Enter Math Marks: "))
English = int(input("Enter English Marks: "))
Kisw = int(input("Enter Kiswahili Marks: "))
Science = int(input("Enter Science Marks: "))
SS = int(input("Enter S/SRE Marks: "))



def findgrade(average):

    if average >= 80 and average <= 100:
        return("Grade is A")
    elif average >= 75 and average <= 79:
        return("Grade is A-")
    elif average >= 65 and average <= 69:
        return("Grade is B+")
    elif average >= 60 and average <= 64:
        return("Grade is B")
    elif average >= 55 and average <= 59:
        return("Grade is B-")
    elif average >= 50 and average <= 54:
        return ("Grade is C+")
    elif average >= 45 and average <= 49:
        return ("Grade is C-")
    elif average >= 40 and average <= 44:
        return ("Grade is D+")
    elif average >= 35 and average <= 39:
        return ("Grade is D")
    elif average >= 30 and average <= 34:
        return ("Grade is D-")
    elif average >= 0 and average <= 29:
        return ("Grade is E")
    else:
        return ("Invalid Grade")
totalMarks = Maths + English + Kisw + Science + SS
average = totalMarks/5

print(findgrade(average))
print(average)
print(totalMarks)"""

def compare_num(a,b,c):

    if a > b and a > c:
        print(a,'is the largest')
    elif b > a and b > c:
        print(b, 'is the largest')
    elif c >a and c>b:
        print(c,"is the largest")


compare_num(1000,5000,0)


