import numpy as np

A = np.array([[4.0, 2.0],
              [2.0, 4.0]])

# Compute values and vectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("--- Eigen-Analysis Matrix Solution ---")
for i in range(len(eigenvalues)):
    print(f"Eigenvalue λ_{i+1} = {eigenvalues[i]:.1f}")
    print(f"Corresponding Normalized Eigenvector v_{i+1} = {eigenvectors[:, i]}\n")