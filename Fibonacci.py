#approach using callable class for memoization
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def Fibonacci_Mem_call(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Mem_call(n-1) + Fibonacci_Mem_call(n-2)


#Fibonacci function using a loop -- method 3
def Fibonacci_loop(n):

    l = [0, 1]
    for _ in range(n-1):
        x = sum(l[-2:])
        l.append(x)
    return l[-1]


#memoize approach -- method 2
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def Fibonacci_Mem(n):
    """Fibonacci function implemented"""
    try:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Fibonacci_Mem(n-1) + Fibonacci_Mem(n-2)
    except:
        print('Incorrect input')


#simple recurcisse function -- method 1
def Fibonacci_Rec(n):
    """Fibonacci function implemented"""
    try:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Fibonacci_Rec(n-1) + Fibonacci_Rec(n-2)
    except:
        print('Incorrect input')



if __name__ == '__main__':
    print("1--> recurcisse implementation, 2--> memoize approach, 3--> loop approach, 4--> memoize + callable")
    l = [1, 2, 3, 4] #list of existing implemetation of the Fibonacci function

    imp = int(input("wich implementation do you want to use ? "))

    if imp in l:
        val = int(input("value you want to calculate the fib ? ")) #value to use to calculate the fib
        if imp == 1:
            print("the output value is {}".format(Fibonacci_Rec(val)))
        elif imp == 2:
            print("the output value is {}".format(Fibonacci_Mem(val)))
        elif imp == 3:
            print("the output value is {}".format(Fibonacci_loop(val)))
        elif imp == 4:
            print("the output value is {}".format(Fibonacci_Mem_call(val)))
    else:
        print("no such implementation exits in this project")
else:
    print('script imported by another module')
