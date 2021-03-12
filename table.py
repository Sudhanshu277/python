# a = int(input("enter the number\n"))

# for i in range (1,11):
#     # print(a*i)
#     print(str(a) + "X" + str(i) + "=" +str(i*a))

# a = int(input("ENETR the number"))
# fact = 1
# for i in range (1,a+1):
#     fact = fact * i
# print(f"The factorial of this {a} is {fact}")

# num = int(input("ENTER the number:\n"))
# prime =True
# for i in range (2,num):
#     if(num%2==0):
#         prime=False
#         break
# if(num==0 or num==1):
#     print("this is not a prime")
# elif prime:
#     print("this is prime")
# else:
#     print("this is not prime")




# a = int(input("enter the number"))
# i = 1
# while (i<=a):
#     print(i)
#     i = i+1

#write a program to print from 10 to 1
# i = 10
# while (i>=1):
#     print(i)
#     i =i-1

# write the program to print from n to 1
# n = int(input("ENTER THE NUMBER"))
# while (n>=1):
#     print(n)
#     n = n-1

# n = int(input("enter the number upto you want to add"))
# sum = 0 
# i =1
# while(i<=n):
#     sum = sum+i
#     i = i+1
# print("sum",sum)

# Write a program to print sum of Square/cube from 1 to n 10
# n = int(input("Enter the number"))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+(i*i)
#     #sum = sum+(i*i*i)
#     i = i+1
# print(sum)

# n = int(input("Enter the number"))
# sum = 0
# i = 1
# while(n>=i):
#    sum = sum+(n*n)
#    i = n+1
# print(sum)

#write a program to print  even no. b/w 1 to n 

# n = int(input("enter the number"))
# i = 1
# sum = 0
# while(i<=n):
#     sum = sum + 2
#     print(sum)
#     i = i+2

# Write a program to find sum of digits of a given numbers.
n=int(input("Enter a number:"))
sum=0
while(n>0):
    i=n%10
    sum=sum+i
    n=n//10
print("The total sum of digits is:",sum)

#write a program to find sum of square/cube of digits a given no.


# write a number armstrong 

# num = int(input("Enter a number: "))  
# sum = 0  
# i = num  
  
# while i > 0:  
#    digit = i % 10  
#    sum += digit ** 3  
#    i //= 10  
  
# if num == sum:  
#    print(num,"is an Armstrong number")  
# else:  
#    print(num,"is not an Armstrong number")

#write a program to find product  of digit of input no.

# num = int(input("Enter the number"))
# sum = 1
# while(num>0):
#    i = num%10
#    sum = sum*i
#    num=num//10
# print(sum)
#2nd method
# i =int(input("enter the number"))
# prod=1
# while(i>0):
#    prod=prod*(i%10)
#    i=i//10
# print(prod)

#resverse the input number

# num = int(input("enter the number"))
# sum = 0
# while(num>0):
#    i = num%10
#    sum = (sum*10)+i
#    num = num//10
# print(sum)

#factorial

# i = int(input("enter the number"))
# fac = 1
# while(i>0):
#    fac =fac*i
#    i= i-1
# print(fac)

#fabnocci

# n = int(input("enter the number"))
# x=0
# y=1
# z=0 

# while(z<=n):
#    print(z)
#    x=y
#    y=z
#    z=x+y
