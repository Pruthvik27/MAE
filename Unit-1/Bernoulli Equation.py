import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t', real=True, positive=True)
y = sp.symbols('y', cls=sp.Function)

bernoulli_ode = sp.Eq(y(t).diff(t) + y(t)/t, t * y(t)**3)

# Solved symbolically directly with initial condition
sol_bern = sp.dsolve(bernoulli_ode, y(t), ics={y(1): 1})
print("Symbolic solution structure for non-linear Bernoulli Equation:")
sp.pprint(sol_bern)

# Note: The valid domain domain remains restricted due to log singularity boundaries (1 - 2*ln(t) > 0)
# This boundary occurs precisely around t = sqrt(e) ~ 1.648
t_vals = np.linspace(0.1, 1.62, 400)
y_vals = sp.lambdify(t, sol_bern.rhs, 'numpy')(t_vals)

plt.figure(figsize=(8, 4.5))
plt.plot(t_vals, y_vals, 'm-', linewidth=2, label='Bernoulli State Trajectory')
plt.title("Bernoulli Non-linear Transformed ODE Profile")
plt.xlabel("Time $t$")
plt.ylabel("State Variable $y(t)$")
plt.ylim(0, 10)
plt.grid(True)
plt.legend()
plt.show()