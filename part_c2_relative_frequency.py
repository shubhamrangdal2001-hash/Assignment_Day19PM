# Part C - Q2: Compute probability from frequency data (relative frequency approach)

def compute_probability(event, frequency_data):
    """
    Computes probability of an event using relative frequency.

    Parameters:
        event         : The outcome we want probability for
        frequency_data: dict with outcome -> count

    Returns:
        Probability of the event (float)
    """
    total = sum(frequency_data.values())
    if total == 0:
        raise ValueError("Total frequency cannot be zero.")
    if event not in frequency_data:
        return 0.0
    return frequency_data[event] / total


# Example: frequency of outcomes when rolling a die 60 times
frequency_data = {
    1: 9,
    2: 11,
    3: 10,
    4: 8,
    5: 12,
    6: 10
}

print("=== Relative Frequency - Probability Calculation ===")
print(f"{'Outcome':<10} {'Frequency':<12} {'Probability':<12}")
print("-" * 34)
total = sum(frequency_data.values())
for outcome, freq in frequency_data.items():
    prob = compute_probability(outcome, frequency_data)
    print(f"{outcome:<10} {freq:<12} {prob:.4f}")

print(f"\nTotal observations: {total}")
print(f"\nP(rolling a 5) = {compute_probability(5, frequency_data):.4f}")
print(f"P(rolling a 1) = {compute_probability(1, frequency_data):.4f}")

# Verify sum of all probabilities = 1
total_prob = sum(compute_probability(k, frequency_data) for k in frequency_data)
print(f"\nSum of all probabilities = {total_prob:.4f}")
