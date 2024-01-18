import random

# Segna l'ordine delle città
# Quality:
#   vettore binario per rappresentare se l'elemento è presente
#   quality= somma dei flow (media distanze * media flow)/(somma delle distanze)
# Tweak:
#   Modifichiamo la soluzione
# IsIdeal:
#   non lo sappiamo

def greedy_assignment(flow_matrix, distance_matrix):

    """
    Function: greedy_assignment

    Description:
    This function employs a greedy algorithm to solve the facility assignment problem.
    It iteratively assigns facilities to locations based on minimizing the total cost.

    Parameters:
    - flow_matrix (List[List[int]]): Matrix representing the flow between facilities and locations.
    - distance_matrix (List[List[int]]): Matrix representing the distance between facilities and locations.

    Returns:
    List[int]: A list representing the assignment of facilities to locations.

    Example:
        # Example usage of the greedy_assignment function
        flow_matrix, distance_matrix = generate_random_instance(5)
        assignment_result = greedy_assignment(flow_matrix, distance_matrix)
        print(assignment_result)
    """

    n = len(flow_matrix)
    unassigned_facilities = set(range(n))
    assignment = [0] * n

    for location in range(n):
        min_cost = float('inf')
        best_facility = None

        for facility in unassigned_facilities:
            current_cost = sum(flow_matrix[i][facility] * distance_matrix[i][location] for i in range(n))
            if current_cost < min_cost:
                min_cost = current_cost
                best_facility = facility

        assignment[best_facility] = location
        unassigned_facilities.remove(best_facility)

    return assignment


def generate_random_instance(size):

    """
    Function: generate_random_instance
    
    Description:
    This function generates a random instance of the facility assignment problem.
    It creates random flow and distance matrices for a given problem size.
    
    Parameters:
    - size (int): The size of the problem instance.
    
    Returns:
    Tuple[List[List[int]], List[List[int]]]: Tuple containing the generated flow and distance matrices.
    
    Example:
        # Example usage of the generate_random_instance function
        flow_matrix, distance_matrix = generate_random_instance(5)
        print("Generated Flow Matrix:", flow_matrix)
        print("Generated Distance Matrix:", distance_matrix)
    """
    flow_matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
    distance_matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
    return flow_matrix, distance_matrix

size = 10  # You can change the size as needed
flow_matrix, distance_matrix = generate_random_instance(size)

print("Flow Matrix:")
for row in flow_matrix:
    print(row)

print("\nDistance Matrix:")
for row in distance_matrix:
    print(row)

result = greedy_assignment(flow_matrix, distance_matrix)
print("Greedy assignment:", result)