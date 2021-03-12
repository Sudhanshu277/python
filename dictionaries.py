# dictionaries are used to store data values in key: value pairs.
# dictionaries is a collection of key value pairs

a={
    "name": "pninfosys",
    "college": "RJIT",
    # "college": "itm" , #duplicates not allowed

    "mark" : [1,2,3,1,(1,3,4,6)],  #tuple ko count ni karega
    "education": {'ram': 'MCA'},
    
}

# print(a)
# print(a['mark'].count(3))
# print(type(a['college']))
# print(a['education']['ram'])

#change dictionary items
# print(a['mark'])
# a['mark']=[40,50,60]
# print(a['mark'])
# print(type(a["mark"]))


#change tuple in dictionary 
# print(type(a[4]))
a[4] = (40,50,30,35,42)
print(type(a[4]))