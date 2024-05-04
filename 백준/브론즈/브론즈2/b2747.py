# 피보나치 수 

memo = {1:1,2:1}
def fibo(n):
    

    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    
    return memo[n]

print(fibo(int(input())))