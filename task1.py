student={"Angela": 100,"Ben":95,"Catherin":93,"Danny":97}
a=input("Enter  the Student's name: ")
if a in student:
    print("{}'s marks {}".format(a,student[a]))

else:
       print("Student  not found ")

