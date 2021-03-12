
# print(type(a))

# print

# keys={"break","case","continue","default","defer","else","for","func","goto","if","map","range","return","struct","type","var"}

# b = input("enter the word")

# if a in keys:
#     print(b+" is a keyword")
# else:
#     print(b+" is not a keyword")


   

# year = int(input("Enter a year: ")) 

# if (year % 4) == 0:
#     print(" is not a leap year") 
# elif (year % 100) == 0:
#     print(" is not a leap year")
# elif (year % 400) == 0:
#     print(" is not a leap year")
# else:
#     print("this is a leap year")

# Python program to check if year is a leap year or not

# year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} is a leap year".format(year))
#        else:
#            print("{0} is not a leap year".format(year))
#    else:
#        print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))


# number series

# num = int(input('enter the number'))
# a=0
# b=0

# for i in range(1,num+1):
#     if(i%2!=0):
#         a=a+7
#     else:
#         b=b+6
# if(num%2!=0):
#     print(' {} term of series is {}'.format(num,a-7))
# else:
#     print('{} term of series is {}'.format(num,b-6))

#2nd method
# c = 0
# d = []
# e = 0
# for i in range(0,16):
#     d.append(c)
#     d.append(e)
#     c = c+7
#     e = e+6
# print(d[14])

#candies
# total_candies =10

# no_of_candies = int(input("no of candies"))
# if no_of_candies in range(1,6):
#     print('no of candies sold:' ,no_of_candies)
#     print('number of candies available:',total_candies-no_of_candies)
# else:
#     print("invalid input")
#     print('no of canides ',total_candies)

#oxygen

# trainee = [[],[],[]]
# for i in range(3):
#     for j in range(3):
#         trainee[i].append(int(input()))
#         if (trainee[i][-1] not in range(1,101)):
#             print("invalid input")
# for i in range(3):
#     trainee[3].append((trainee[2][i]+trainee[1][i]+trainee[0][i])//3)
# maximum = max(trainee[3])
# for i in range(3):
#     if trainee[3][i] <70:
#         print("trainee {0} is unfit".format(i+1))
#     elif trainee[3][i] == maximum:
#         print("trainee number",i+1)

# washing

# n= int(input())
# if n==0:
#     print("Time estimated : 0 minutes")
# elif n in range(1,2001):
#     print("Time estimated : 25 minutes")
# elif n in range(2001,4001):
#     print("time estimated :35 minutes")
# elif n in range(4001,7001):
#     print("time estimated : 45 minutes")
# else:
#     print("invalid")

#decimal number
num = str(input("enter the number"))
print(int(num, 17))