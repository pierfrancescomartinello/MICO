from typing import Any, Callable, Set, Tuple, List
import random

if __name__ == "__main__":
    Vector = Set[Any]


def one_point_crossover(v:Vector,
                        w:Vector,
                        c:int
)->Tuple[Vector,Vector]:
    
    """
    Perform one-point crossover between two vectors.

    Parameters:
    - v (Vector): The first vector.
    - w (Vector): The second vector.
    - c (int): The crossover point.

    Returns:
    Tuple[Vector, Vector]: Two vectors after one-point crossover.

    Example:
        v = [1, 2, 3, 4, 5]
        w = [6, 7, 8, 9, 10]
        c = 2
        result_v, result_w = one_point_crossover(v, w, c)
        print(result_v)  # Output: [1, 2, 8, 9, 10]
        print(result_w)  # Output: [6, 7, 3, 4, 5]
    
    """

    return v[:c] + w[c:], w[:c] + v[c:]

def n_points_crossover(v:Vector,
                       w:Vector,
                       l:list
)->Tuple[Vector,Vector]:
    
    """
    Perform n-points crossover between two vectors.

    Parameters:
    - v (Vector): The first vector.
    - w (Vector): The second vector.
    - l (List[int]): List of crossover points.

    Returns:
    Tuple[Vector, Vector]: Two vectors after n-points crossover.

    Example:
    
        v = [1, 2, 3, 4, 5, 6, 7]
        w = [8, 9, 10, 11, 12, 13, 14]
        l = [2, 4]
        result_v, result_w = n_points_crossover(v, w, l)
        print(result_v)  # Output: [1, 2, 10, 11, 5, 6, 7]
        print(result_w)  # Output: [8, 9, 3, 4, 12, 13, 14]
    
    """
    
    if len(l) == 1:
        return one_point_crossover(v,w,l[0])
    else:
        i,j = n_points_crossover(w[l[0]:],v[l[0]:],l[1:])
        return v[:l[0]] + i, w[:l[0]] + j

def random_crossover(v:Vector,
                     w:Vector,
                     p:int = None,
                     distr:Callable = random.random()
)-> Tuple[Vector,Vector]:
    
    """
    Perform random crossover between two vectors.

    Parameters:
    - v (Vector): The first vector.
    - w (Vector): The second vector.
    - p (float, optional): The probability of crossover for each element (default is 1/len(v)).
    - distr (Callable, optional): A function that generates random values between 0 and 1 (default is random.random).

    Returns:
    Tuple[Vector, Vector]: Two vectors after crossover.

    Example:
    
        v = [1, 2, 3, 4]
        w = [5, 6, 7, 8]
        result_v, result_w = random_crossover(v, w)
        print(result_v)  # Output: [1, 6, 3, 8]
        print(result_w)  # Output: [5, 2, 7, 4]
    
    """

    p = p if p is not None else 1/len(v)
    for i in range(len(v)):
        if p >distr():
            v[i],w[i] = w[i],v[i]
    return v,w


def random_shuffle(V:Vector
)->Vector:
    
    """
    Randomly shuffle the elements of a vector.

    Parameters:
    - V: The input vector to be shuffled.

    Returns:
    Vector: The vector with its elements randomly shuffled.

    Example:
        input_vector = [1, 2, 3, 4, 5]
        shuffled_vector = random_shuffle(input_vector)
        print(shuffled_vector)
    """

    return random.shuffle(V)


def uniform_crossover(probability:float,
                      W:List[Vector],
                      distribution:Callable = random.random()
)->List[Vector]:
    
    """
    Perform uniform crossover on a list of vectors.

    Parameters:
    - probability: The probability of performing uniform crossover for each element.
    - W: The list of vectors to undergo uniform crossover.
    - distribution: A function to generate random values (default is random.random).

    Returns:
    List[Vector]: The list of vectors after uniform crossover.

    Example:
        custom_distribution = ...
        input_vectors = ...
        result_vectors = uniform_crossover(0.8, input_vectors, custom_distribution)
        print(result_vectors)
    """

    v:Vector
    to_Ret:List[Vector]
    for i in range(1, len(W[0])):
        if probability > distribution():
            for j in W:
                v.append(j[i])
            random_shuffle(v)
            for index, j in enumerate(W):
                to_Ret[index] = v
    return to_Ret


