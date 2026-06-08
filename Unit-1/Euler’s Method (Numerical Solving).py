import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define derivative function f(t, i)
def di_dt(t, i):
    return 10 - 2 * i

# 1. Manual Implementation of Euler's Method
h = 0.2
t_start, t_end = 0, 1.5
steps = int((t_end - t_start) / h) + 1

t_euler = np.zeros(steps)
i_euler = np.zeros(steps)
i_euler[0] = 0.0 # Initial condition

for n in range(0, steps - 1):
    t_euler[n+1] = t_euler[n] + h
    i_euler[n+1] = i_euler[n] + h * di_dt(t_euler[n], i_euler[n])

print(f"Euler approximation at t = 0.4s: {i_euler[2]:.2f} A")

# 2. High-Precision Numerical Solver for baseline verification
t_span = (t_start, t_end)
sol = solve_ivp(di_dt, t_span, [0], t_eval=np.linspace(t_start, t_end, 200))

# Plotting Comparison
plt.figure(figsize=(8, 4.5))
plt.plot(sol.t, sol.y[0], 'b-', label='High-precision ODE Solver (Exact baseline)')
plt.step(t_euler, i_euler, 'r-o', where='post', label=f"Euler's Method ($h={h}$)")
plt.title("Euler's Method Numerical Estimation vs Accurate Baseline")
plt.xlabel("Time (seconds)")
plt.ylabel("Current $i(t)$ (Amperes)")
plt.legend()
plt.grid(True)
plt.show()