Practical No. 2 - Implement Fibonacci and Golden Section Search

def f(x):
    return (x-2)**2

def fibonacci_search(a,b,n):

    fib=[1,1]
    for i in range (2,n+1):
        fib.append(fib[i-1]+fib[i-2])

    k=1
    x1=a+(fib[n-2]/fib[n])*(b-a)
    x2=a+(fib[n-1]/fib[n])*(b-a)

    f1=f(x1)
    f2=f(x2)

    while k < n-1:

        if f1>f2:
            a=x1
            x1=x2
            f1=f2

            x2=a+(fib[n-k-1]/fib[n-k])*(b-a)
            f2=f(x2)

        else:

            b=x2
            x2=x1
            f2=f1

            x1=a+(fib[n-k-2]/fib[n-k])*(b-a)
            f1=f(x1)

        k = k + 1

    minimum=(a+b)/2

    print("Minimum Point=",minimum)
    print("Minimum Value=",f(minimum))

fibonacci_search(0,5,10)
