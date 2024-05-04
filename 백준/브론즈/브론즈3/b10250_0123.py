# ACM 호텔

T = int(input())

for i in range(T):
    H, W, N = map(int,input().split())
    floor = N % H 
    roomNumber = (N // H) + 1
    
    if floor == 0 : 
        print((H*100)+roomNumber-1 )
    else:
        print((floor * 100) + roomNumber)
        
        