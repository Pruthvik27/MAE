import sympy as sp

t, s = sp.symbols('t s', real=True, positive=True)
f_div_t = sp.sin(t) / t

F_div, _, _ = sp.laplace_transform(f_div_t, t, s)
print("Laplace Transform via Frequency Domain Integration:")
sp.pprint(F_div)