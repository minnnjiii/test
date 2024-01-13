# 문자열 반복

T = int(input())

for _ in range(T):
    count, word = input().split()
    for x in word:
        print(x*int(count),end="")
    print()
    