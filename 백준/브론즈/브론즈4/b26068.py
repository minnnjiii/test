# 치킨댄스를 추는 곰곰이를 본 임스2 
# 26068번 

n = int(input()) # 선물받은 횟수

count = 0 # 임스가 사용할 기프티콘 개수
for i in range(n):
    rest = input().replace("D-", "").strip()
    rest = int(rest)
    if rest <= 90 : 
        count += 1

print(count)