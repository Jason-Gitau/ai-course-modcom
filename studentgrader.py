# we are trying to summarize student grades

# set up variables that ask for the stdent's name and their three grades

try:
    # name
   name=input("kindly enter your name> ")
 
    #  exams
   exam_1=int(input("kindly enter your exam 1 score> "))
   exam_2=int(input("kindly enter your exam 2 score> "))
   exam_3=int(input("kindly enter your exam 3 score> "))


   # get the average of the three exams
   average=(exam_1+exam_2+exam_3)//3

   # grade the marks
   
   if average>=90:
    grade="A"
   elif average>=80 and average<90:
    grade="B"
   elif average>=70 and average<80:
    grade="C"
   elif average>=60 and average<70:
    grade="D"
   else:
    grade="F"

    

    # store the student data in a dictionary
   student={"Name":name,"Average":average,"grade":grade}
   print(student)


   print(f"{name} \nHad an average score of {average} \nWhich is a {grade}")
except:
    print("KINDLY ENTER VALID CREDENTIALS")

