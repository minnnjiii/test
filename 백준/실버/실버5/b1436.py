# 영화감독 숌
# 백준/1436번

import sys
input = sys.stdin.readline

N = int(input()) 


ans = 666
count = 0

while True:
    if '666' in str(ans):
        count += 1

    if count == N:
        break

    ans += 1

print(ans)

'''
666

1666
2666
3666
4666
5666

6660
6661
6662
6663
6664
6665
6666
6667
6668
6669

7666
8666
9666
10666
11666
12666
13666
14666
15666

16661
16666

95666
96661

'''