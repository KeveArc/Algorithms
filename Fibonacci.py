def Fibonacci_Rec(n):
    """Fibonacci function implemented"""
    try:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return Fibonacci_Rec(n-1) + Fibonacci_Rec(n-2)
    except:
        print('Incorrect input')




if __name__ == '__main__':
    print("1--> recurcisse implementation")
    l = [1] #list of existing implemetation of the Fibonacci function

    imp = int(input("wich implemetation do you want to use ?"))
    if imp in l:
        val = int(input("value you want to calculate the fib ? ")) #value to use to calculate the fib
        if imp == 1: print("the output value is {}".format(Fibonacci_Rec(val)))
    else:
        print("no such implementation exits in this project")

else:
    print('script imported by another module')
