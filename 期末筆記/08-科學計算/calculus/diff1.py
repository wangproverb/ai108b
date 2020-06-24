import math

def df(f, x, h=0.00001):
    return (f(x+h)-f(x))/h

print('df(sin, 3.14159/4)=', df(math.sin, 3.14159/4))
