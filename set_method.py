#creating an empty set

a =set()
#print(type(a))

#adding values to an empty set
a.add(4)
a.add(5)
a.add(4)
# a.add([5,35,6]) #cannot use list to set
# a.add((5.35,6)) #tuple
# a.add({5:7})  #cannot use dictionary to set

print(a)

print(len(a))
a.remove(5)
print(a)

#clear()
a.clear()
print(a)

#pop() the pop() method remove a random item from a set

b = {"vikas" , "taj" , "mohit"}
b.pop()
print(b)