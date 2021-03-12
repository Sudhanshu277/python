# names = ["ram","vikas","rohit"]
# a = input("enter your name")
# if a in names:
#     print("yes your name is ther")
# else:
#     print("no")

marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "A++"
elif marks>=80:
    grade =  "A+"
elif marks>=70:
    grade =  "B+" 
elif marks>=60:
    grade =  "B" 
elif marks>=50:
    grade =  "c"
else:
    grade ="Fail"  

print("Your grads is " +grade)