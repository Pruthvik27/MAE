import numpy as np
import matplotlib.pyplot as plt

# Define parameters
L = 2.0
t = np.linspace(-4, 4, 1000)

def fourier_arbitrary(t, L, num_harmonics):
    series_sum = np.zeros_like(t)
    for n in range(1, num_harmonics + 1):
        b_n = (4 * (-1)**(n + 1)) / (n * np.pi)
        series_sum += b_n * np.sin((n * np.pi * t) / L)
    return series_sum

plt.figure(figsize=(8, 4))
plt.plot(t, t % (2*L) - L, 'k--', label='Exact Waveform (Sawtooth)', alpha=0.5)
plt.plot(t, fourier_arbitrary(t, L, 3), 'b-.', label='3 Harmonics')
plt.plot(t, fourier_arbitrary(t, L, 25), 'r-', label='25 Harmonics (Converged)')
plt.title("Fourier Series with Arbitrary Period ($2L=4$)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True, linestyle=':')
plt.legend()
plt.show()