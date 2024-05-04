# 팩토리얼 3 

# N! 을 출력하는 문제 

N = int(input())
factorial = 1 
for i in range(1, N+1):
    factorial *= i 
print(factorial)