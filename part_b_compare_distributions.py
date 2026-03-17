import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate samples
np.random.seed(42)
normal_data = np.random.normal(loc=0, scale=1, size=1000)
uniform_data = np.random.uniform(low=-3, high=3, size=1000)

# Stats comparison
print("=== Distribution Comparison ===")
print(f"{'Metric':<20} {'Normal':>12} {'Uniform':>12}")
print("-" * 44)
print(f"{'Mean':<20} {np.mean(normal_data):>12.4f} {np.mean(uniform_data):>12.4f}")
print(f"{'Median':<20} {np.median(normal_data):>12.4f} {np.median(uniform_data):>12.4f}")
print(f"{'Std Dev':<20} {np.std(normal_data):>12.4f} {np.std(uniform_data):>12.4f}")
print(f"{'Variance':<20} {np.var(normal_data):>12.4f} {np.var(uniform_data):>12.4f}")
print(f"{'Skewness':<20} {stats.skew(normal_data):>12.4f} {stats.skew(uniform_data):>12.4f}")

# Plot both histograms side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(normal_data, bins=30, edgecolor='black', color='steelblue', alpha=0.8)
axes[0].set_title("Normal Distribution (mu=0, sigma=1)")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")
axes[0].axvline(np.mean(normal_data), color='red', linestyle='--', label='Mean')
axes[0].legend()

axes[1].hist(uniform_data, bins=30, edgecolor='black', color='darkorange', alpha=0.8)
axes[1].set_title("Uniform Distribution (low=-3, high=3)")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")
axes[1].axvline(np.mean(uniform_data), color='red', linestyle='--', label='Mean')
axes[1].legend()

plt.tight_layout()
plt.savefig("part_b_distributions.png")
plt.show()
print("\nPlot saved as part_b_distributions.png")

print("\n=== When to use each distribution ===")
print("Normal  : Modelling heights, test scores, measurement errors.")
print("          Use when data clusters symmetrically around a mean.")
print("Uniform : Modelling random events with equal likelihood (e.g., rolling a die).")
print("          Use when every outcome in a range is equally probable.")
