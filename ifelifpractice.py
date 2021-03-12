a = input("Enter you location:\n")
b = int(input("Enter you distance(km) from your college:\n"))

if(b<10 and a=="gwalior"):
    print("you can submit your sheet in your college")

elif(b>10 and a=="gwalior"):
    print("your nearest college are : \n 1.mulsimbord 2. agra college")
elif(b>=20 and b<=20 and a=="gwalior"):
    print("your nearset college are:\n 1.rjit 2.mits")
else:
    print("submit online")



