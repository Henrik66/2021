import time

#f

x=array[40]=-1


def f(n,i):
    if n == 0:
        x[n]=0
        return (0,i)
    if n == 1:
        n[n]=1
        return (1,i)
    if n > 1:
        return f(n-1,i) + f(n-2,i)
    
