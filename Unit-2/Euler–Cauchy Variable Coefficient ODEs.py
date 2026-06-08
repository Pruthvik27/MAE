import sympy as sp

t = sp.symbols('t', real=True, positive=True)
y = sp.symbols('y', cls=sp.Function)

euler_cauchy_ode = sp.Eq(t**2 * y(t).diff(t, 2) - 3 * t * y(t).diff(t) + 3 * y(t), 0)
sol_ec = sp.dsolve(euler_cauchy_ode, y(t))

print("Euler-Cauchy General Solution:")
sp.pprint(sol_ec)