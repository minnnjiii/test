# 거스름돈
# 백준_5585번


coins = [500,100,50,10,5,1]

# 1000엔 - purchase 했을 때 가장 적은 잔돈의 개수 
# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔


money = 1000 - int(input()) 
count = 0

for coin in coins : 
    count += money // coin
    money %= coin

print(count)