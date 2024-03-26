# 남욱이의 닭장
# 백준/11006번 



# input
# 모든 닭의 다리수의 합 N 
# 닭의 수 M

# print
# 다리가 잘린 닭의 수 U
# 멀쩡한 닭의 수 T


T = int(input()) # test case

for _ in range(T) :
    n,m = map(int,input().split()) 
    u = 2*m - n
    t = m - u
    print(u,t)