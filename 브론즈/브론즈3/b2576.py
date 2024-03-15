# 홀수
# 2576번 

nums= [] 
oddNum = [] # 홀수 담을 리스트
for i in range(7):
    nums.append(int(input()))

for num in nums:
    if num % 2 == 1 :
        oddNum.append(num)

if len(oddNum) > 0 :
    print(sum(oddNum))
    print(min(oddNum))
else:
    print(-1)
