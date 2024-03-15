# 지능형 기차 2

train = [0] * 10

for i in range(10):
    drop, board = map(int,input().split())
    train[i] = (train[i-1] - drop)
    train[i] += board

print(max(train))
