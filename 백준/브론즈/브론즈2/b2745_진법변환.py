# 진법 변환 

numList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
answer = 0 

for i , num in enumerate(N[::-1]):
    answer += int(B) ** i * numList.index(num)
print(answer)
