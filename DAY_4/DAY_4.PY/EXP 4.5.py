import re
str1="she sells sea shell at sea shore"
p1="sea"
rep="ocean"
ns=re.sub(p1,rep,str1,2)
print(ns)
if re.match(p1,str1):
    print("match found")
else:
    print(p1,"not present in string")
    p2="she"
    if re.match(p2,str1):
        print("match found")
    else:
       print("not present in string")
       
if re.search(p1,str1):
    print("match found")
else:
    print(p1,"not present in string")
