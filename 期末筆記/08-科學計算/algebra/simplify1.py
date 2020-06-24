import sympy as sp

x = sp.symbols("x")
exp = sp.simplify((x+2)**2-(x+1)**2)
print('exp=', exp)
