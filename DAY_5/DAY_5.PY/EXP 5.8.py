""" write a program to add 6 user defined numbers and return the value to the main
program 8  6 4 2 10 0 """
"""         def add():
    a=8
    b=6
    c=4
    d=2
    e=10
    f=0
    return(a+b+c+d+e+f)
add()
print(add())       """

x=list(map(int,input().split()))
def add():
    result=0
    for i in range(0,len(x)):
        result=result+x[i]
    print(result)
add()

