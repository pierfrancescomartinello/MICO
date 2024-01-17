def subset_sum(nums, target_sum):
    """
    Solve the Subset Sum problem and return the subset using dynamic programming.

    Parameters:
    - nums: list of integers, representing the set of numbers.
    - target_sum: integer, the target sum to be achieved.

    Returns:
    - list of integers, the subset that adds up to the target sum if it exists,
      an empty list otherwise.

    Algorithm:
    - Dynamic programming approach with a 2D table (dp) to store intermediate results.
    - dp[i][j] is True if there exists a subset of the first i numbers that adds up to j.
    - Fills the dp table iteratively based on whether each number is included or not.

    Example usage:
    nums = [3, 34, 4, 12, 5, 2]
    target_sum = 9
    result = subset_sum(nums, target_sum)
    print("Subset with sum", target_sum, "exists:", result)
    """
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: an empty subset can always achieve a sum of 0
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If the current number is greater than the target sum, skip it
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Include the current number or exclude it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    # Reconstruct the subset
    subset = []
    i, j = n, target_sum
    while i > 0 and j > 0:
        if dp[i][j] and not dp[i - 1][j]:
            subset.append(nums[i - 1])
            j -= nums[i - 1]
        i -= 1

    return subset[::-1]

# Example usage:
nums = [3, 34, 4, 12, 5, 2]
target_sum = 9
result = subset_sum(nums, target_sum)
print("Subset with sum", target_sum, "exists:", result)