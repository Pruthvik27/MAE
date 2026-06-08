import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t, s = sp.symbols('t s', real=True, positive=True)
f_t = sp.exp(-3*t) * sp.sin(4*t)

# Symbolic Transform Execution
F_s, _, _ = sp.laplace_transform(f_t, t, s)
print("Symbolic Laplace Transform F(s):")
sp.pprint(sp.simplify(F_s))

# Numerical plotting
t_vals = np.linspace(0, 2, 500)
f_num = sp.lambdify(t, f_t, 'numpy')(t_vals)

plt.figure(figsize=(8, 3.5))
plt.plot(t_vals, f_num, 'b-', linewidth=2, label='$e^{-3t}\sin(4t)$')
plt.axhline(0, color='black', linestyle=':', alpha=0.5)
plt.title("Time-Domain Damped Sinusoidal Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()