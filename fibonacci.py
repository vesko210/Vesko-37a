n = int(input())
def Fibonacci(c, a = 0, b = 1):
    if c != 0:
        print(a)
        c -= 1
        Fibonacci(c,b,a+b)
Fibonacci(n + 2)
