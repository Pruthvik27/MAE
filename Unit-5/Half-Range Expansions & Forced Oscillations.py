import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 15, 1000)
y_steady = np.zeros_like(t)

# Summing responses for non-resonant modes (n=1, n=2, n=4, n=5)
for n in [1, 2, 4, 5]:
    b_n = 2.0 / n
    A_n = b_n / (9.0 - n**2)
    y_steady += A_n * np.sin(n * t)

# Particular solution for the resonant 3rd harmonic: yp_3 = (-b_3 / (2*omega_0)) * t * cos(omega_0 * t)
b_3 = 2.0 / 3.0
y_resonant = (-b_3 / (2 * 3.0)) * t * np.cos(3 * t)

y_total = y_steady + y_resonant

plt.figure(figsize=(8, 4))
plt.plot(t, y_total, 'm-', label='Total Output $y(t)$')
plt.plot(t, (b_3/6)*t, 'k:', label='Resonant Envelope Boundary')
plt.plot(t, -(b_3/6)*t, 'k:')
plt.title("Forced System Output showing 3rd-Harmonic Resonance Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Response Amplitude")
plt.grid(True)
plt.legend()
plt.show()