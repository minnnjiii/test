# 핸드폰 번호 궁합
# 백준/17202번

# 핸드폰 번호는 리스트로 받기
A = list(map(int, input()))
B = list(map(int, input()))

# 테이블 만들기 
arr = [0]*16

# 숫자 하나씩 번갈아가면서 A와 B 번호 합치기
for i in range(16):
    # A부터 
    if i % 2 == 0:
        arr[i] = A[i//2] # 테이블에 순서대로 숫자 넣기
    # 그 다음은 B
    else:
        arr[i] = B[i//2]

# 궁합률 구하기
while len(arr) != 2: # arr가 2가 될 때까지 계산
    ans = [] 
    for i in range(len(arr)-1):
        # 인접한 두 숫자를 더한 후 
        # 10으로 나눈 나머지를 구해 일의 자리 숫자만 저장함
        num = (arr[i]+arr[i+1]) % 10 
        ans.append(num)
    arr = ans

print(*arr, sep="") 