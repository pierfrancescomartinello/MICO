from typing import Any, Callable, Set, Tuple, List
import random

if __name__ == "__main__":
    Vector = Set[Any]

def genetic_algorithm(population_size:int,
                      random_el:Callable,
                      time:int,
                      assess_fitness:Callable,
                      fitness:Callable,
                      isIdeal:Callable,
                      select_with_replacement:Callable,
                      mutate:Callable,
                      crossover:Callable,
                      P:Vector = None,
        
)->Any:
    
    """
    Genetic Algorithm.

    Parameters:
    - population_size (int): The size of the population.
    - random_el (Callable): A function to generate a random individual.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - assess_fitness (Callable): A function to assess the fitness of the population.
    - fitness (Callable): A function to evaluate the fitness of an individual.
    - isIdeal (Callable): A function that checks if a solution is ideal.
    - select_with_replacement (Callable): A function to select individuals from the population with replacement.
    - mutate (Callable): A function to perform mutation on an individual.
    - crossover (Callable): A function to perform crossover between two individuals.
    - P (Vector, optional): The initial population (default is None).

    Returns:
    Any: The best individual found by the genetic algorithm.

    Example:
    
        result = genetic_algorithm(population_size=100,
                                   random_el=random_element,
                                   time=100,
                                   assess_fitness=assess_fitness,
                                   fitness=individual_fitness,
                                   isIdeal=is_ideal_solution,
                                   select_with_replacement=select_individual_with_replacement,
                                   mutate=mutate_individual,
                                   crossover=crossover_individuals)
    
    """

    best = None
    if P == None:
        for _ in range(1, population_size): P.append(random_el())
    while not isIdeal(best) and time >0:
        fitted_P = assess_fitness(P)
        if best == None: best = P[0]
        for i in fitted_P:
            if fitness(i[0]) > fitness(best): best = i[0]
        Q = list()
        for _ in range(1,(population_size//2)):
            p_a = select_with_replacement(P)
            p_b = select_with_replacement(P)
            c_a, c_b = crossover(p_a,p_b)
            Q.append(mutate(c_a))
            Q.append(mutate(c_b))
        P = Q
        time -= 1
    return best


