import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 samples from normal distribution
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=1000)

# Compute descriptive statistics
mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

print("=== Normal Distribution - Descriptive Statistics ===")
print(f"Mean     : {mean:.4f}")
print(f"Variance : {variance:.4f}")
print(f"Std Dev  : {std_dev:.4f}")

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, edgecolor='black', color='steelblue', alpha=0.8)
plt.title("Histogram of Normal Distribution (n=1000)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.axvline(mean, color='red', linestyle='--', label=f'Mean = {mean:.2f}')
plt.legend()
plt.tight_layout()
plt.savefig("part_a1_histogram.png")
plt.show()
print("\nHistogram saved as part_a1_histogram.png")
