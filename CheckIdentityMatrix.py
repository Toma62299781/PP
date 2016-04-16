# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def square_check(mat):
    """
    Check whether the input matrix is square matrix
    :param mat: list
    :return: Boolean
    """
    return len(mat) == len(mat[0])

def i_check(m, n, row):
    """
    Check whether the input row is the right row of identity matrix
    :param m: row of input matrix
    :param n: the n * n matrix, the number n
    :param row: the row being checked
    :return: Boolean
    """
    if m.count(1) == 1 and m.count(0) == n-1:
        if m[row] == 1:
            return True
    else:
        return False

def is_identity_matrix(matrix):
    # First check whether the matrix is a square matrix
    if square_check(matrix):
        n = len(matrix)
        cnt = 0
        # Check the rows of the matrix one by one
        for cnt in range(0, n):
            if not i_check(matrix[cnt], n, cnt):
                return False
        return True
    else:
        return False





# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False