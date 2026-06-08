import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t, s = sp.symbols('t s', real=True, positive=True)
f_step = (t - 2)**2 * sp.Heaviside(t - 2)

F_step, _, _ = sp.laplace_transform(f_step, t, s)
print("Laplace Transform with Heaviside Shift Function:")
sp.pprint(F_step)

t_arr = np.linspace(0, 5, 500)
f_step_num = sp.lambdify(t, f_step, 'numpy')(t_arr)

plt.figure(figsize=(8, 3.5))
plt.plot(t_arr, f_step_num, 'm-', linewidth=2, label='$(t-2)^2 u(t-2)$')
plt.axvline(2, color='r', linestyle='--', label='Delay Threshold ($t=2$)')
plt.title("Delayed Step Response Profile")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()