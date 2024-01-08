from typing import Any, Callable
import math
from Newer.miscellaneous.miscellaneous import IterableQueue

"""Single State Methods"""

def hill_climbing(S:Any,
                  tweak:Callable,
                  quality:Callable,
                  time:Any,
                  isIdeal:Callable
) -> Any:
    
    """
    Hill Climbing Algorithm.

    Parameters:
    - S (Any): The initial state.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - time (Any): The maximum number of iterations or time limit for the algorithm.
    - isIdeal (Callable): A function that checks if a state is ideal.

    Returns:
    Any: The best state found by the hill climbing algorithm.
    """
        
    while not isIdeal(S) or time > 0:
        R = tweak(S)
        if quality(R) > quality(S): S = R
        time -=1
    return S

def steepest_hill_climbing(S:Any,
                           tweak:Callable,
                           quality:Callable, 
                           isIdeal:Callable, 
                           time:int, 
                           n:int

)-> Any:
    
    """
    Steepest Hill Climbing Algorithm.

    Parameters:
    - S (Any): The initial state.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - n (int): The number of iterations for steepest ascent.

    Returns:
    Any: The best state found by the steepest hill climbing algorithm.
    """
    while not isIdeal(S) and time > 0:
        R = tweak(S)
        for _ in range(1,n):
            W = tweak(S)
            if quality(W) > quality(R): R = W
            pass
        if quality(R) > quality(S): S = R
        time -= 1
    return S

def steepest_hill_falling(S:Any, 
                          tweak:Callable, 
                          quality:Callable, 
                          isIdeal:Callable, 
                          time:int, 
                          n:int
)-> Any:
    
    """
    Steepest Hill Falling Algorithm.

    Parameters:
    - S (Any): The initial state.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - n (int): The number of iterations for steepest descent.

    Returns:
    Any: The best state found by the steepest hill falling algorithm.
    """
    while not isIdeal(S) and time > 0:
        R = tweak(S)
        for _ in range(1,n):
            W = tweak(S)
            if quality(W) < quality(R): R = W
        if quality(R) < quality(S): S = R
        time -= 1   
    return S

def steepest_hill_climbing_with_replacement(S:Any, 
                                            tweak:Callable,
                                            quality:Callable,
                                            isIdeal:Callable,
                                            time:int,
                                            n:int

)-> Any:
    """
    Steepest Hill Climbing Algorithm with Replacement.

    Parameters:
    - S (Any): The initial state.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - n (int): The number of iterations for steepest ascent.

    Returns:
    Any: The best state found by the steepest hill climbing algorithm with replacement.
    """
    best = S
    while not isIdeal(best) and time > 0:
        R = tweak(S)
        for _ in range(1,n):
            W = tweak(S)
            if quality(W) > quality(R): R = W
        S = R
        if quality(S) > quality(best): best = S
        time -= 1
    return best

def steepest_hill_falling_with_replacement(S:Any,
                                           tweak:Callable,
                                           quality:Callable,
                                           isIdeal:Callable, 
                                           time:int, 
                                           n:int

)-> Any:
    
    """
    Steepest Hill Falling Algorithm with Replacement.

    Parameters:
    - S (Any): The initial state.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - n (int): The number of iterations for steepest descent.

    Returns:
    Any: The best state found by the steepest hill falling algorithm with replacement.
    """

    best = S
    while not isIdeal(best) and time > 0:
        R = tweak(S)
        for _ in range(1,n):
            W = tweak(S)
            if quality(W) < quality(R): R = W
        S = R
        if quality(S) < quality(best): best = S
        time -= 1
    return best

def random_search(S:Any,
                  time:int,
                  quality:Callable,
                  rand_gen:Callable,
                  isIdeal:Callable
)-> Any:
    
    """
    Random Search Algorithm.

    Parameters:
    - S (Any): The initial state.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - quality (Callable): A function that evaluates the quality of a state.
    - rand_gen (Callable): A function that generates a random state.
    - isIdeal (Callable): A function that checks if a state is ideal.

    Returns:
    Any: The best state found by the random search algorithm.
    """

    best = S
    while not isIdeal(best) and time > 0:
        S = rand_gen()
        if quality(S) > quality(best): best = S
        time -=1
    return best

def hill_climbing_with_random_restarts(distribution:callable,
                                       S:Any,
                                       time:int,
                                       tweak:Callable,
                                       quality:Callable,
                                       rand_gen:Callable,
                                       isIdeal:Callable
)-> Any:
    """
    Hill Climbing Algorithm with Random Restarts.

    Parameters:
    - distribution (Callable): A function that generates values for random restarts.
    - S (Any): The initial state.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - rand_gen (Callable): A function that generates a random state.
    - isIdeal (Callable): A function that checks if a state is ideal.

    Returns:
    Any: The best state found by the hill climbing algorithm with random restarts.
    """
    best = S
    while not isIdeal(best) and time > 0:
        t = distribution()
        while not isIdeal(S) and time >0  and t>0:
            R = tweak(S)
            if quality(R) > quality(S): S = R
        if quality(S) > quality(best): best = S 
        S = rand_gen()
        time-=1
    return best


