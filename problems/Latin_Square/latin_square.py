def generate_latin_square(n):
    """
    Generate a Latin square of order n.

    Parameters:
    - n: integer, the order of the Latin square.

    Returns:
    - list of lists, representing the Latin square.

    Example usage:
    latin_square = generate_latin_square(4)
    print("Latin Square:")
    for row in latin_square:
        print(row)
    """
    if n < 1:
        raise ValueError("Order of Latin square should be at least 1.")

    latin_square = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            latin_square[i][j] = (i + j) % n + 1

    return latin_square

# Example usage:
order = 4
latin_square = generate_latin_square(order)
print(f"Latin Square of order {order}:")
for row in latin_square:
    print(row)
