# python_intro.py
"""Python Essentials: Introduction to Python.
Griffin Brandstetter
MTH 420
4/14/2023
"""


# Problem 1 (write code below)

if __name__ == "__main__":
    print("Hello, world!") 

# Problem 2


def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    pi = 3.14159
    return 4/3 *pi*(r**3)


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, '   ',b,'   ',c, d, e)


# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    length = len(my_string)
    half = length // 2
    return my_string[:half]
    

def backward(my_string):
    return my_string[::-1]


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    animals = ["bear", "ant", "cat", "dog"]
    animals.append("eagle")
    animals[2] = "fox"
    animals.remove(animals[1])
    animals = sorted(animals)[::-1]
    x = animals.index('eagle')
    animals[x] = 'hawk'
    animals[-1] = animals[-1] + 'hunter'
    return animals


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if word[0] in vowels:
        ordway = word + 'hay'
    else:
        ordway = word[1:] + word[0] + 'ay'
        
    return(ordway)



# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    n = 101
    m = 101
    nm = n*m
    
    while n < 1000:
        m = 101
        while m < 1000:
            if n*m > nm:
                if backward(str(n*m)) == str(n*m):
                    nm = n*m
            m += 1
        n += 1
        
    return nm

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    ln = 0
    for j in range(n):
        j = float(j)
        ln += ((-1)**j)/(j+1)
    return(ln)
        

