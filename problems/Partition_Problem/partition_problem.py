# Segna l'ordine delle città
# Quality:
#   vettore n-ario per rappresentare se l'elemento è presente nell'insieme n
#   quality= somma elementi/numero di bin - deviazione dalla media per ogni singolo elemento
# Tweak:
#   Modifichiamo la soluzione
# IsIdeal:
#   non lo sappiamo


def partition_greedy(nums):
    # Step 1: Sort the numbers in descending order
    sorted_nums = sorted(nums, reverse=True)

    # Step 2: Initialize subsets and their sums
    subsets = [[] for _ in range(len(nums))]
    subset_sums = [0] * len(nums)

    # Step 3: Assign each number to the subset with the smaller sum
    for num in sorted_nums:
        min_sum_index = subset_sums.index(min(subset_sums))
        subsets[min_sum_index].append(num)
        subset_sums[min_sum_index] += num

    return subsets, subset_sums

# Example usage:
numbers = [1, 5, 11, 5, 2, 7, 3]
result_sets, result_sums = partition_greedy(numbers)

# Determine the number of sets based on the sums
num_sets = len(set(result_sums))

if num_sets > 1:
    print(f"Partition successful into {num_sets} sets:")
    for i in range(num_sets):
        print(f"Subset {i + 1}: {result_sets[i]} (Sum: {result_sums[i]})")
else:
    print("Partition not possible.")


def partition_greedy_with_sets(nums, num_sets):
    # Step 1: Sort the numbers in descending order
    sorted_nums = sorted(nums, reverse=True)

    # Step 2: Initialize subsets and their sums
    subsets = [[] for _ in range(num_sets)]
    subset_sums = [0] * num_sets

    # Step 3: Assign each number to the subset with the smaller sum
    for num in sorted_nums:
        min_sum_index = subset_sums.index(min(subset_sums))
        subsets[min_sum_index].append(num)
        subset_sums[min_sum_index] += num

    return subsets, subset_sums

# Example usage:
numbers = [1, 5, 11, 5, 2, 7, 3]
desired_num_sets = 3

# Check if the desired number of sets is feasible
if desired_num_sets > 0 and desired_num_sets <= len(numbers):
    result_sets, result_sums = partition_greedy_with_sets(numbers, desired_num_sets)
    print(f"Partition successful into {desired_num_sets} sets:")
    for i in range(desired_num_sets):
        print(f"Subset {i + 1}: {result_sets[i]} (Sum: {result_sums[i]})")
else:
    print("Invalid number of sets specified.")