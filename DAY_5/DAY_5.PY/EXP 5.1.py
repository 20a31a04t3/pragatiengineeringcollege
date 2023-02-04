a=int(input("enter size:"))
b=list(map(int,input("enter the number:")))
print(b)
s=0
for i in range(1,len(b)):
    if b[i]==1:
        s+=1
print(s)
