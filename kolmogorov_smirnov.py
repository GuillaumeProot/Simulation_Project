import math

def kolmogorov_smirnov_uniform_test(numbers):
    """
    Kolmogorov-Smirnov test for uniform distribution
    param : numbers list of Pi's decimals 
    return: p-value
    """
    n = len(numbers)
    # Compute the empirical distribution
    empirical_distribution = [0] * n
    for i in range(n):
        empirical_distribution[i] = numbers[i] / n

    # Compute the theoretical distribution
    theoretical_distribution = [0] * n
    for i in range(n):
        theoretical_distribution[i] = i / n

    # Compute the max distance
    max_distance = 0
    for i in range(n):
        max_distance = max(max_distance, abs(empirical_distribution[i] - theoretical_distribution[i]))

    # Compute the p-value
    p_value = 0
    for i in range(n):
        p_value += max(abs(empirical_distribution[i] - theoretical_distribution[i]), max_distance - abs(empirical_distribution[i] - theoretical_distribution[i]))

    if p_value/n > math.sqrt(1.36 * (1 / n)):
        return False
    else:
        return True
