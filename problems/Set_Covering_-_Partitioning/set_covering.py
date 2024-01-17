from typing import List, Set, Dict

def greedy_set_cover(universe: Set[int], sets: List[Set[int]]) -> List[Set[int]]:
    """
    Solve the Set Covering problem using the Greedy Set Covering algorithm.

    Parameters:
    - universe: set, the universe of elements to be covered.
    - sets: list of sets, a collection of sets where each set is a subset of the universe.

    Returns:
    - list of sets, the chosen sets that cover the entire universe.
    
    Algorithm:
    1. Initialize an empty set C to represent the chosen sets.
    2. Create a copy of the universe U'.
    3. While U' is not empty:
       a. Select the set from S that covers the maximum number of uncovered elements in U'.
       b. Add this set to the chosen set C.
       c. Remove the covered elements from U'.
    4. The set C represents the selected sets that cover the entire universe.

    This version is adapted to use frozensets to handle the unhashable type issue with sets.
    """
    covered_elements = set()
    chosen_sets = []

    while covered_elements != set(universe):
        # Calculate the number of uncovered elements each set covers
        uncovered_counts = {frozenset(s): len(set(s) - covered_elements) for s in sets}
        
        # Select the set that covers the maximum number of uncovered elements
        best_set = max(uncovered_counts, key=uncovered_counts.get)
        
        # Add the chosen set to the solution
        chosen_sets.append(set(best_set))
        
        # Update the covered elements
        covered_elements |= set(best_set)

    return chosen_sets

# Example usage:
universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {2, 5, 7, 10}]

solution = greedy_set_cover(universe, sets)
print("Chosen sets:", solution)

input()


def weighted_set_cover(universe: Set[int], sets: List[Set[int]], weights: Dict[Set[int], float]):
    """
    Solve the Weighted Set Covering problem using a greedy algorithm.

    Parameters:
    - universe: set, the universe of elements to be covered.
    - sets: list of sets, a collection of sets where each set is a subset of the universe.
    - weights: dict, a dictionary mapping sets to their associated weights.

    Returns:
    - list of sets, the chosen sets that cover the entire universe.

    Algorithm:
    1. Initialize an empty set C to represent the chosen sets.
    2. Create a copy of the universe U'.
    3. While U' is not empty:
       a. Select the set from S that covers the maximum number of uncovered elements in U'.
       b. Add this set to the chosen set C.
       c. Remove the covered elements from U'.
    4. The set C represents the selected sets that cover the entire universe.

    This version extends the basic Set Covering algorithm by considering the weights associated with each set.
    """
    covered_elements = set()
    chosen_sets = []

    while covered_elements != set(universe):
        # Calculate the score for each set based on the number of uncovered elements and the set weight
        scores = {frozenset(s): weights[frozenset(s)] / len(set(s) - covered_elements) if len(set(s) - covered_elements) > 0 else 0 for s in sets}

        
        # Select the set with the maximum score
        best_set = max(scores, key=scores.get)
        
        # Add the chosen set to the solution
        chosen_sets.append(best_set)
        
        # Update the covered elements
        covered_elements |= set(best_set)

    return chosen_sets


universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {2, 5, 7, 10}, {10}]
weights = {frozenset({1, 2, 3}): 1.5, frozenset({4, 5, 6}): 2.0, frozenset({7, 8, 9}): 1.0, frozenset({2, 5, 7, 10}): 1.5, frozenset({10}):1.0}

solution = weighted_set_cover(universe, sets, weights)
print("Chosen sets:", solution)