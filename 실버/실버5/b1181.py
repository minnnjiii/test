# 단어 정렬
# 백준/1181번

import sys
input = sys.stdin.readline

n = int(input()) 

word = []
for _ in range(n):
    word.append(input().strip())

word = list(set(word))

word.sort()
word.sort(key=len)

for i in word:
    print(i)