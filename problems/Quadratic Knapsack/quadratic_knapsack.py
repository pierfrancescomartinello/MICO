from itertools import product
import random

# Segna l'ordine delle città
# Quality:
#   vettore binario per rappresentare se l'elemento è presente
#   quality= (somma peso in knapsack rapportato al costo - alpha* somma peso che esce fuori dal knapsack) - beta*profitto se due elementi sono presenti
# Tweak:
#   Modifichiamo la soluzione
# IsIdeal:
#   non lo sappiamo

def generate_random_instance(size):
    weights = [random.randint(1, 10) for _ in range(size)]
    values = [random.randint(1, 10) for _ in range(size)]
    quadratic_terms = [
        [random.randint(0, 5) for _ in range(size)] for _ in range(size)
    ]
    return weights, values, quadratic_terms


def quadratic_knapsack_bruteforce(weights, values, quadratic_terms, capacity):
    n = len(weights)
    best_value = 0
    best_selection = None

    for selection in product([0, 1], repeat=n):
        total_weight = sum(weights[i] * selection[i] for i in range(n))
        if total_weight <= capacity:
            total_value = sum(values[i] * selection[i] for i in range(n))
            quadratic_penalty = sum(
                quadratic_terms[i][j] * selection[i] * selection[j]
                for i in range(n)
                for j in range(n)
            )
            total_value -= quadratic_penalty

            if total_value > best_value:
                best_value = total_value
                best_selection = selection

    return best_selection, best_value

size = 10
weights, values, quadratic_terms = generate_random_instance(size)
capacity = 15

print("Weights:", weights)
print("Values:", values)
print("Quadratic Terms:")
for row in quadratic_terms:
    print(row)

result, total_value = quadratic_knapsack_bruteforce(weights, values, quadratic_terms, capacity)

print("\nBest selection:", result)
print("Total value:", total_value)

