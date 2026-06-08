import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 2000  # Sampling Frequency (Hz)
dt = 1.0 / fs
time_axis = np.arange(0, 0.2, dt) # Track for 200ms window

# Waveform voltage containing 50Hz fundamental and 250Hz switching noise
voltage_wave = 12 * np.sin(2 * np.pi * 50 * time_axis) + 4 * np.sin(2 * np.pi * 250 * time_axis)

# Process FFT
fft_computed = np.fft.fft(voltage_wave)
freq_bins = np.fft.fftfreq(len(time_axis), d=dt)

# Filter for the positive frequency spectrum half
half_len = len(time_axis) // 2
display_freqs = freq_bins[:half_len]
normalized_mags = np.abs(fft_computed)[:half_len] * (2.0 / len(time_axis))

# Graphing Time Domain vs Frequency Domain side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))
ax1.plot(time_axis, voltage_wave, 'g-', linewidth=2)
ax1.set_title("Voltage Waveform (Time Domain)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Voltage (V)")
ax1.grid(True)

ax2.stem(display_freqs, normalized_mags, 'r', basefmt='k-')
ax2.set_xlim(0, 400)
ax2.set_title("FFT Discrete Frequency Spectrum")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Voltage Magnitude (V)")
ax2.grid(True)

plt.tight_layout()
plt.show()