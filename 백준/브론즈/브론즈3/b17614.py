# 369
# 백준/17614번

# 369게임이 N까지 규칙을 지키며 진행된다면 
# 그때까지의 들은 박수의 횟수 가 총 몇 번인지

n = int(input()) 

count = 0 #박수 count 

for i in range(1,n+1):
    for j in str(i) : 
        if j == "3" or j == "6" or j == "9":
            count += 1

print(count)