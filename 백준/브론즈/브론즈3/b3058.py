# 짝수를 찾아라
# 3058

# 7개의 자연수가 주어질 때, 
# 이들 중 짝수인 자연수들을 모두 골라 그 합을 구하고, 
# 고른 짝수들 중 최솟값을 찾는 프로그램을 작성하시오.
t = int(input())

for i in range(t):
    nums = list(map(int,input().split())) 
    even = [] 
    for num in nums:
        if num % 2 == 0 : 
            even.append(num) 
    
    print(sum(even),min(even)) 

