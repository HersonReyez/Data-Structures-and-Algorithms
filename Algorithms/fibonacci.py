#####################################
# LeetCode - 509. Fibonacci Number
#####################################
number = 10

# Recursive version - O(n^2)
def fibonacciRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fibonacciRec(n-1) + fibonacciRec(n-2)
    
print(fibonacciRec(number))

# Dinamic Progaming
# Top Down Memorization - O(n)
memo = {0:0, 1:1}
def fibonacciMemo(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacciMemo(n-1) + fibonacciMemo(n-2)
        return memo[n]
    
print(fibonacciMemo(number))


# Dinamic Programing
# Bottom Up Tabulation
def fibonacciTab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    array = [0] * (n + 1)
    array[1] = 1
    for i in range(2, n + 1):
        array[i] = array[i-2] + array[i-1]
    return array[n]

print(fibonacciTab(number))



# Iterative version - O(n)
# variable constant space 
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev = 0
    current = 1
    for i in range(2, n + 1):
        prev, current = current, prev + current
    return current
    
print(fibonacci(number))

# Binet’s Formula - O(log n)
def fib(n):
    golen_ratio = (1 + (5 ** 0.5)) / 2
    return int(round((golen_ratio ** n) / (5 ** 0.5)))

print(fib(number))