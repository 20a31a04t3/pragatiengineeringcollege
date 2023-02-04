x=int(input("enter the number:"))
a=[]
b=[]
c=[]
for i in range(1,x+1):
    a.append(i)
print(a)
for i in range(1,x+1):
  b.append(a.pop())
for i in range(1,x+1):
  c.append(b.pop())
print(a)
print(b)
print(c)


def hand1(n,a,b,c):
    if n==0:
        hand(n-1,a,c,b):
            if a:
                c.append(a.pop())
            hand1(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle:")


