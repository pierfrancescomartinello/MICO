from typing import Any, Callable, Set

if __name__ == "__main__":
    Vector = Set[Any]

"""Evolution Strategies"""
def mu_and_lambda(mu:int,
                  lambd:int,
                  time:int,
                  fitness:Callable,
                  assess_fitness:Callable,
                  random_el:Callable,
                  isIdeal:Callable,
                  mutate:Callable,
                  P:Vector = None
)-> Any:
    
    """
    Mu and Lambda Evolutionary Algorithm.

    Parameters:
    - mu (int): The number of parents.
    - lambd (int): The number of offspring.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - fitness (Callable): A function to evaluate the fitness of an individual.
    - assess_fitness (Callable): A function to assess the fitness of the population.
    - random_el (Callable): A function to generate a random individual.
    - isIdeal (Callable): A function that checks if a solution is ideal.
    - mutate (Callable): A function to perform mutation on an individual.
    - P (Vector, optional): The initial population (default is None).

    Returns:
    Any: The best individual found by the Mu and Lambda evolutionary algorithm.

    Example:
    
        result = mu_and_lambda(mu=5,
                               lambd=20,
                               time=100,
                               fitness=individual_fitness,
                               assess_fitness=assess_fitness,
                               random_el=random_element,
                               isIdeal=is_ideal_solution,
                               mutate=mutate_individual)
    
    """

    best = None
    if P == None:
        for _ in range(1, lambd): P.append(random_el())
    while not isIdeal(best) and time >0:
        fitted_P = assess_fitness(P)
        if best == None: best = P[0]
        for i in fitted_P:
            if fitness(i[0]) > fitness(best): best = i[0]
        Q = [i[0] for i in fitted_P[:lambd]]
        P = list()
        for q in Q:
            for _ in range(1, int(lambd/mu)): P.append(mutate(q))
        time > 0
    return best

def mu_plus_lambda(mu:int, 
                   lambd:int, 
                   time:int, 
                   fitness:Callable, 
                   assess_fitness:Callable,
                   random_el:Callable,
                   isIdeal:Callable,
                   mutate:Callable,
                   P:Vector = None
)->Any:
    
    """
    Mu Plus Lambda Evolutionary Algorithm.

    Parameters:
    - mu (int): The number of parents.
    - lambd (int): The number of offspring.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - fitness (Callable): A function to evaluate the fitness of an individual.
    - assess_fitness (Callable): A function to assess the fitness of the population.
    - random_el (Callable): A function to generate a random individual.
    - isIdeal (Callable): A function that checks if a solution is ideal.
    - mutate (Callable): A function to perform mutation on an individual.
    - P (Vector, optional): The initial population (default is None).

    Returns:
    Any: The best individual found by the Mu Plus Lambda evolutionary algorithm.

    Example:

        result = mu_plus_lambda(mu=5,
                                lambd=20,
                                time=100,
                                fitness=individual_fitness,
                                assess_fitness=assess_fitness,
                                random_el=random_element,
                                isIdeal=is_ideal_solution,
                                mutate=mutate_individual)
    
    """

    best = None
    if P == None:
        for _ in range(1,lambd): P.append(random_el())
    while not isIdeal(best) and time >0:
        fitted_P = assess_fitness(P)
        if best == None: best = P[0]
        for i in fitted_P:
            if fitness(i[0]) > fitness(best): best = i[0]
        Q = [i[0] for i in fitted_P[:lambd]]
        P = Q
        for q in Q:
            for _ in range(1, int(lambd/mu)):
                P.append(mutate(Q))
        time -= 1
    return best