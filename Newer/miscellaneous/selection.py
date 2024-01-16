from typing import Any, Callable, List
import random
from miscellaneous import pareto_dominance as p_d

if __name__ == "__main__":
    Vector = List[Any]

## At random selection methods
    
def fitness_proportionate_selection(population:List[Vector],
                                    fitness:Callable = None,
                                    fit:List[Any] = None
)->Vector:
    
    """
    Perform fitness proportionate selection on a population.

    Parameters:
    - population: The list of vectors representing the population.
    - fitness: A function to calculate the fitness value for a vector (default is None).
    - fit: The list of fitness values corresponding to the vectors (default is None).

    Returns:
    Vector: The selected vector based on fitness proportionate selection.

    Example:
    population_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    fitness_values = [calculate_fitness(v) for v in population_list]
    selected_vector = fitness_proportionate_selection(population_list, calculate_fitness, fitness_values)
    print(selected_vector)
    """

    if not fit: fit = [fitness(p) for p in population]
    if all(i == 0.0 for i in fit):
        fit = [1 for _ in range(len(fit))]
    fit = fit[0] + [sum(fit[:i]) for i in range(1,len(fit))]
    return population[random.randint(0,len(fit)-1)]

def stochasting_universal_sampling(populiation:List[Vector],
                                   fitness:Callable = None,
                                   fit:List[Any] = None
)-> Vector:

    """
    Perform stochastic universal sampling on a population.

    Parameters:
    - population: The list of vectors representing the population.
    - fitness: A function to calculate the fitness value for a vector (default is None).
    - fit: The list of fitness values corresponding to the vectors (default is None).

    Returns:
    Vector: The selected vector based on stochastic universal sampling.

    Example:
        population_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        fitness_values = [calculate_fitness(v) for v in population_list]
        selected_vector = stochasting_universal_sampling(population_list, calculate_fitness, fitness_values)
        print(selected_vector)
    """

    index = 0
    if not fit: fit = [fitness(p) for p in populiation]
    if all(i == 0.0 for i in fit): fit = [1.0 for _ in range(len(fit))]
    fit = fit[0] + [sum(fit[:i]) for i in range(1,len(fit))]
    value = random.randrange(0,fit[-1])
    while fit[index] < value: index += 1
    return populiation[index]


## Non random Selection methods

def tournament_selection(population:List[Vector],
                         fitness:Callable,
                         t:int = 2
)-> Vector:
    """
    Perform tournament selection on a population.

    Parameters:
    - population: The list of vectors representing the population.
    - t: The tournament size (number of participants, default is 2).
    - fitness: A function to calculate the fitness value for a vector.

    Returns:
    Vector: The selected vector based on tournament selection.

    Example:
        population_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        selected_vector = tournament_selection(population_list, calculate_fitness, 2)
        print(selected_vector)
    """

    best:Vector = None
    for _ in range(t):
        next_candidate = population[random.randint(0,len(population)-1)]
        if not best or fitness(next_candidate) > fitness(best):
            best = next_candidate
    return best

def tournament_selection_with_extraction(population:List[Vector],
                                         fitness:Callable,
                                         t:int = 2
)->Vector:
    
    """
    Perform tournament selection on a population with extraction.

    Parameters:
    - population: The list of vectors representing the population.
    - fitness: A function to calculate the fitness value for a vector.
    - t: The tournament size (number of participants, default is 2).

    Returns:
    Vector: The selected vector based on tournament selection.

    Example:
        population_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        selected_vector = tournament_selection_with_extraction(population_list, calculate_fitness, 2)
        print(selected_vector)
    """

    best:Vector = None
    for _ in range(t):
        next_candidate = population.pop(random.randint(0,len(population)-1))
        if not best or fitness(next_candidate) > fitness(best):
            best = next_candidate
    return best


def pareto_dominance_binary_tournament_selection(population:List[Vector],
                                                 objectives:List[Callable]
)-> Vector:
    
    """
    Perform binary tournament selection based on Pareto dominance.

    Parameters:
    - population: The list of vectors representing the population.
    - objectives: A list of objective functions to evaluate the solutions.

    Returns:
    Vector: The selected vector based on binary tournament selection.

    Example:
    selected_vector = pareto_dominance_binary_tournament_selection(population_list, [objective_function_1, objective_function_2])
    print(selected_vector)
    """

    a = population.pop(random.randint(0,len(population)-1))
    b = population.pop(random.randint(0,len(population)-1))
    if p_d(a,b,objectives):
        return a
    elif p_d(a,b,objectives):
        return b
    else: return (a,b)[random.randint(0,1)]

