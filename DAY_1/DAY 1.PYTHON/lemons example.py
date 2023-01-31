a=int(input("enter no of lemons:"))
b=int(input("enter no of lemons needed:"))

if a-b<0 :
    print("invalid and u have",b-a,"less")
elif a-b>0:
    print("u have",a-b,"more ")
else :
    print("sufficient")

