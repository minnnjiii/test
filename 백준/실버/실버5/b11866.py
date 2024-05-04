# 요세푸스 문제 0
# 백준/11866번

import sys
input = sys.stdin.readline



N,K = map(int,input().split())

'''
1,2,3,4,5,6,7 
6 3 1 7 5 2 4
'''


yo = [i for i in range(1,N+1)]
que = []

idx = 0
while yo:
    idx += K - 1
    if idx >= len(yo):
        idx %= len(yo)
    que.append(str(yo.pop(idx)))

print("<",", ".join(que), ">",sep="")