from typing import Any, Callable, Set, Tuple, List
import random
from miscellaneous.recombination import line_recombination

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
            if i[1] > fitness(best): best = i[0]
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


def genetic_algorithm_with_elitism(population_size:int,
                                   n:int,
                                   random_el:Callable,
                                   assess_fitness:Callable,
                                   fitness:Callable,
                                   isIdeal:Callable,
                                   time:int,
                                   select_with_replacement:Callable,
                                   crossover:Callable,
                                   mutate:Callable
)-> Any:
    
    """
    Perform a genetic algorithm with elitism.

    Parameters:
    - population_size: The size of the population.
    - n: The number of individuals to select for elitism.
    - random_el: A function to generate a random individual.
    - assess_fitness: A function to assess the fitness of the population.
    - fitness: A function to calculate the fitness value for an individual.
    - isIdeal: A function to check if an individual is ideal.
    - time: The maximum number of iterations or time limit for the algorithm.
    - select_with_replacement: A function for selecting individuals with replacement.
    - crossover: A function for crossover operation.
    - mutate: A function for mutation operation.

    Returns:
    Any: The best individual found by the genetic algorithm with elitism.

    Example:
        best_individual = genetic_algorithm_with_elitism(100, 10, generate_random_individual,
                                                        assess_fitness_function, calculate_fitness,
                                                        is_ideal_function, 50, select_with_replacement_function,
                                                        crossover_function, mutate_function)
        print(best_individual)
    """

    P:Vector = None
    best:Any = None
    for _ in population_size: P.append(random_el)
    while not isIdeal(best) and time>0:
        fitted_P = sorted(assess_fitness(P),key = lambda x: x[1])
        for i in fitted_P:
            if not best or i[1] > fitness(best): best = i[0]
        Q = [i[0] for i in fitted_P[:n]]
        P = fitted_P[n:]
        for _ in range(int(population_size-n)/2):
            p_a = select_with_replacement(P)
            p_b = select_with_replacement(P)
            c_a, c_b = crossover(p_a,p_b)
            Q.append(mutate(c_a))
            Q.append(mutate(c_b))
        P = Q
        time -= 1
    return best


def steady_state_genetic_algorithm(population_size:int,
                                   time:int,
                                   assess_fitness:Callable,
                                   fitness:Callable,
                                   random_el:Callable,
                                   select_with_replacement:Callable,
                                   crossover:Callable,
                                   mutate:Callable,
                                   isIdeal:Callable,
                                   select_for_death:Callable
)-> Any:
    
    """
    Perform a steady-state genetic algorithm.

    Parameters:
    - population_size: The size of the population.
    - time: The maximum number of iterations or time limit for the algorithm.
    - assess_fitness: A function to assess the fitness of the population.
    - fitness: A function to calculate the fitness value for an individual.
    - random_el: A function to generate a random individual.
    - select_with_replacement: A function for selecting individuals with replacement.
    - crossover: A function for crossover operation.
    - mutate: A function for mutation operation.
    - isIdeal: A function to check if an individual is ideal.
    - select_for_death: A function for selecting individuals for removal.

    Returns:
    Any: The best individual found by the steady-state genetic algorithm.

    Example:
        best_individual = steady_state_genetic_algorithm(100, 50, assess_fitness_function, calculate_fitness,
                                                        generate_random_individual, select_with_replacement_function,
                                                        crossover_function, mutate_function, is_ideal_function,
                                                        select_for_death_function)
        print(best_individual)
    """

    P:Vector = None
    best:Any = None
    for _ in population_size: P.append(random_el)
    fitted_P = sorted(assess_fitness(P), key = lambda x:x[1])
    for i in fitted_P:
        if not best or i[1] > fitness(best):best = i[0]
    while not isIdeal(best) and time >0:
        p_a = select_with_replacement(P)
        p_b = select_with_replacement(P)
        c_a, c_b = crossover(p_a, p_b)
        c_a = mutate(c_a)
        c_b = mutate(c_b)
        if fitness(c_a) > fitness(best): best = c_a
        if fitness(c_b) > fitness(best): best = c_b
        p_d = select_for_death(P)
        p_e = select_for_death(P)
        P.remove(p_d)
        P.remove(p_e)
        P.add(c_a)
        P.add(c_b)

        time -= 1
    return best


