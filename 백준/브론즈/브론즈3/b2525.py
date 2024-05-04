H, M = map(int,input().split())
add = int(input())

t = H * 60 + M+add
hour = t // 60
min = (t % 60) 

if hour > 23: 
    hour -= 24

print(hour,min)