# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

# Test Cases
correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


def check_generator(n):
    """
    This function will generate the check list of the sudoku
    :param n: n * n sudoku
    :return: list contains the range of the number
    """

    check = []
    for integer in range(1, n + 1):
        check.append(integer)
    return check


def col(soduku):
    # This function will get and return the columns of the sudoku
    n = len(soduku)
    column = []
    column_n = 0
    pre_list = []
    cnt = 0
    while column_n <= n - 1:
        while cnt <= n - 1:
            pre_list.append(soduku[cnt][column_n])
            cnt += 1
        column_n += 1
        column.append(pre_list)
        cnt = 0
        pre_list = []
    return column


def check_int(sub):
    """
    This function will check whether the elements in
    the list is all integers from 1 to n

    :Input Type: list

    :rtype: Boolean
    """
    check = check_generator(len(sub))
    for ele in sub:
        if ele not in check:
            return False
    return True


def check_sudoku(sudo):
    # Check whether the numbers in list is number
    for integer in sudo:
        if not check_int(integer):
            return False
    # Check the rows
    for rows in sudo:
        if len(rows) != len(set(rows)):
            return False
    # Check the Columns
    column = col(sudo)
    for cols in column:
        if len(cols) != len(set(cols)):
            return False
    return True


print check_sudoku(incorrect)
# >>> False

print check_sudoku(correct)
# >>> True

print check_sudoku(incorrect2)
# >>> False

print check_sudoku(incorrect3)
# >>> False

print check_sudoku(incorrect4)
# >>> False

print check_sudoku(incorrect5)
# >>> False
