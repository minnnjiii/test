# 행렬 덧셈

# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

A, B = [], []
N, M = map(int, input().split())

for row in range(N):
    row = list(map(int,input().split()))
    A.append(row)
    
for row in range(N):
    row = list(map(int,input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end = ' ')
    print() # 줄바꿈 
    

    
    