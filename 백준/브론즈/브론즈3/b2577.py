# 숫자의 개수
# 2577

import math

nums = []
for _ in range(3) :
    nums.append(int(input()))

num = math.prod(nums)

num = str(num)
for i in '0123456789' : 
    print(num.count(i))