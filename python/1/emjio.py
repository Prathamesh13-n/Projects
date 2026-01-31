import demoji

# this modules does not read a emjio only read a emjio 

a = "Prathamesh Nehete 😍 "
a1 = demoji.replace(a , " ")
# print(a1)

# here only read the emjio 
a2 = demoji.findall(a)
# print(a2)

# here read the sentences as well as a emjio
a3 = demoji.replace_with_desc(a)
print(a3)