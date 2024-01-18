# Segna l'ordine delle città
# Quality:
#   vettore binario per rappresentare se l'elemento è presente
#   quality= somma peso in knapsack rapportato al costo - alpha* somma peso che esce fuori dal knapsack
# Tweak:
#   Modifichiamo la soluzione
# IsIdeal:
#   non lo sappiamo

def knapsack_01(weights, values, capacity):

    """
    Solve the 0/1 Knapsack problem using dynamic programming.

    Parameters:
    - weights: list of integers, representing the weights of items.
    - values: list of integers, representing the values of items.
    - capacity: integer, the maximum weight capacity of the knapsack.

    Returns:
    - integer, the maximum total value that can be obtained by selecting items for the knapsack.

    Algorithm:
    - Dynamic programming approach with a 2D table (dp) to store intermediate results.
    - dp[i][w] represents the maximum value that can be obtained with the first i items and a knapsack of weight w.
    - Fills the dp table iteratively, considering whether to include each item or not.

    Example usage:
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_value = knapsack_01(weights, values, capacity)
    print("Maximum value for 0/1 Knapsack:", max_value)
    """

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage:
weights = [2, 3, 4, 5, 1, 3]
values = [3, 4, 5, 6, 1, 9]
capacity = 5

max_value = knapsack_01(weights, values, capacity)
print("Maximum value for 0/1 Knapsack:", max_value)


def knapsack_fractional(weights, values, capacity):

    """
    Solve the Fractional Knapsack problem using a greedy algorithm.

    Parameters:
    - weights: list of integers, representing the weights of items.
    - values: list of integers, representing the values of items.
    - capacity: integer, the maximum weight capacity of the knapsack.

    Returns:
    - float, the maximum total value that can be obtained by selecting items for the knapsack,
      considering fractional parts of items.

    Algorithm:
    - Calculate the value-to-weight ratios for each item and sort them in descending order.
    - Iterate through the sorted ratios, adding items to the knapsack until the capacity is exhausted.
    - If an item cannot be fully added, include a fractional part based on the remaining capacity.

    Example usage:
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_value_fractional = knapsack_fractional(weights, values, capacity)
    print("Maximum value for Fractional Knapsack:", max_value_fractional)
    """

    n = len(weights)
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    remaining_capacity = capacity

    for ratio, weight, value in ratios:
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_value += fraction * value
            break

    return total_value

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value_fractional = knapsack_fractional(weights, values, capacity)
print("Maximum value for Fractional Knapsack:", max_value_fractional)