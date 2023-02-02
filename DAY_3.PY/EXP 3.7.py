num=[12,13,14,15,1,6,2,78]
num1=[]#empty list
print(sorted(num))
print(any(num))#results True because data is present 
print(any(num1))#results False because its empty list
num.append(0) #element is added at last
print(num)
num.insert(3,100) #syntax:-insert(index,value)
print(num)
print(num.index(14))#prints the index position of 14
num.remove(12)#removes the value from lists
print(num)
num.reverse()# reverses the list
print(num)
