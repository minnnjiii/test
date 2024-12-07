import sys

input = sys.stdin.readline

t = int(input()) 

for _ in range(t):
    a, b = map(int, input().split())
    last_digit = int(str(a)[-1])  # a의 마지막 자리 숫자

    if b == 0:
        print(1)  # b가 0인 경우 항상 결과는 1
        continue

    # 마지막 자리 숫자에 따른 반복 패턴
    patterns = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    
    pattern = patterns[last_digit]  # 해당 숫자의 반복 패턴
    index = (b - 1) % len(pattern)  # 패턴에서 b번째의 인덱스 계산
    result = pattern[index]  # 결과는 패턴의 해당 인덱스 값

    # 마지막 자리 0인 경우 10번 컴퓨터 출력
    print(10 if result == 0 else result)
