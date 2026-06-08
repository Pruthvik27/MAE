import numpy as np

A = np.array([[1, 2, 3],
              [2, 4, 6],
              [3, 6, 9]])

b = np.array([[1], [3], [5]])
A_augmented = np.hstack((A, b))

rank_A = np.linalg.matrix_rank(A)
rank_aug = np.linalg.matrix_rank(A_augmented)

print("--- Existence and Uniqueness Test ---")
print(f"Rank of Coefficient Matrix A: {rank_A}")
print(f"Rank of Augmented Matrix [A|b]: {rank_aug}")

if rank_A != rank_aug:
    print("Result: Rank(A) != Rank([A|b]) -> System is INCONSISTENT (No Solution exists).")
elif rank_A == A.shape[1]:
    print("Result: Rank(A) == Number of variables -> System has a UNIQUE solution.")
else:
    print("Result: Rank(A) == Rank([A|b]) < Number of variables -> INFINITE solutions exist.")