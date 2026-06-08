import sympy as sp

t, s = sp.symbols('t s', real=True, positive=True)
f_base = t * sp.cos(2*t)
f_deriv = sp.diff(f_base, t)

F_deriv_s, _, _ = sp.laplace_transform(f_deriv, t, s)
print("Laplace Transform of the Derivative Expression:")
sp.pprint(sp.simplify(F_deriv_s))