def tree_style_genetic_algorithm(population_size:int,
                                 time:int,
                                 r:float,
                                 random_el:Callable,
                                 assess_fitness:Callable,
                                 fitness:Callable,
                                 select_with_replacement:Callable,
                                 crossover:Callable,
                                 isIdeal:Callable
)-> Any:
    
    """
    Perform a tree-style genetic algorithm.

    Parameters:
    - population_size: The size of the population.
    - time: The maximum number of iterations or time limit for the algorithm.
    - r: The probability of selecting an individual without crossover.
    - random_el: A function to generate a random individual.
    - assess_fitness: A function to assess the fitness of the population.
    - fitness: A function to calculate the fitness value for an individual.
    - select_with_replacement: A function for selecting individuals with replacement.
    - crossover: A function for crossover operation.
    - isIdeal: A function to check if an individual is ideal.

    Returns:
    Any: The best individual found by the tree-style genetic algorithm.

    Example:
        best_individual = tree_style_genetic_algorithm(100, 50, 0.3, generate_random_individual,
                                                       assess_fitness_function, calculate_fitness,
                                                       select_with_replacement_function, crossover_function,
                                                       is_ideal_function)
        print(best_individual)
    """

    P:Vector = None
    best:Any = None
    for _ in range(population_size): P.append(random_el())
    fitted_P = sorted(assess_fitness(P), key = lambda x :x[1])
    
    while not isIdeal(best) and time > 0:
        for i in fitted_P:
            if not best or i[1] > fitness(best):best = i[0]
        Q = List()
        while len(Q) < population_size:
            if r >= random.random():
                p_i = select_with_replacement(P)
                Q.append(p_i)
            else:
                p_a = select_with_replacement(P)
                p_b = select_with_replacement(P)
                c_a, c_b = crossover(p_a, p_b)
                Q.append(c_a)
                if len(Q) < population_size: Q.append(c_b)
        P = Q
        time -= 1
    return best


def scatter_search_with_path_relinking(seeds:Vector,
                                       init_size:int,
                                       hill_climb_time:int,
                                       fitness_based_cut:int,
                                       diversity_based_cut:int,
                                       time:int,
                                       hill_climb:Callable,
                                       assess_fitness:Callable,
                                       assess_diversity:Callable,
                                       fitness:Callable,
                                       mutate:Callable,
                                       different_element:Callable,
                                       isIdeal:Callable,
                                       crossover:Callable = line_recombination()

)->Any:
    
    """
    Perform scatter search with path relinking.

    Parameters:
    - seeds: The initial set of solutions (seeds).
    - init_size: The initial size of the population.
    - hill_climb_time: The number of iterations for hill climbing.
    - fitness_based_cut: The number of solutions to include in the population based on fitness.
    - diversity_based_cut: The number of solutions to include in the population based on diversity.
    - time: The maximum number of iterations or time limit for the algorithm.
    - hill_climb: The hill climbing function.
    - assess_fitness: A function to assess the fitness of the population.
    - assess_diversity: A function to assess the diversity of the population.
    - fitness: A function to calculate the fitness value for a solution.
    - mutate: A function for mutation.
    - different_element: A function to generate a different element.
    - isIdeal: A function to check if a solution is ideal.
    - crossover: The crossover function.

    Returns:
    Any: The best solution found by the scatter search with path relinking.

    Example:
        best_solution = scatter_search_with_path_relinking(seeds, 20, 10, 5, 5, 50, hill_climb_function,
                                                           assess_fitness_function, assess_diversity_function,
                                                           calculate_fitness, mutate_function, generate_different_element,
                                                           is_ideal_function, line_recombination)
        print(best_solution)
    """

    Q:Vector = None
    P = seeds
    for _ in range(init_size - len(seeds)): P.append(different_element(P))
    best:Any = None
    for p in P:
        for _ in range(hill_climb_time): p  = hill_climb(p)
        if not best or fitness(p) > fitness(best): best = p
        while not isIdeal(best) and time > 0:
            B = sorted(assess_fitness(P), key= lambda x:x[1])[:fitness_based_cut]
            D = sorted(assess_diversity(P), key= lambda x :x[1])[:diversity_based_cut]
            P = P + B + D
            for i, p_i in enumerate(P):
                for j, p_j in enumerate(P):
                    if i == j: continue
                    else:
                        c_a = mutate(c_a)
                        c_b = mutate(c_b)
                        for _ in range(hill_climb_time): c_a = hill_climb(c_a)
                        for _ in range(hill_climb_time): c_b = hill_climb(c_b)
                        c_a, c_b = crossover(p_i,p_j)
                        if fitness(c_a) > fitness(best): best = c_a
                        if fitness(c_b) > fitness(best): best = c_b
                        Q.append(c_a)
                        Q.append(c_b)
            P = P + Q
            time -= 1
    return best


