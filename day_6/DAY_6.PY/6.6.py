"""     to check whether the given number is even or odd by using
        single stance class obj with an attribytte following the constructor
        test case
        21                                                                  """
class num:
    def __init__(self,var):
        self.var=var
        if var%2==0:
            print("even number")
        else:
            print("odd number")
i=int(input("enter number:"))
obj=num(i)

