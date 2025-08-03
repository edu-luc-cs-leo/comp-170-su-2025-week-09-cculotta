def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW
# Recursive versions of assignment methods

def sum_of_digits(n):
    """Recursively computes the sum of digits of n."""
    if n < 10:
        result = n
    else:
        result = sum_of_digits(n // 10) + (n % 10)
    return result

def count_occurrences(data_list, target):
    """Recursively counts how many times target appears in data_list."""
    if len(data_list) == 0:
        result = 0
    else:
        if data_list[0] == target:
            result = 1 + count_occurrences(data_list[1:], target)
        else:
            result = count_occurrences(data_list[1:], target)
    return result

# Iterative replacements for week09.factorial and week09.fibonacci

def factorial_iterative(n):
    """Computes n! iteratively."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci_iterative(n):
    """Computes F(n) = F(n-1) + F(n-2) iteratively, with F(1)=1 and F(2)=2."""
    if n == 1 or n == 2:
        result = n
    else:
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        result = b
    return result

