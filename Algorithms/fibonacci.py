number = 35
## Recursion ##
def fibonacciRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fibonacciRec(n-1) + fibonacciRec(n-2)
    
print(fibonacciRec(number))

## Iterative ##
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n >= 2:
        a = 0
        b = 1
        c = -1
        counter = 2
        while counter <= n:
            c = a + b 
            a = b
            b = c
            counter += 1
        return c
        
    
    
print(fibonacci(number))
