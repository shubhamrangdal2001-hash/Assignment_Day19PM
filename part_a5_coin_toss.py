import numpy as np

# Simulate 1000 coin tosses
# 0 = Tails, 1 = Heads
np.random.seed(7)
tosses = np.random.randint(0, 2, size=1000)

# Count heads
heads = np.sum(tosses)
tails = 1000 - heads

# Estimated probability of heads
estimated_prob = heads / 1000
theoretical_prob = 0.5

print("=== Coin Toss Simulation (1000 tosses) ===")
print(f"Heads count       : {heads}")
print(f"Tails count       : {tails}")
print(f"Estimated P(H)    : {estimated_prob:.4f}")
print(f"Theoretical P(H)  : {theoretical_prob:.4f}")
print(f"Difference        : {abs(estimated_prob - theoretical_prob):.4f}")

print("\n=== Observation ===")
print("As the number of trials increases, the estimated probability")
print("converges towards the theoretical probability of 0.5.")
print("This is consistent with the Law of Large Numbers.")
