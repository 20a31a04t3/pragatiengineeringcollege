#EXP 1.1
a,b,c=10,20,30
print(a,b,c)
print(a,b,c,sep='')
print(a,b,c,sep='%')
print(a,b,c,sep='*')
print(a,end='')
print(b,end='*')
print(c,end='-')
print('A','B','C',sep='')
print(1,2,3)
#print(1,2,3,sep+'*')

#EXP 1.2
x,y,z=input("enter the three values").split()
print("total no of students:",x)
print("total no of boys:",y)
print("total no of girls:",z)

#EXP 1.3
x,y,z=input("enter the three values").split('0')
print("total no of students:",x)
print("total no of boys:",y)
print("total no of girls:",z)

#EXP 1.4
a=5
b=5.0
if a==b:
    print("yes")
else :
    print ("No")

#EXP 1.5
a=5
b=True
if 1==b:
    print("yes")
else :
    print ("No")

#EXP 1.6
a=int(input("enter number:"))
if a%7==0:
    print("yes")
else:
    print("No")
email="balaji@gmail.com"
pwd=123456
otp=5678
cemail=input("enter the mail")
cpwd=int(input("enter pwd:"))

#EXP 1.7
if(cemail==email and cpwd==pwd):
    print("log in successfully")
    cotp=int(input("enter otp:"))
    if(cotp==otp):
        print("order placed successfully")
    else :
        print("order failed due to incorect otp")
elif(cemail==email and cpwd!=pwd):
    print("login failed due to wrong pwd")
elif(cemail!=email and cpwd==pwd):
    print("login failed due to wrong email")
elif(cemail!=email and cpwd!=pwd):
    print("login failed due to wrong mail and pwd")

#EXP 1.8

for i in range (200,1,-1) :
    
    print(i)

#EXP 1.9
    
for i in range (97,123) :
    
    print(chr(i),end=' ')

#EXP 1.10
    for i in range(90,65,-2):
    if i!=65:
        if i!=69:
            if i!=73:
                if i!=79:
                    if i!=85:
                        print(chr(i),end='')
       
   
    



