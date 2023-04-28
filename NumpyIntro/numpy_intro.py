# numpy_intro.py
"""Python Essentials: Intro to NumPy.
Griffin Brandstetter
MTH 420
4/26/23
"""

import numpy as np

def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A = np.array( [ [3, -1, 4], [1, 5, -9] ] )
    B = np.array( [ [2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -2] ] )
    AB = np.dot(A, B)
    return(AB)



def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array( [ [3, 1, 4], [1, 5, 9], [-5, 3, 1] ] )
    M = -1 * np.dot(np.dot(A,A),A) + 9 * np.dot(A,A) - 15 * A
    return(M)



def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.ones((7,7))
    A = np.triu(A)
    B = np.full((7,7), 6)
    B = np.triu(B)
    B = B -1
    ABA = np.dot(np.dot(A,B),A)
    ABA = ABA.astype(np.int64)
    return(ABA)
    


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    B = np.copy(A)
    index = B < 0
    B[index] = 0
    return(B)


def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.arange(6).reshape((2,3))
    B = np.full((3,3), 3)
    B = np.tril(B)
    C = -2 * np.eye(3)
    OATI = np.hstack((np.zeros((3,3)), np.transpose(A), np.eye(3)))
    AOO = np.hstack((A, np.zeros((2,5))))
    BOC = np.hstack((B, np.zeros((3,2)), C))
    return(np.vstack((OATI, AOO, BOC)))
    
print(prob5())
           
def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    B = 1/A.sum(axis=0)
    return(B*A)

C = np.arange(16).reshape((4,4))
print(prob6(C))


def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    raise NotImplementedError("Problem 7 Incomplete")
