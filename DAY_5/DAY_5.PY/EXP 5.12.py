from  datetime import*
d=date.today()
print(d)
i=date(2023,2,3)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)
