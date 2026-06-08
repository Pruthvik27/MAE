import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t', real=True)
x, y = sp.symbols('x y', cls=sp.Function)

eq1 = sp.Eq(x(t).diff(t) + y(t), sp.exp(t))
eq2 = sp.Eq(y(t).diff(t) - x(t), 0)

# Solve the coupled differential system
solutions = sp.dsolve([eq1, eq2], [x(t), y(t)], ics={x(0): 0, y(0): 0})
print("Coupled System Analytical Solutions:")
sp.pprint(solutions)

# Extract and plot the variables
t_space = np.linspace(0, 2.5, 500)
x_net = sp.lambdify(t, solutions[0].rhs, 'numpy')(t_space)
y_net = sp.lambdify(t, solutions[1].rhs, 'numpy')(t_space)

plt.figure(figsize=(9, 4.5))
plt.plot(t_space, x_net, 'g-', linewidth=2, label='Network State $x(t)$')
plt.plot(t_space, y_net, 'r--', linewidth=2, label='Network State $y(t)$')
plt.title("Coupled Electrical System Loop Response")
plt.xlabel("Time (s)")
plt.ylabel("State Vector Scaling")
plt.grid(True, linestyle=':')
plt.legend()
plt.show()