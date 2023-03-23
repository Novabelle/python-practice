# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)




























def return_first_five_fibonacci_as_a_list():
    """Return the first five Fibonacci numbers as a list."""
    return [fibonacci(i) for i in range(5)]
    
