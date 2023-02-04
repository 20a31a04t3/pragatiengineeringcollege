a=int(input("enter value:"))
b=input()
c=list(b)
count=0
for i in range(0,a):
    if c[i]=='1':
        count=count+1;
print(count-1)
