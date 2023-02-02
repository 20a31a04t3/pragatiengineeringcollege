n=int(input("enter the number:"))
a=n
d=n
sum=0
count=0
while n!=0:
    r=n%10
    n=n//10
    count=count+1
print(count)   
for i in range(1,count+1):
    while a!=0:   
        r=a%10
        a=a//10
        sum=sum+pow(r,count)
print(sum)
if d==sum:
    print("ARMSTRONG NUMBER")
else:
    print("NOT A ARMSTRONG NUMBER")
