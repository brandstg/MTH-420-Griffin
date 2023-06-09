# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name>
<Class>
<Date>
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la
    
def gram(A):
    m = A.shape[0]
    n = A.shape[1]
    Q = A.copy()
    Q = np.array(Q, dtype=float)
    R = np.eye(n)
    
    n = Q.shape[1]
    for i in range(n):
        R[i,i] = np.sqrt(np.dot(Q[:,i].T, Q[:,i]))
        Q[:,i] = Q[:,i] / R[i,i]
        for j in range(i+1, n):
            R[i,j] = np.dot(Q[:,j], Q[:,i])
            Q[:,j] = Q[:,j] - R[i,j]*Q[:,i]
        
    return(Q,R)

# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q,R = gram(A)
    b = np.array(b, dtype=float)
    x = la.solve_triangular(R, np.dot(Q.T,b))
    return(x)

A = np.array([[1,1,1],[1,2,4],[1,3,9],[1,4,16]])
b = [1,3,19,2]
print(least_squares(A,b))

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data = np.load('housing.npy')
    n = data.shape[0]
    A = np.column_stack((data[:,0], np.ones(n)))
    b = data[:,1]
    
    m = least_squares(A,b)
    
    x = np.linspace(0,16,100)
    y = m[0]*x + m[1]
    ax1 = plt.subplot(211)
    ax1.plot(data[:,0], data[:,1], 'k', marker='x',lw=2, linestyle="")
    ax1.plot(x,y)
    plt.show()
    
line_fit()


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    from scipy import linalg as la
    data = np.load('housing.npy')
    n = data.shape[0]
    A = np.column_stack((data[:,0], np.ones(n)))
    b = data[:,1]
    
    f=[0,0,0,0]
    
    for j in range(4):
        A = np.vander(data[:,0],3*j+4)
        f[j] = np.poly1d(la.lstsq(A,b)[0])
    
    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)
    
    x = np.linspace(0,16,100)
    ax0.plot(data[:,0], data[:,1], 'k', marker='x',lw=2, linestyle="")
    ax0.plot(x,f[0](x))
    ax1.plot(data[:,0], data[:,1], 'k', marker='x',lw=2, linestyle="")
    ax1.plot(x,f[1](x))
    ax2.plot(data[:,0], data[:,1], 'k', marker='x',lw=2, linestyle="")
    ax2.plot(x,f[2](x))
    ax3.plot(data[:,0], data[:,1], 'k', marker='x',lw=2, linestyle="")
    ax3.plot(x,f[3](x))
    plt.show()
    
    fig.show()
    
polynomial_fit()


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")
    plt.show()

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
