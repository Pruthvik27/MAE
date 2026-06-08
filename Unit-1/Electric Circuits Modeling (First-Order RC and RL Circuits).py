import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. Structural Parameter Setups
R_val = 10.0   # Ohms
L_val = 2.0    # Henries
E_val = 40.0   # Volts

tau = L_val / R_val  # Circuit Time Constant
print(f"Circuit Transient Time Constant (tau) = {tau} seconds")
print(f"Expected 99% Steady State reached at ~5*tau = {5*tau} seconds")

# 2. Define Symbolic Framework
t = sp.symbols('t', real=True, positive=True)
i = sp.symbols('i', cls=sp.Function)

rl_circuit_eq = sp.Eq(L_val * i(t).diff(t) + R_val * i(t), E_val)
rl_sol = sp.dsolve(rl_circuit_eq, i(t), ics={i(0): 0})

print("\nAnalytical Loop Current Expression:")
sp.pprint(rl_sol)

# 3. Graphing Transient Curves
t_axis = np.linspace(0, 1.5, 500)
i_axis = sp.lambdify(t, rl_sol.rhs, 'numpy')(t_axis)

plt.figure(figsize=(9, 5))
plt.plot(t_axis, i_axis, 'b-', linewidth=2.5, label='Transient Loop Current $i(t)$')
plt.axhline(E_val/R_val, color='r', linestyle='--', label=f'Steady State Max Threshold ({E_val/R_val}A)')
plt.axvline(tau, color='gray', linestyle=':', label=f'1 Time Constant (tau = {tau}s)')

plt.title("Transient Response Curve of a Series RL Circuit", fontsize=12)
plt.xlabel("Time (seconds)", fontsize=10)
plt.ylabel("Current (Amperes)", fontsize=10)
plt.grid(True, alpha=0.4)
plt.legend(loc='lower right')
plt.show()