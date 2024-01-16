from typing import Any, Callable, List, bool
import queue
import random


def random_vector(len:int,
                  max:int | Any,
                  min:int | Any
)-> Any:
    
    """
    Generate a random vector.

    Parameters:
    - len (int): The length of the vector.
    - max (int or Any): The maximum value for each element of the vector.
    - min (int or Any): The minimum value for each element of the vector.

    Returns:
    Any: A random vector.
    """

    if len == 1 and type(max) == int and type(min) == int:
        return random.randrange(max, min)
    else:
        return [random.randrange(min[i], max[i]) for i in range(len)]

def bit_flip(p:float,
             V:Any):
    
    """
    Apply bit-flip mutation to a binary vector.

    Parameters:
    - p (float): The probability of flipping each bit.
    - v (Any): The binary vector.

    Returns:
    Any: The mutated binary vector.
    """

    return [not i if p > random.random() else i for i in V]

def NewHomeBase(S:Any,
                W:Any,
                quality:Callable
)->Any:
    
    """
    Update the home base by choosing the state with higher quality.

    Parameters:
    - S (Any): The current home base state.
    - W (Any): The potential new home base state.
    - quality (Callable): A function that evaluates the quality of a state.

    Returns:
    Any: The updated home base state.
    """

    return S if quality(S)>=quality(W) else W

def random_bit_vector(len:int
)-> List[bool]:
    
    """
    Generate a random binary vector.

    Parameters:
    - len (int): The length of the binary vector.

    Returns:
    List[bool]: A random binary vector.
    """

    return [random.random() > 0.5 for _ in range(len)]

def pareto_dominance(A:Any,
                     B:Any,
                     objectives:List[Callable]
)-> bool:
    
    """
    Check if solution A Pareto dominates solution B.

    Parameters:
    - A: The first solution.
    - B: The second solution.
    - objectives: A list of objective functions to evaluate the solutions.

    Returns:
    bool: True if A dominates B, False otherwise.

    Example:
    is_dominant = pareto_dominance(solution_A, solution_B, [objective_function_1, objective_function_2])
    print(is_dominant)
    """

    for o in objectives:
        if o(A) < o(B): return False
    return True


def pareto_non_dominated_front(objectives:List[Callable],
                               subpop:List[Any]
)-> List[Any]:
    
    """
    Identify the Pareto non-dominated front in a population.

    Parameters:
    - objectives: A list of objective functions to evaluate the solutions.
    - subpop: The subpopulation for which to find the non-dominated front.

    Returns:
    List[Any]: The non-dominated front.

    Example:
    non_dominated_front = pareto_non_dominated_front([objective_function_1, objective_function_2], population)
    print(non_dominated_front)
    """

    F = List()
    for s in subpop:
        F.append(s)
        for f in F:
            if f ==s:continue
            else:
                if pareto_dominance(s, f, objectives): F.remove(f)
                else: 
                    F.remove(s)
                    continue
    return F



class IterableQueue(queue.Queue):

    """
    An iterable queue that supports the `in` operator for checking the presence of an item.

    This class extends the functionality of the standard `queue.Queue` by adding the `__contains__` method,
    allowing users to check whether an item is present in the queue using the `in` operator.

    Methods:
    - __contains__(item): Check if the item is present in the queue.

    Inherited Methods from queue.Queue:
    - put(item): Put an item into the queue.
    - get(): Remove and return an item from the queue.
    - empty(): Return True if the queue is empty, False otherwise.
    - qsize(): Return the approximate size of the queue.

    Attributes:
    - mutex: A lock to synchronize access to the queue.

    Example:
        my_queue = IterableQueue()
        my_queue.put(1)
        my_queue.put(2)
        print(1 in my_queue)  # Output: True
        print(3 in my_queue)  # Output: False
    
    """

    def __contains__(self, item):
        with self.mutex:
            return item in self.queue
pass


