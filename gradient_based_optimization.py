from typing import Any, Callable, Set

if __name__ == "__main__":
    Vector = list[Any]

def gradient_ascent(X:Vector,
                    alpha:float,
                    gradient:Callable,
                    isIdeal:Callable,
                    mul:Callable,
                    f:Callable,
                    sum:Callable,
                    time:int
)-> Vector:
    while not isIdeal(X) and time > 0:
        X = sum(X, mul(alpha, gradient(f(X))))
        time -=1
    return X

def gradient_descent(X:Vector,
                     alpha:float,
                     gradient:Callable,
                     isIdeal:Callable,
                     mul:Callable,
                     f:Callable,
                     dif:Callable,
                     time:int
)-> Vector:
    while not isIdeal(X) and time > 0:
        X = dif(X, mul(alpha, gradient(f(X))))
        time -=1
    return X


def newton(X:Vector,
           alpha:float,
           gradient:Callable,
           hessian_invert:Callable,
           isIdeal:Callable,
           f:Callable,
           mul:Callable,
           dif:Callable,
           time:int
)-> Vector:
    while not isIdeal(X) and time >0:
        X = dif(X, mul(mul(alpha, hessian_invert(f(X))), gradient(f(X))))
    return X


def gradient_ascent_with_restarts(X:Vector,
                                  alpha:float,
                                  time:int,
                                  gradient:Callable,
                                  f:Callable,
                                  gt:Callable,
                                  mul:Callable,
                                  sum:Callable,
                                  rand:Callable,
                                  modulo:Callable
)-> Vector:
    X_Temp = X
    while time > 0:
        while modulo(gradient(f(X))) != 0:
            X = sum(X, mul(alpha, gradient(f(X))))
        if gt(f(X), f(X_Temp)): X_Temp = X
        X = rand()
        time -= 1
    return X_Temp


def gradient_descent_with_restarts(X:Vector,
                                   alpha:float,
                                   time:int,
                                   gradient:Callable,
                                   f:Callable,
                                   gt:Callable,
                                   mul:Callable,
                                   dif:Callable,
                                   rand:Callable,
                                   modulo:Callable
)-> Vector:
    X_Temp = X
    while time > 0:
        while modulo(gradient(f(X))) != 0:
            X = dif(X, mul(alpha, gradient(f(X))))
        if gt(f(X), f(X_Temp)): X_Temp = X
        X = rand()
        time -= 1
    return X_Temp

