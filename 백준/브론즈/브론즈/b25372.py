# 성택이의 은밀한 비밀번호

N = int(input())

for i in range(N):
    password = input()
    if len(password) >= 6 and len(password) <= 9:
        print("yes")
    else:
        print("no")