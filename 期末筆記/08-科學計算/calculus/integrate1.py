import math

def integrate(f, a, b, h=0.001):
    area = 0
    x = a
    while (x < b):
        area += f(x)*h
        x += h
    return area

print('integrate(sin, 0, Pi)=', integrate(math.sin, 0, 3.14159))
