import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. Symbolic Verification
t = sp.symbols('t', real=True, positive=True)
T = sp.symbols('T', cls=sp.Function)
k = sp.symbols('k', real=True, positive=True)
Tm = 25

# Define the ODE
ode = sp.Eq(T(t).diff(t), -k * (T(t) - Tm))

# General solution
gen_sol = sp.dsolve(ode, T(t))
print(f"General Solution: {gen_sol.rhs}")

# Apply Initial Condition: T(0) = 100
ics = {T(0): 100}
particular_sol = sp.dsolve(ode, T(t), ics=ics)
print(f"Particular Solution with initial condition: {particular_sol.rhs}")

# Find value of k where T(10) = 75
k_eq = sp.Eq(particular_sol.rhs.subs(t, 10), 75)
k_val = sp.solve(k_eq, k)[0]
print(f"Calculated value of thermal constant k: {float(k_val):.5f}")

# 2. Numerical Evaluation & Plotting
final_expr = particular_sol.rhs.subs(k, k_val)
t_num = np.linspace(0, 60, 500)
# Lambda function to convert SymPy expression to a quick NumPy numerical function
T_num = sp.lambdify(t, final_expr, 'numpy')(t_num)

plt.figure(figsize=(8, 4.5))
plt.plot(t_num, T_num, 'r-', linewidth=2, label='Component Temp $T(t)$')
plt.axhline(Tm, color='k', linestyle='--', label='Ambient Temp $T_m=25^\circ C$')
plt.title("Thermal Component Cooling Profile (First-Order ODE)")
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle=':')
plt.legend()
plt.show()