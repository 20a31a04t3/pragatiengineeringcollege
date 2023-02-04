n=int(input("enter size:"))
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(0,len(b)):
    if b[i]%2==0:
        c.append(b[i])
    else:
        d.append(b[i])
print(c)
print(d)

