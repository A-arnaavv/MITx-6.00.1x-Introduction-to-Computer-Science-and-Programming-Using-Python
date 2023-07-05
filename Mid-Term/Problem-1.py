# Problem 1-1
Suppose x = "pi" and y = "pie". The line of code x, y = y, x will swap the values of x and y, resulting in x = "pie" and y = "pi".
Answer-True


# Problem 1-2
Suppose x is an integer in the following code:

def f(x):
    while x > 3:
        f(x+1)

For any value of x, all calls to f are guaranteed to never terminate.
Answer-False


# Problem 1-3
A Python program always executes every line of code written at least once.
Answer-False


# Problem 1-4
Suppose you have two different functions that each assign a variable called x. Modifying x in one function means you always modify x in the other function for any x.
Answer-False


# Problem 1-5
The following code will enter an infinite loop for all values of i and j.

while i >= 0:
    while j >= 0:
        print(i, j)
Answer-False


# Problem 1-6
It is always possible and feasible for a programmer to come up with test cases that run through every possible path in a program.
Answer-False


# Problem 1-7
Assume f() is defined. In the statement a = f(), a is always a function.
Answer-False


# Problem 1-8
A program that keeps running and does not stop is an example of a syntax error.
Answer-False


# Problem 1-9
Consider the following function.

def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)

A new object of type list is created for each recursive invocation of f.
Answer-True


# Problem 1-10
A tuple can contain a list as an element.
Answer-True
