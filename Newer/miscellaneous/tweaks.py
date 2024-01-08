from typing import Any, Callable, List
import random

if __name__ == "__main__":
    Vector = List[Any]

def macro_for_convolution(V:Vector,
                                p:float,
                                min:Any,
                                max:Any,
                                tweak:Callable,
                                function:Callable,
                                r:float = None,
                                sigma:float = None
)-> Vector:
    
    """
    Apply macro mutation for convolution to a vector.

    Parameters:
    - V (Vector): The input vector.
    - p (float): The probability of applying the convolution.
    - min (Any): The minimum allowable value after convolution.
    - max (Any): The maximum allowable value after convolution.
    - tweak (Callable): A function to tweak the individual components of the vector.
    - function (Callable): A function to generate random values for convolution.
    - r (float, optional): The range for convolution (default is None).
    - sigma (float, optional): The standard deviation for convolution (default is None).

    Returns:
    Vector: The vector after applying macro mutation for convolution.

    Example:
        input_vector = [1, 2, 3, 4, 5]
        result_vector = macro_for_convolution(input_vector, 0.5, 0, 10, tweak_function, random_function, r=0.1)
        print(result_vector)
    """

    toRetV:Vector
    for index, i in enumerate(V):
        if p > random.random():
            n = function(-r,r) if sigma != None else function(0,sigma)
            i_temp = tweak(i, n)
            toRetV[index] = i_temp if (i_temp >= min and i_temp <= max) else i
    return V

def bounded_uniform_convolution(V:Vector,
                                p:float,
                                r:float,
                                min:Any,
                                max:Any,
                                tweak:Callable
)-> Vector:
    
    """
    Apply bounded uniform convolution to a vector.

    Parameters:
    - V (Vector): The input vector.
    - p (float): The probability of applying the convolution.
    - r (float): The range for convolution.
    - min (Any): The minimum allowable value after convolution.
    - max (Any): The maximum allowable value after convolution.
    - tweak (Callable): A function to tweak the individual components of the vector.

    Returns:
    Vector: The vector after applying bounded uniform convolution.

    Example:
    
        input_vector = [1, 2, 3, 4, 5]
        result_vector = bounded_uniform_convolution(input_vector, 0.5, 0.1, 0, 10, tweak_function)
        print(result_vector)
    

    """

    return macro_for_convolution(V,p,min, max,tweak, random.random(), r, None)


def gaussian_convolution(V:Vector, 
                         p:float, 
                         r:float, 
                         min:Any, 
                         max:Any, 
                         tweak:Callable, 
                         sigma:float
)-> Vector:
    
    """
    Apply Gaussian convolution to a vector.

    Parameters:
    - V (Vector): The input vector.
    - p (float): The probability of applying the convolution.
    - r (float): Not used (since it's specific to bounded uniform convolution).
    - min (Any): The minimum allowable value after convolution.
    - max (Any): The maximum allowable value after convolution.
    - tweak (Callable): A function to tweak the individual components of the vector.
    - sigma (float): The standard deviation for Gaussian convolution.

    Returns:
    Vector: The vector after applying Gaussian convolution.

    Example:
    
        input_vector = [1, 2, 3, 4, 5]
        result_vector = gaussian_convolution(input_vector, 0.5, 0.1, 0, 10, tweak_function, sigma=0.2)
        print(result_vector)
    
    """

    return macro_for_convolution(V,p,min, max,tweak, random.gauss(), None, sigma)

