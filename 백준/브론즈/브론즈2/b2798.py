# 블랙잭
# 백준/2798번 

# n장의 카드를 모두 숫자가 보이도록 바닥에 놓음 
# 딜러는 숫자 m을 외침 

# 플레이어는 n장의 카드 중 3장의 카드를 고르는데 
# 고른 카드의 합이 m을 넘지 않으면서 m과 최대한 가깝게 만들어야 함
# 카드 3장의 합을 구해 출력하시오 

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
num = list(map(int,input().split())) 

ans = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ans.append(num[i]+num[j]+num[k])

for l in ans[:]:
    if l > m :
        ans.remove(l)

print(max(ans))