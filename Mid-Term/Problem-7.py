# Problem 7
# Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because .

#def general_poly (L):
#    """ L, a list of numbers (n0, n1, n2, ... nk)
#    Returns a function, which when applied to a value x, returns the value 
#    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE


# Paste your function here
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def to_apply (x):
        n = 0
        for i in L:
            n = x*n + i
        return n
    return to_apply
