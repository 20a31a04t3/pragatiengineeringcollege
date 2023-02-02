#write a python program to find absolute value for the difference in between even
#and odd digits of a given number
#Test case 1:-   1 2 2 3
#Test case 2:-  4 5 6 7
#Test case 3:-  1 2 3 4 5 6 7 8 9

n=int(input("enter the number:"))
even=0
odd=0
diiference=0
while n!=0:
    r=n%10
    if r%2==0:
        even=even+r
    else:
        odd=odd+r
    n=n//10
print(even)
print(odd)
print(abs(even-odd))
