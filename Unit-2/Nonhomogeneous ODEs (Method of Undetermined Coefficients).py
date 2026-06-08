import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t', real=True)
y = sp.symbols('y', cls=sp.Function)

# Define the nonhomogeneous differential equation
nonhom_ode = sp.Eq(y(t).diff(t, 2) + 3 * y(t).diff(t) + 2 * y(t), 4 * t**2)

# Solve with explicit boundary constraints
sol_nonhom = sp.dsolve(nonhom_ode, y(t), ics={y(0): 0, y(t).diff(t).subs(t, 0): 0})
print("Analytical Solution for Nonhomogeneous ODE:")
sp.pprint(sol_nonhom)

# Vectorize and plot the output
t_vals = np.linspace(0, 3, 300)
y_vals = sp.lambdify(t, sol_nonhom.rhs, 'numpy')(t_vals)

plt.figure(figsize=(8, 4))
plt.plot(t_vals, y_vals, 'k-', linewidth=2, label='System Response $y(t)$')
plt.title("Transient + Particular Response of a Nonhomogeneous System")
plt.xlabel("Time ($t$)")
plt.ylabel("Response ($y$)")
plt.grid(True, linestyle=':')
plt.legend()
plt.show()