def differential_evolution(alpha:float,
                           population_size:int,
                           time:int,
                           random_el:Callable,
                           assess_fitness:Callable,
                           fitness:Callable,
                           isIdeal:Callable,
                           crossover:Callable,
                           sum:Callable,
                           dif:Callable,
                           mul:Callable
        
)-> Any:
    
    """
    Perform scatter search with path relinking.

    Parameters:
    - seeds: The initial set of solutions (seeds).
    - init_size: The initial size of the population.
    - hill_climb_time: The number of iterations for hill climbing.
    - fitness_based_cut: The number of solutions to include in the population based on fitness.
    - diversity_based_cut: The number of solutions to include in the population based on diversity.
    - time: The maximum number of iterations or time limit for the algorithm.
    - hill_climb: The hill climbing function.
    - assess_fitness: A function to assess the fitness of the population.
    - assess_diversity: A function to assess the diversity of the population.
    - fitness: A function to calculate the fitness value for a solution.
    - mutate: A function for mutation.
    - different_element: A function to generate a different element.
    - isIdeal: A function to check if a solution is ideal.
    - crossover: The crossover function.

    Returns:
    Any: The best solution found by the scatter search with path relinking.

    Example:
        best_solution = scatter_search_with_path_relinking(seeds, 20, 10, 5, 5, 50, hill_climb_function,
                                                           assess_fitness_function, assess_diversity_function,
                                                           calculate_fitness, mutate_function, generate_different_element,
                                                           is_ideal_function, line_recombination)
        print(best_solution)
    """

    P:Vector = None
    Q:Any = None
    best:Any = None
    for _ in range(population_size): P.append(random_el())
    while not isIdeal(best) and time > 0:
        for i,p in enumerate(P):
            if Q and fitness(Q[i]) > fitness(p): p = Q[i]
            if not best or fitness(p) > fitness(best): best = P
        Q = P
        for i, q in enumerate(Q):
            list = [j  if j != i else None for j in range(len(Q) -1)]
            a = Q[index_a := list[random.randrange(0,len(list) - 1)]]
            list.pop(index_a)
            b = Q[index_b := list[random.randrange(0,len(list) - 1)]]
            list.pop(index_b)
            c = Q[list[random.randrange(0,len(list) - 1)]]
            d = sum(a, mul(alpha, dif(b, c)))
            p = crossover(d, q)[0]
        time -= 1
    return best


def particle_swarm_optimization(swarm_size:int,
                                number_of_informants:int,
                                time:int,
                                alpha:float,    
                                beta:float,     
                                gamma:float,
                                delta:float,
                                epsilon:float,
                                random_particle:Callable,
                                return_fittest:Callable,
                                fitness:Callable,
                                isIdeal:Callable,
                                mul:Callable,
                                sum:Callable,
)-> Vector:
    
    """
    Perform particle swarm optimization.

    Parameters:
    - swarm_size: The size of the particle swarm.
    - number_of_informants: The number of informants for each particle.
    - time: The maximum number of iterations or time limit for the algorithm.
    - alpha: Proportion of velocity.
    - beta: Proportion of personal best.
    - gamma: Proportion of informants' best.
    - delta: Proportion of global best.
    - epsilon: Jump size of a particle.
    - random_particle: A function to generate a random particle.
    - return_fittest: A function to return the fittest among a list of particles.
    - fitness: A function to calculate the fitness value for a particle.
    - isIdeal: A function to check if a solution is ideal.
    - mul: A function to perform multiplication.
    - sum: A function to perform addition.

    Returns:
    Vector: The best solution found by the particle swarm optimization.

    Example:
        best_solution = particle_swarm_optimization(50, 5, 100, 0.5, 0.3, 0.2, 0.1, 0.01,
                                                   random_particle_function, assess_fitness_function,
                                                   return_fittest_function, calculate_fitness_function,
                                                   is_ideal_function, multiplication_function, addition_function)
        print(best_solution)
    """

    P: List(Tuple[Any, Vector, Vector]) = None # P will have the element, any know location it has visited and its current velocity
    best:Vector = None
    for _ in range(swarm_size): P.append(random_particle())
    while not isIdeal(best) and time>0:
        for p in P:
            if not best or fitness(p[0]) > fitness(best): best = p[0]
        for p in P:
            x_personal = return_fittest(p[1])
            x_informants = return_fittest([i[1] for i in random.sample(P, number_of_informants)])
            x_global = return_fittest([p[1] for p in P])
            for i, v_i in enumerate(p[2]):
                b = random.randrange(0, beta)
                c = random.randrange(0, gamma)
                d = random.randrange(0, delta)
                v_i = alpha*v_i + b*(x_personal - (p[0])[i]) + c*(x_informants - (p[0])[i]) + d*(x_global +(p[0])[i])
            p[1].append(p[0])
            p[0] = sum(p[0], mul(epsilon, p[3]))
        time -= 1
    return best


