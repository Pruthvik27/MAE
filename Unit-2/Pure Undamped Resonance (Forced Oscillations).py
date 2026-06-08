import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t', real=True)
y = sp.symbols('y', cls=sp.Function)

# System model with an identical internal natural frequency and external input frequency
resonance_ode = sp.Eq(y(t).diff(t, 2) + 9 * y(t), 8 * sp.cos(3 * t))
sol_res = sp.dsolve(resonance_ode, y(t), ics={y(0): 0, y(t).diff(t).subs(t, 0): 0})

print("Analytical Expression Showing Pure Physical Resonance:")
sp.pprint(sol_res)

# Generate time data to view structural growth
t_range = np.linspace(0, 15, 600)
y_res_num = sp.lambdify(t, sol_res.rhs, 'numpy')(t_range)

# Create tracking envelope boundaries (+- 4/3 * t) to show amplitude growth trend
envelope = (4.0 / 3.0) * t_range

plt.figure(figsize=(9, 4.5))
plt.plot(t_range, y_res_num, 'r-', label='Resonant Oscillation Output')
plt.plot(t_range, envelope, 'b--', alpha=0.6, label='Amplitude Envelope ($\pm \\frac{4}{3}t$)')
plt.plot(t_range, -envelope, 'b--', alpha=0.6)
plt.title("Pure Undamped Resonance Amplitude Growth Profile")
plt.xlabel("Time (seconds)")
plt.ylabel("Displacement / Voltage Amplitude")
plt.grid(True)
plt.legend(loc='upper left')
plt.show()