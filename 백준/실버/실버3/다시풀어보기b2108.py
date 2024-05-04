# 통계학
# 백준/2108번

from collections import Counter
import sys
input = sys.stdin.readline


n = int(input())

num = []

_sum = 0 
for _ in range(n):
    x = int(input())
    num.append(x) 
    _sum += x

num.sort() 
print(round(_sum/n))
print(num[n//2])

cnt_num = Counter(num).most_common()
if len(cnt_num) > 1 and cnt_num[0][1] == cnt_num[1][1]:
    print(cnt_num[1][0])
else:
    print(cnt_num[0][0])

print(num[-1]-num[0])
