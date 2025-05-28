import math

def get_grade(average):
    if average>=90:
        return "A"
    elif average>=80 and average<90:
        return "B"
    elif average>=70 and average<80:
        return "C"
    elif average>=60 and average<70:
       return "D"
    else:
       return "F"


students_count=0
while True:
    try:
        students_count=int(input("kindly enter no of students: "))

        if students_count==0:
            print("invalid number")
        else:
            break
    except:
        print("Invalid input")

# get student data

for student in range(students_count):
    # name
   students=[]
   name=input(f"kindly enter your {student+1} name> ")

   scores=[]
   for i in range(3):
        try:
           exam=int(input(f"kindly enter {name}'s exam {i+1} score> "))

           if exam<0 and exam>100:
               print("invalid score")
           else:
               scores.append(exam)
               break
        except:
            print("something went bad")
           
              
       
   average=math.floor(sum(scores)/len(scores))
   grade=get_grade(average)
   print(f"{name} \n has an average of {average}\n which is a {grade}")

   student={
    "name":name,
    "average":average,
    "grade":grade
   }
   students.append(student)

print("-"*40)
print(f"{"student name":<15}{"average":<10}{"grade":<40}")
print("-"*40)

for student in students:
    print(f"{student['name']}{student['average']}{grade['grade']}")
    print("-"*40)
