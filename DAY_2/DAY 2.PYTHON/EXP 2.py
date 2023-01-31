a=int(input("enter the day no:"))

if a>84:
        print("your plan is expired,kindly recharge")
        
else :
        b=int(input("enter no of calls:"))
        c=int(input("enter the no of msgs sent:"))
        d=float(input("enter the data :"))
        print("you have plan upto",84-a,"days")
        
        if b>=3000:
            print("your talktime is expired and 90 rupees topup")
        else :
            print("you have",3000-b,"calls left")
        if c>=100:
            print("msg limit is over")
        else :
            print("you have",100-c,"msgs left")
        if d>=2.0:
            print("your data limit is over")
        else :
            print("you have",2.0-d,"data left") 
        
