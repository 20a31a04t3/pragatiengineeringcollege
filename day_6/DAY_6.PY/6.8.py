class circle(self):
    a=3.14759
    def fun(self,val):
        self.val=val
        area =circle.a*val*val
        cir=2*circle.a*val
        print(area)
        print(cir)
num=float(input("enter radius:"))
obj=circle()
obj.circle(num)

