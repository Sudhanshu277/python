# i = 1
# while i<5:
#     j=1
#     while j<5:
#         print(j)
#         j = j+1
#     i = i+1

# print * in style 

# i = 1
# while i<=5:
#     j=1
#     while j<=i:
#         # print("*",end="")
#         print(i,end="")
#         # print(j,end="")
#         j = j+1
#     print() #new line
#     i = i+1

# reverse style of *

# i = 1
# while i<=5:
#     b=1
#     while b<= 5-i:
#         print(" ",end='')
#         b = b+1
#     j = 1
#     while j<=i:
#         print("*",end='')
#         #print(i,end='')
#         #print(j,end='')
#         j = j+1
#     print()
#     i = i+1

# i = 1
# k=1
# while i<=5:
#     b =1
#     while b<=5-i:
#         print(" " ,end='')
#         b = b+1
#     j=1
#     while j<=k:
        # print("*",end='')
        # print(k,end='')
        # print(j,end='')
        # print(i,end='')
    #     j = j +1
    # k =k+2
    # print()
    # i = i+1

n = 5
i = 1
while (n>0):
    b =1
    while (b<i):
        print(" ", end="")
        b = b+1
    j = 1
    while (j<=(n*2)-1):
        print("*", end="")
        j = j+1
    print()
    n = n-1
    i = i+1

