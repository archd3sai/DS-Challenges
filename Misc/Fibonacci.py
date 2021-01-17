def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
def fibonacci2(n):
    '''dynamic programming, complexity = O(n)'''
    
    base1, base2 = 0, 1
    
    for i in range(n):
        base1, base2 = base2, base1 + base2
        print(base1, base2)
    return base1
    
memo = {0: 1, 1: 1}
def fibonacci4(n):
    '''Top down + memorization (dictionary), complexity = O(n)'''
    if n not in memo:
        memo[n] = fibonacci4(n-1) + fibonacci4(n-2)
    return memo[n]
