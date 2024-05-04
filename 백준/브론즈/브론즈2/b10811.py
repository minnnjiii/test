# 바구니 뒤집기 _ 10811

N , M = map(int,input().split())

b = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int,input().split())
    b[i:j+1] = reversed(b[i:j+1])
b.remove(b[0])
print(*b)