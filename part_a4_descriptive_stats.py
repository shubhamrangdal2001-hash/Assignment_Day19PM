import numpy as np
from scipy import stats

# Sample dataset - slightly right skewed
np.random.seed(10)
data = np.concatenate([
    np.random.normal(50, 10, 800),
    np.random.exponential(scale=20, size=200)
])

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Mode (using scipy)
mode_result = stats.mode(np.round(data).astype(int), keepdims=True)
mode_val = mode_result.mode[0]

# Standard deviation
std = np.std(data)

# Skewness
skewness = stats.skew(data)

print("=== Descriptive Statistics ===")
print(f"Mean     : {mean:.4f}")
print(f"Median   : {median:.4f}")
print(f"Mode     : {mode_val}")
print(f"Std Dev  : {std:.4f}")
print(f"Skewness : {skewness:.4f}")

# Interpret skewness
print("\n=== Skewness Interpretation ===")
if skewness > 0.5:
    print("The distribution is RIGHT (positively) skewed.")
    print("Tail is on the right. Mean > Median.")
elif skewness < -0.5:
    print("The distribution is LEFT (negatively) skewed.")
    print("Tail is on the left. Mean < Median.")
else:
    print("The distribution is approximately symmetric.")
