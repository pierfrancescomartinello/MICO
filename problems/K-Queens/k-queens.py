# Rappresentazione: Lista della posizione di riga delle regine per ogni colonna
#
#
#Quality: per ogni regina -> (numero di regine totali - alpha*numero di regine in scacco)/numero di regine
# quality = somma di prima()/numero di regine
#
# Tweak: cambio in modo random la posizione di un numero random di regine, usualmente 1

def queens(n, i, a, b, c):

    """
    Generate solutions to the N-Queens problem using backtracking.

    Parameters:
    - n (int): The size of the chessboard and the number of queens.
    - i (int): The current row being considered (default is 0).
    - a (list): A list representing the placement of queens in each row (default is an empty list).
    - b (list): A list to keep track of diagonals (default is an empty list).
    - c (list): A list to keep track of diagonals (default is an empty list).

    Yields:
    List[int]: A solution representing the placement of queens in each row.

    Example:
    for solution in queens(4):
        print(solution)
    """

    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a




def print_queens(n:int = 8):

    """
    Print solutions to the N-Queens problem with a visual representation of the chessboard.

    Parameters:
    - n: int, size of the chessboard (default is 8)
    """

    for s in queens(n, 0, [], [], []): solution = s
    print(solution)
    for i in range(n):
        row_index = solution.index(i)
        string = ("⬜"*(row_index) if (row_index)!= 0 else "") + ("👑") + ("⬜"*(n-row_index-1) if n-row_index-1!= 0 else "")
        print(string)

print_queens(8)