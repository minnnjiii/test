# 카드2
# 백준/2164번 

import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) 

deque = deque([i for i in range(1,n+1)])

while True:
    if len(deque) <= 1 : 
        break 

    deque.popleft()
    num = deque.popleft()
    deque.append(num) 
    
print(deque[0])