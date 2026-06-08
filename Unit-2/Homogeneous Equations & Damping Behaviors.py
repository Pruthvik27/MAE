import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t', real=True)
y = sp.symbols('y', cls=sp.Function)

def solve_damping(c_val):
    ode = sp.Eq(y(t).diff(t, 2) + c_val * y(t).diff(t) + 9 * y(t), 0)
    # Initial Conditions: y(0) = 2, y'(0) = 0
    sol = sp.dsolve(ode, y(t), ics={y(0): 2, y(t).diff(t).subs(t, 0): 0})
    return sol.rhs

# Generate mathematical solutions
y_over = solve_damping(c_val=10)
y_critical = solve_damping(c_val=6)
y_under = solve_damping(c_val=2)

print("Symbolic Underdamped Solution (c=2):")
sp.pprint(y_under)

# Numerical conversion and plotting
t_arr = np.linspace(0, 5, 500)
f_over = sp.lambdify(t, y_over, 'numpy')(t_arr)
f_critical = sp.lambdify(t, y_critical, 'numpy')(t_arr)
f_under = sp.lambdify(t, y_under, 'numpy')(t_arr)

plt.figure(figsize=(9, 5))
plt.plot(t_arr, f_over, 'g-', label='Overdamped (c=10)', linewidth=2)
plt.plot(t_arr, f_critical, 'b--', label='Critically Damped (c=6)', linewidth=2)
plt.plot(t_arr, f_under, 'r-', label='Underdamped (c=2)', linewidth=2)
plt.axhline(0, color='black', linestyle=':', alpha=0.5)
plt.title("Second-Order Response: The Three Damping States")
plt.xlabel("Time (seconds)")
plt.ylabel("Response $y(t)$")
plt.legend()
plt.grid(True, linestyle=':')
plt.show()