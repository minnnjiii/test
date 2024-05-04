# 영수증

sum = int(input()) # 책 10권 총 가격
for i in range(9):
    sum -= int(input())

print(sum) # 나머지 한 권 가격