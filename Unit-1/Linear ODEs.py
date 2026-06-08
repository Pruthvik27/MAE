import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t', real=True, positive=True)
y = sp.symbols('y', cls=sp.Function)

# State equation directly
linear_ode = sp.Eq(t * y(t).diff(t) + 2 * y(t), t**2 - t + 1)

# Solve with boundary conditions
sol_linear = sp.dsolve(linear_ode, y(t), ics={y(sp.Integer(1)): sp.Rational(1, 2)})
print("Verified Symbolic Solution Matrix:")
sp.pprint(sol_linear)

# Vectorize for dynamic tracking
t_domain = np.linspace(0.5, 3.0, 300)
y_domain = sp.lambdify(t, sol_linear.rhs, 'numpy')(t_domain)

plt.figure(figsize=(8, 4.5))
plt.plot(t_domain, y_domain, 'g-', linewidth=2, label='$y(t)$ Trajectory')
plt.scatter([1.0], [0.5], color='red', zorder=5, label='Initial Constraint (1, 0.5)')
plt.title("Analytical Solution of 1st-Order Linear ODE")
plt.xlabel("Independent variable $t$")
plt.ylabel("$y(t)$ Value")
plt.legend()
plt.grid(True)
plt.show()