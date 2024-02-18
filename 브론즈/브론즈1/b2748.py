# 피보나치 수 2 
# 2748번

memo = {}

def fibo(n):

    if n == 1 or n == 2 : 
        return 1 

    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    
    return memo[n]

print(fibo(int(input())))