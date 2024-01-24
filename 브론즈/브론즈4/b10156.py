# 과자 

# K = 과자 한 개의 가격
# N = 사려고 하는 과자의 개수 
# M = 현재 가진 돈의 액수

K, N, M = map(int,input().split())

if M - (K * N) < 0 :
    print(abs(M-(K*N)))
else: 
    print(0)