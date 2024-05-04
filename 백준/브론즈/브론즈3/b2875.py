# 대회 or 인턴
# 2875

n, m , k = map(int,input().split()) # 여,남,인턴
 
team = 0 

while True:
    n -= 2
    m -= 1

    if n < 0 or m < 0 or n+m <k : 
        break

    team += 1

print(team)