# a = input("enter string")
# b = input(" enter 2nd string")

# if (len(a)!=len(b)):
#     b = b.replace("b",a);
#     print(a);
#     print(b);
# else:
#     print(a);
#     print(b);    
# letter = ''' dear <|NAME|>,
# You are selected !
# Have a great day ahead!
# thanks and regards,
# pninfosys
# DATE : <|DATE|>
# '''
# name = input("enter your name\n")
# date = input("enter date\n")
#letter = letter.replace("<|NAME|>" , name)
# letter = letter.replace("<|DATE|>" , date)

# print(letter)
number = (input("certificate no.\n"))
name = input("enter your name\n")
course = input("enter your couse\n")
date = (input("enter date\n"))
gender = input("enter gender\n")

c = ''' certification no . <|number|>   PNINFOSYS
                                     
                                     CERTIFICATE
                                    OF INTERNSHIP
                                 proudly presented to
                                       <|name|>
          has successfully completed <|course|> internship with PNINFOSYS
          during the period from <|date|> 
          we found him sincere, hardworking, dedicated and result oriented.

              <|gender|> worked well as part of the team during his tenurse.
        we take this opportunity to thank him and wish him all the best for future.'''


c = c.replace("<|number|>" , number)
c = c.replace("<|name|>" , name)
c = c.replace("<|course|>"  , course)
c =  c.replace("<|date|>" , date)
c = c.replace("<|gender|>" , gender)
print(c)