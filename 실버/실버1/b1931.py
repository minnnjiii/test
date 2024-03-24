# 회의실 배정
# 백준_1931번

# 최대 사용할 수 있는 회의의 최대 개수를 출력하라

n = int(input()) 

meeting = []
for _ in range(n):
    start, end = map(int,input().split()) 
    meeting.append((start,end))

# 종료 시간을 기준으로 정렬
meeting.sort(key=lambda x: (x[1],x[0]))
print(meeting)

count = 0 # 회의실 사용 개수

last_time = 0 # 마지막 사용 시간

for start, end in meeting:
    if start >= last_time:
        last_time = end 
        count += 1

print(count)

