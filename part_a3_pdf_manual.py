import numpy as np
import matplotlib.pyplot as plt
import math

# Manual implementation of Normal PDF
# Formula: f(x) = (1 / (sigma * sqrt(2*pi))) * exp(-0.5 * ((x - mu) / sigma)^2)

def normal_pdf(x, mu, sigma):
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coefficient * math.exp(exponent)

# Parameters
mu = 0
sigma = 1

# Generate x values
x_values = np.linspace(-4, 4, 300)
y_values = [normal_pdf(x, mu, sigma) for x in x_values]

print("=== Manual Normal PDF (mu=0, sigma=1) ===")
print(f"{'x':<8} {'PDF(x)':<12}")
print("-" * 20)
# Print a few sample values
for x in [-2, -1, 0, 1, 2]:
    print(f"{x:<8} {normal_pdf(x, mu, sigma):.6f}")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, color='darkorange', linewidth=2)
plt.fill_between(x_values, y_values, alpha=0.2, color='darkorange')
plt.title("Normal PDF (Manual Implementation, mu=0, sigma=1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("part_a3_pdf.png")
plt.show()
print("\nPDF plot saved as part_a3_pdf.png")
