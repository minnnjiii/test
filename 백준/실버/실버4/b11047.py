# 동전 0 
# 백준_11047번

# 동전은 총 n종류
# 적절히 사용하여 만든 가치의 합 k

# k원을 만드는데 필요한 동전 개수의 최소값을 구하라 

n, k = map(int,input().split()) 

coins = [] # 동전 가치

for _ in range(n) : 
    coins.append(int(input())) 

coins.sort(reverse=True) # 동전 금액 큰 순서대로 정렬 

count = 0 # 동전 갯수
for coin in coins: 
    
    count += k//coin
    k %= coin 

print(count) 