def simulated_annealing(S:Any,
                        t:int,
                        time:int,
                        tweak:Callable,
                        quality:Callable,
                        P:Callable,
                        decreasing:Callable,
                        isIdeal:Callable,
                        reheatability:bool = False,
                        reheating:Callable = None,
)-> Any:
    
    """
    Simulated Annealing Algorithm.

    Parameters:
    - S (Any): The initial state.
    - t (int): Initial temperature.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - P (Callable): A function to calculate the acceptance probability.
    - decreasing (Callable): A function to decrease the temperature.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - reheatability (bool): Whether to use reheating (default is False).
    - reheating (Callable): A function to adjust the temperature during reheating.

    Returns:
    Any: The best state found by the simulated annealing algorithm.
    """

    original_t = t
    best = S
    while not isIdeal(best) and time >0 and t>0:
        R = tweak(S)
        if quality(R)> quality(S) or P() >= math.e**((quality(R)-quality(S))/t): S= R
        if reheatability: t = reheating(original_t, t)
        else: t = decreasing(t)
        if quality(S) > quality(best): best = S
        time-=1
    return best

def taboo_search(l:int,
                 n:int,
                 S:Any,
                 tweak:Callable,
                 quality:Callable,
                 isIdeal:Callable,
                 time:int
)-> Any:
    
    """
    Taboo Search Algorithm.

    Parameters:
    - l (int): Size of the taboo list.
    - n (int): Number of iterations for each step.
    - S (Any): The initial state.
    - tweak (Callable): A function that tweaks the current state.
    - quality (Callable): A function that evaluates the quality of a state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - time (int): The maximum number of iterations or time limit for the algorithm.

    Returns:
    Any: The best state found by the taboo search algorithm.
    """

    best = S
    L = IterableQueue(l)
    L.put(S)
    while not isIdeal(best) and time >0:
        R = tweak(S)
        for _ in range(1,n):
            W = tweak(S)
            if W not in L and (quality(W)>quality(R) or R in L): R=W
        if R not in L: 
            S = R
            L.put(R)
        if quality(S) > quality(best): best = S
    return best


def feature_based_taboo_search(l:int,
                               n:int,
                               S:Any,
                               tweak:Callable,
                               quality:Callable,
                               isIdeal:Callable,
                               time:int
)->Any:
    
    """
    Feature-Based Taboo Search Algorithm.

    Parameters:
    - l (int): Size of the taboo list.
    - n (int): Number of iterations for each step.
    - S (Any): The initial state.
    - tweak (Callable): A function that tweaks the current state and returns the state and the step.
    - quality (Callable): A function that evaluates the quality of a state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - time (int): The maximum number of iterations or time limit for the algorithm.

    Returns:
    Any: The best state found by the feature-based taboo search algorithm.
    """

    best = S
    L = IterableQueue()
    while not isIdeal(best) and time > 0:
        R, step_R = tweak(S, L)
        for _ in range(1,n):
            W, step_W = tweak(S, L)
            if quality(W) > quality(R): R, step_R = W, step_W
        S = R
        L.put(step_R)
        if quality(S) > quality(best): best = S
        time -=1
    return best

def ILS(S: Any,
        time: int,
        quality: Callable,
        tweak: Callable,
        isIdeal: Callable,
        perturb: Callable,
        NHB: Callable
) -> Any:
    """
    Iterated Local Search (ILS) Algorithm.

    Parameters:
    - S (Any): The initial state.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - quality (Callable): A function that evaluates the quality of a state.
    - tweak (Callable): A function that tweaks the current state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - perturb (Callable): A function that perturbs the current state.
    - NHB (Callable): A function that generates a new starting point for the next iteration.

    Returns:
    Any: The best state found by the ILS algorithm.
    """
    best = S
    while not isIdeal(best) and time > 0:
        R = tweak(S)
        S_perturbed = perturb(R)
        R = NHB(S, S_perturbed)
        
        if quality(R) > quality(best):
            best = R
        
        S = R
        time -= 1
    
    return best


def ILS_with_Random_Restarts(distribution:Callable,
                             S:Any,
                             time:int,
                             quality:Callable,
                             tweak:Callable,
                             isIdeal:Callable,
                             perturb:Callable,
                             NHB:Callable
)-> Any:
    
    """
    Iterated Local Search (ILS) Algorithm with Random Restarts.

    Parameters:
    - distribution (Callable): A function that generates values for random restarts.
    - S (Any): The initial state.
    - time (int): The maximum number of iterations or time limit for the algorithm.
    - quality (Callable): A function that evaluates the quality of a state.
    - tweak (Callable): A function that tweaks the current state.
    - isIdeal (Callable): A function that checks if a state is ideal.
    - perturb (Callable): A function that perturbs the current state.
    - NHB (Callable): A function that generates a new starting point for the next iteration.

    Returns:
    Any: The best state found by the ILS algorithm with random restarts.
    """

    H = S
    best = S
    while not isIdeal(best) and time >0:
        t = distribution()
        while isIdeal(S) and t >0 and time >0:
            R = tweak(S)
            if quality(R) > quality(S): S = R
            t -= 1
        if quality(S) > quality(best): best = S
        H = NHB(H,S)
        S = perturb(H)
        time -= 1
    pass