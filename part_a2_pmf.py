import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Binomial PMF: P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
def binomial_pmf(n, p):
    k_values = list(range(n + 1))
    probabilities = [comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in k_values]
    return k_values, probabilities

# Parameters
n = 10    # number of trials
p = 0.5   # probability of success

k_values, probs = binomial_pmf(n, p)

# Verify total probability sums to 1
total = sum(probs)
print("=== Binomial PMF (n=10, p=0.5) ===")
print(f"{'k':<5} {'P(X=k)':<10}")
print("-" * 15)
for k, prob in zip(k_values, probs):
    print(f"{k:<5} {prob:.6f}")

print(f"\nTotal probability = {total:.6f}")
print("Sums to 1:", round(total, 10) == 1.0)

# Plot PMF
plt.figure(figsize=(8, 5))
plt.bar(k_values, probs, color='steelblue', edgecolor='black', alpha=0.8)
plt.title(f"Binomial PMF (n={n}, p={p})")
plt.xlabel("k (Number of Successes)")
plt.ylabel("P(X = k)")
plt.xticks(k_values)
plt.tight_layout()
plt.savefig("part_a2_pmf.png")
plt.show()
print("\nPMF plot saved as part_a2_pmf.png")
