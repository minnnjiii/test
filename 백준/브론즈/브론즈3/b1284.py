# 집 주소
# 1284번

import sys
input = sys.stdin.readline

while True:

    sum = 0 
    N = str(input().strip())
    
    if N == "0" :
        break

    for i in range(0,len(N)) : 
        if N[i] == "1":
            sum += 2
        elif N[i] == "0":
            sum += 4
        else:
            sum += 3

    print(sum+len(N)+1) 