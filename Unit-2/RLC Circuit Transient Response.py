import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. Transient Simulation
t = sp.symbols('t', real=True, positive=True)
i = sp.symbols('i', cls=sp.Function)

# Parameters
L, R, C = 1.0, 2.0, 0.25

rlc_ode = sp.Eq(L * i(t).diff(t, 2) + R * i(t).diff(t) + (1/C) * i(t), 0)
# Applied initial constraints: i(0) = 0, i'(0) = 12
rlc_sol = sp.dsolve(rlc_ode, i(t), ics={i(0): 0, i(t).diff(t).subs(t, 0): 12})

print("Analytical Expression for RLC Loop Current i(t):")
sp.pprint(rlc_sol)

# 2. AC Resonance Frequency Sweep Calculation
# Impedance Z = sqrt( R^2 + (omega*L - 1/(omega*C))^2 )
# Current Amplitude I0 = E0 / Z
omega_vals = np.linspace(0.1, 5.0, 1000)
E0 = 10.0 # Peak AC Input Voltage
Z = np.sqrt(R**2 + (omega_vals * L - 1 / (omega_vals * C))**2)
I0_amplitude = E0 / Z

# Peak theoretical resonance occurs at omega_0 = 1 / sqrt(LC)
omega_0 = 1 / np.sqrt(L * C)
print(f"\nTheoretical Resonant Frequency (omega_0) = {omega_0:.2f} rad/s")

# Plotting Results Side-by-Side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Transient Response
t_vals = np.linspace(0, 6, 500)
i_vals = sp.lambdify(t, rlc_sol.rhs, 'numpy')(t_vals)
ax1.plot(t_vals, i_vals, 'b-', linewidth=2, label='Current $i(t)$')
ax1.axhline(0, color='black', linestyle=':', alpha=0.6)
ax1.set_title("RLC Circuit DC Turn-On Transient Response")
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Current (Amperes)")
ax1.grid(True)
ax1.legend()

# Plot 2: Frequency Sweep (Resonance curve)
ax2.plot(omega_vals, I0_amplitude, 'r-', linewidth=2, label='Current Peak Amplitude')
ax2.axvline(omega_0, color='k', linestyle='--', label=f'Resonance Peak ({omega_0:.1f} rad/s)')
ax2.set_title("AC Frequency Sweep & System Resonance Peak")
ax2.set_xlabel("Frequency $\omega$ (rad/s)")
ax2.set_ylabel("Peak Current $I_0$ (Amperes)")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()