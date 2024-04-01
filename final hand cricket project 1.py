import random
print("even or odd:")
decision=input()
syst = random.randint(1,10)
user=int(input("enter the num:"))
print("system:",syst)
sum=syst+user
a=0
b=0
if sum%2==0:
    a="EVEN"
    print(a)
else:
    b="ODD"
    print(b)


if decision.upper()==a or decision.upper()==b:
    print(decision)
    print(" 1 for batting,2 for bowling")
    playtype=int(input("choose the playtype"))
    if playtype==1:
        print("user batting")
        n=1
        score_user=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                
                if syst!=user:
                    score_user=score_user+user
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        print("system batting")
        n=1
        score_syst=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                if syst!=user:
                    score_syst=score_syst+syst
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        if score_user>score_syst:
            print("user won")
        print("system won")
    else:
        print("system batting")
        n=1
        score_syst=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                if syst!=user:
                    score_syst=score_syst+syst
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        print("user batting")
        n=1
        score_user=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                if syst!=user:
                    score_user=score_user+user
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        if score_user>score_syst:
            print("user won")
        print("system won")
else:
    print(decision)
    print(" 1 for batting,2 for bowling")
    playtype=random.randint(1,2)
    if playtype==1:
        print("system batting")
        n=1
        score_syst=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                if syst!=user:
                    score_syst=score_syst+syst
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        print("user batting")
        n=1
        score_user=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                if syst!=user:
                    score_user=score_user+user
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        if score_user>score_syst:
            print("user won")
        print("system won")
    else:
        print("user batting")
        n=1
        score_user=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                if syst!=user:
                    score_user=score_user+user
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        print("system batting")
        n=1
        score_syst=0
        while n==1:
            syst = random.randint(1,10)
            user=int(input("enter the num:"))
            print(syst)
            if user<=10:
                if syst!=user:
                    score_syst=score_syst+syst
                else:
                    print("Bowled")
                    n=0
            else:
                print("enter the value between 1 and 10:")
        if score_user>score_syst:
            print("user won")
        print("system won")
