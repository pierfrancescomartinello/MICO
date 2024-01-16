from typing import Any, Callable, Set, Tuple, List
import random

if __name__ == "__main__":
    Vector = Set[Any]


def line_recombination(V:Vector,
                       W:Vector,
                       mul:Callable,
                       sum:Callable,
                       check_on_deviation:Callable,
                       deviation:float= 0.25
)-> Tuple[Vector,Vector]:
    
    """
    Perform line recombination on two vectors.

    Parameters:
    - V: The first input vector.
    - W: The second input vector.
    - mul: A function for element-wise multiplication.
    - sum: A function for element-wise addition.
    - check_on_deviation: A function to check deviation between vectors.
    - deviation: Deviation parameter (default is 0.25).

    Returns:
    Tuple[Vector, Vector]: The resulting vectors after line recombination.

    Example:
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        result_vector1, result_vector2 = line_recombination(vector1, vector2, multiplication, addition, deviation_check)
        print(result_vector1, result_vector2)
    """

    alpha, beta = random.randrange(-deviation, 1+deviation), random.randrange(-deviation, 1+deviation)
    t:Vector = None
    s:Vector = None
    for i in len(V):
        t = sum(mul(alpha,V[i]), mul(1+alpha, W[i]))
        s = sum(mul(beta,W[i]), mul(1+beta, V[i]))
        if check_on_deviation(t,s):
            V[i] = t
            W[i] = s
    return V,W


def intermediate_recombination(V:Vector,
                               W:Vector,
                               mul:Callable,
                               sum:Callable,
                               check_on_deviation:Callable,
                               deviation:float= 0.25
)-> Tuple[Vector,Vector]:
    
    """
    Perform intermediate recombination on two vectors.

    Parameters:
    - V: The first input vector.
    - W: The second input vector.
    - mul: A function for element-wise multiplication.
    - sum: A function for element-wise addition.
    - check_on_deviation: A function to check deviation between vectors.
    - deviation: Deviation parameter (default is 0.25).

    Returns:
    Tuple[Vector, Vector]: The resulting vectors after intermediate recombination.

    Example:
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        result_vector1, result_vector2 = intermediate_recombination(vector1, vector2, multiplication, addition, deviation_check)
        print(result_vector1, result_vector2)
    """


    alpha, beta = random.randrange(-deviation, 1+deviation), random.randrange(-deviation, 1+deviation)
    t:Vector = None
    s:Vector = None
    for i in len(V):
        alpha, beta = random.randrange(-deviation, 1+deviation), random.randrange(-deviation, 1+deviation)
        t:Vector = None
        s:Vector = None 
        while not check_on_deviation(t,s):
            t = sum(mul(alpha,V[i]), mul(1+alpha, W[i]))
            s = sum(mul(beta,W[i]), mul(1+beta, V[i]))
        V[i] = t
        W[i] = s
    return V,W

