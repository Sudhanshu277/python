# a = int(input("ENETR NO 1ST: \n"))
# b = int(input("ENETR NO 2nd: \n"))
# c = int(input("ENETR NO 3rd: \n"))
# d = int(input("ENETR NO 4th: \n"))

# if(a>b and a>c and a>d):
#     print(a)
# elif(b>a and b>c and b>d):
#     print(b)
# elif(c>a and c>b and c>d):
#     print(c)
# elif(d>a and d>c and d>b):
#     print(d)
# else:
#     print("equal")   

a = int(input("ENTER 1ST SUBJECT MARKS"))
b = int(input("ENTER 2ND SUBJECT MARKS"))
c= int(input("ENTER 3RD SUBJECT MARKS"))


if(a<33 or b>33 or c>33):
    print("you are fail")
elif(a+b+c/3 <40):
    print("you are fali due to less percentage")
else:
    print("passed")
