str1=(input("enter string1:"))
str2=(input("enter string2:"))
if (len(str1)==len(str2)):
    if sorted(str1)==sorted(str2):
        print("aligrm")
    else:
        print(" not aligrm")
else:
    print("not aligrm due to length")
