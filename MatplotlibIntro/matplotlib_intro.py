# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Griffin Brandstetter
MTH 420
4/28/23
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.normal(size=(n,n))
    M = np.mean(A, axis=1)
    V = np.var(M)
    return(V)

    

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    P = [var_of_means(100), var_of_means(200), var_of_means(300), var_of_means(400), var_of_means(500), var_of_means(600), var_of_means(700), var_of_means(800), var_of_means(900), var_of_means(1000)]
    plt.plot(P) 
    plt.show()  
    
prob1()


# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    cos = np.cos(x)
    sin = np.sin(x)
    arctan = np.arctan(x)
    plt.plot(x, cos)
    plt.plot(x, sin)
    plt.plot(x, arctan)
    plt.show()
    
prob2()


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2, 1, 40, endpoint=False)
    f1 = 1 / (x1-1)
    x2 = np.linspace(1, 6, 40)[1:]
    f2 = 1 / (x2-1)
    plt.plot(x1, f1, 'm:', lw = 4)
    plt.plot(x2, f2, 'm:', lw = 4)
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)
    plt.show()
    
prob3()


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2*np.pi, 100)
    xmin = 0
    xmax = 2*np.pi
    ymin = -2
    ymax = 2
    fig, axes = plt.subplots(2, 2)
    fig.suptitle('Some Sines')
    axes[0,0].plot(x, np.sin(x), 'g')
    axes[0,0].set_title('Plot A')
    axes[0,0].axis([xmin, xmax, ymin, ymax]) 
    axes[0,1].plot(x, np.sin(2*x), 'r--')
    axes[0,1].set_title('Plot B')
    axes[0,1].axis([xmin, xmax, ymin, ymax]) 
    axes[1,0].plot(x, 2*np.sin(x), 'b--')
    axes[1,0].set_title('Plot C')
    axes[1,0].axis([xmin, xmax, ymin, ymax]) 
    axes[1,1].plot(x, 2*np.sin(2*x), 'm:')
    axes[1,1].set_title('Plot D')
    axes[1,1].axis([xmin, xmax, ymin, ymax]) 
    plt.show()

prob4()


# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    '''data = np.load('FARS.npy')
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    ax1.plot(data[:,1], data[:,2], 'k', marker=',',lw=0, linestyle="")
    ax1.axis("equal")
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')
    ax2.hist(data[:,0],bins = 24)
    ax2.set_xlabel('Time of Day')
    plt.show'''


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = x.copy()
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.sin(Y) / (X*Y)
    plt.subplot(221)
    plt.pcolormesh(X, Y, Z, cmap="viridis", shading="auto")
    plt.colorbar()
    plt.xlim(-np.pi, np.pi)
    plt.ylim(-np.pi, np.pi)
    plt.axis("equal")
    
    plt.subplot(222)
    plt.contour(X, Y, Z, 10, cmap="coolwarm")
    plt.colorbar()

    
    plt.show

prob6()

